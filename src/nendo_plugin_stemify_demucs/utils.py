"""Utility functions for the stemify package."""
import multiprocessing
from typing import List


def build_command_from_stem_types(
    stem_types: List[str],
    model: str,
    track_path: str,
) -> List[str]:
    """Build a demucs command from stem types.

    Args:
        stem_types (List[str]): The stem types to generate.
        model (str): The demucs model to use.
        track_path (str): The path to the track to stemify.

    Returns:
        List[str]: The demucs command.
    """
    cores = multiprocessing.cpu_count()

    run_command = [
        "demucs",
        "-j",
        str(cores),
        "-n",
        model,
    ]
    for stem_type in stem_types:
        if "no_" in stem_type and stem_type.replace("no_", "") in stem_types:
            run_command.extend(["--two-stems", stem_type.replace("no_", "")])
    run_command.append(track_path)

    return run_command
