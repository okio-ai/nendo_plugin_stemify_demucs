# -*- encoding: utf-8 -*-
"""Tests for the Nendo Demucs Stemifier plugin."""
import unittest

from nendo import Nendo, NendoConfig

nd = Nendo(
    config=NendoConfig(
        library_path="./library",
        log_level="INFO",
        plugins=["nendo_plugin_stemify_demucs"],
    ),
)


class StemifyPluginTests(unittest.TestCase):
    def test_run_stemify_collection_htdemucs_6s(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.mp3")
        collection = nd.library.add_collection(
            name="test_collection",
            track_ids=[track.id],
        )

        gen_collection = nd.plugins.stemify_demucs(
            collection=collection,
            model="htdemucs_6s",
            stem_types=["vocals", "drums", "bass", "other", "guitar", "piano"],
        )

        self.assertEqual(len(nd.library.get_collection_tracks(gen_collection.id)), 6)
        self.assertEqual(len(nd.library.get_tracks()), 7)

    def test_run_process_stemify_collection_htdemucs_6s(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.mp3")
        collection = nd.library.add_collection(
            name="test_collection",
            track_ids=[track.id],
        )

        gen_collection = collection.process(
            "nendo_plugin_stemify_demucs",
            model="htdemucs_6s",
            stem_types=["vocals", "drums", "bass", "other", "guitar", "piano"],
        )

        self.assertEqual(len(nd.library.get_collection_tracks(gen_collection.id)), 6)
        self.assertEqual(len(nd.library.get_tracks()), 7)

    def test_run_stemify_track_htdemucs_6s(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.mp3")

        stems = nd.plugins.stemify_demucs(
            track=track,
            model="htdemucs_6s",
            stem_types=["vocals", "drums", "bass", "other", "guitar", "piano"],
        )

        self.assertEqual(len(stems.tracks()), 6)
        self.assertEqual(len(nd.library.get_tracks()), 7)

    def test_run_stemify_collection_htdemucs_ft(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.mp3")
        collection = nd.library.add_collection(
            name="test_collection",
            track_ids=[track.id],
        )

        gen_collection = nd.plugins.stemify_demucs(
            collection=collection,
            model="htdemucs_ft",
            stem_types=["vocals", "drums", "bass", "other"],
        )

        self.assertEqual(len(nd.library.get_collection_tracks(gen_collection.id)), 4)
        self.assertEqual(len(nd.library.get_tracks()), 5)

    def test_run_stemify_collection_mdx_extra(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.mp3")
        collection = nd.library.add_collection(
            name="test_collection",
            track_ids=[track.id],
        )

        gen_collection = nd.plugins.stemify_demucs(
            collection=collection,
            model="mdx_extra",
            stem_types=["vocals", "no_vocals"],
        )

        self.assertEqual(len(nd.library.get_collection_tracks(gen_collection.id)), 2)
        self.assertEqual(len(nd.library.get_tracks()), 3)


if __name__ == "__main__":
    unittest.main()
