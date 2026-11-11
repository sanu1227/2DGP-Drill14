"""작업 폴더와 무관하게 수업 자료를 찾는다."""

from pathlib import Path

ASSET_DIRECTORY = Path(__file__).resolve().parent


def asset_path(name):
    return str(ASSET_DIRECTORY / name)
