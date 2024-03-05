"""Default settings for the Nendo demucs stemifier."""
from typing import ClassVar, List, Literal

from nendo import NendoConfig
from pydantic import Field


class DemucsConfig(NendoConfig):
    """Default settings for the Nendo demucs stemifier.

    Attributes:
        demucs_model (Literal["htdemucs_6s", "htdemucs_ft", "mdx_extra"], optional): Which demucs model to use. Defaults to "htdemucs_6s".
        stem_types (ClassVar[List[str]]): List of stem types to use. Defaults to ["vocals", "drums", "bass", "other", "guitar", "piano"].
    """

    demucs_model: Literal[
        "htdemucs_6s",
        "htdemucs_ft",
        "mdx_extra",
        "htdemucs",
        "mdx_extra_q",
    ] = Field("mdx_extra")
    stem_types: ClassVar[List[str]] = [
        "vocals",
        "drums",
        "bass",
        "other",
    ]
