__all__ = [
    "M3U8Downloader",
    "M3U8DownloaderError",
    "M3U8DownloaderWarning",
    "__author__",
    "__description__",
    "__name__",
    "__version__"
]
__author__ = "coldsofttech"
__description__ = """
M3U8 Downloader is a Python class designed to download and concatenate video files from M3U8 playlists.
This class provides functionality to handle M3U8 playlist files, download video segments, concatenate them
into a single video file, and manage various error conditions.
"""
__name__ = "pym3u8downloader"
__version__ = "0.1.8"

from pym3u8downloader.downloader import M3U8Downloader
from pym3u8downloader.exceptions import M3U8DownloaderError, M3U8DownloaderWarning
