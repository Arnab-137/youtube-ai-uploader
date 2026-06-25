from pathlib import Path

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
    ".webm",
    ".m4v"
}

def scan_folder(folder):
    videos = []

    folder = Path(folder)

    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in VIDEO_EXTENSIONS:
            videos.append(file)

    return sorted(videos)
