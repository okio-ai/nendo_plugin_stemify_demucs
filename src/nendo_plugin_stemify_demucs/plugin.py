"""A nendo plugin for music stemification."""
import os
import shutil
import subprocess
from logging import Logger
from typing import List, Optional

from nendo import Nendo, NendoConfig, NendoGeneratePlugin, NendoTrack

from .config import DemucsConfig
from .utils import build_command_from_stem_types

settings = DemucsConfig()


class DemucsStemifier(NendoGeneratePlugin):
    """A nendo plugin for stemification based on Demucs by Facebook AI Research.

    https://github.com/facebookresearch/demucs/
    Can use either the htdemucs_6s, htdemucs_ft, or mdx_extra models.
    Also allows control of which stem types to generate.

    Examples:
        ```python
        from nendo import Nendo, NendoConfig

        nendo = Nendo(config=NendoConfig(plugins=["nendo_plugin_stemify_demucs"]))
        track = nendo.library.add_track_from_file(
            file_path="path/to/file.wav",
        )

        stems = nendo.plugins.stemify_demucs(
            track=track,
            stem_types=["vocals", "drums", "bass", "other", "guitar", "piano"],
            model="htdemucs_6s"
        )

        stems.tracks()[0].play()

        stems = nendo.plugins.stemify_demucs(
            track=track,
            stem_types=["vocals", "no_vocals"],
            model="mdx_extra"
        )

        vocals, background = stems.tracks()[0], stems.tracks()[1]
        ```
    """

    nendo_instance: Nendo = None
    config: NendoConfig = None
    logger: Logger = None

    @NendoGeneratePlugin.run_track
    def stemify_track(
            self,
            track: NendoTrack,
            stem_types: Optional[List[str]] = None,
            model: Optional[str] = None,
    ):
        """Stemify a track.

        Args:
            track (NendoTrack): The track to stemify.
            stem_types (List[str], optional): The stem types to generate. Defaults to None.
            model (str, optional): The demucs model to use. Defaults to None.

        Returns:
            List[NendoTrack]: A list of stems.
        """
        if model is None:
            model = (
                self.config.demucs_model
                if hasattr(self.config, "demucs_model")
                else settings.demucs_model
            )

        if stem_types is None:
            stem_types = (
                self.config.stem_types
                if hasattr(self.config, "stem_types")
                else settings.stem_types
            )

        stems: List[NendoTrack] = []
        track_local = track.resource.src

        subprocess.run(
            build_command_from_stem_types(stem_types, model, track_local), shell=False
        )

        track_filename = os.path.basename(track_local).rsplit(".", 1)[0]

        for stem_type in stem_types:
            stem_file = os.path.join(
                os.getcwd(),
                "separated",
                model,
                track_filename,
                stem_type + ".wav",
            )
            stem = self.nendo_instance.library.add_related_track(
                file_path=stem_file,
                related_track_id=track.id,
                track_meta={"title": f"{stem_type} Stem", "stem_type": stem_type},
                track_type="stem",
                relationship_type="stem",
            )
            stems.append(stem)

        # clean up original stems generated from demucs
        shutil.rmtree(os.path.join(os.getcwd(), "separated", model, track_filename))
        return stems
