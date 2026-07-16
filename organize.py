import shutil
from pathlib import Path
import subprocess
import re

ROOT = Path(__file__).parent

LANGUAGE_MAP = {
    ".py": "Python",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".c": "C",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".php": "PHP",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".scala": "Scala",
    ".sql": "SQL",
    ".mysql": "MySQL",
}

IGNORE = {
    ".md",
    ".txt",
    ".json",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
}

count = 0

folders = [f for f in ROOT.iterdir() if f.is_dir()]

for problem_folder in folders:

    if problem_folder.name in LANGUAGE_MAP.values():
        continue

    language = None

    for file in problem_folder.iterdir():

        if file.is_dir():
            continue

        ext = file.suffix.lower()

        if ext in IGNORE:
            continue

        if ext in LANGUAGE_MAP:
            language = LANGUAGE_MAP[ext]
            break

    if language is None:
        continue

    language_folder = ROOT / language
    language_folder.mkdir(exist_ok=True)

    destination = language_folder / problem_folder.name

    if destination.exists():
        print(f"Already exists: {problem_folder.name}")
        continue

    shutil.move(str(problem_folder), str(destination))
    print(f"Moved: {problem_folder.name} -> {language}")
    count += 1

def get_repo_url():
    """
    Returns:
    https://github.com/<username>/<repo>/tree/main
    """

    try:
        remote = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            text=True
        ).strip()

        # SSH
        # git@github.com:user/repo.git
        if remote.startswith("git@github.com:"):
            remote = remote.replace("git@github.com:", "https://github.com/")

        # HTTPS
        # https://github.com/user/repo.git
        remote = remote.replace(".git", "")

        return remote + "/tree/main"

    except Exception:
        return None


readme = ROOT / "README.md"

if readme.exists():

    repo_url = get_repo_url()

    if repo_url is None:
        print("Couldn't determine GitHub repository.")
    else:

        text = readme.read_text(encoding="utf-8")

        folder_map = {}

        # Build mapping automatically
        for language in LANGUAGE_MAP.values():

            language_path = ROOT / language

            if not language_path.exists():
                continue

            for folder in language_path.iterdir():

                if folder.is_dir():
                    folder_map[folder.name] = f"{language}/{folder.name}"

        # Replace every old link
        for old_folder, new_folder in folder_map.items():

            old_link = f"{repo_url}/{old_folder}"
            new_link = f"{repo_url}/{new_folder}"

            text = text.replace(old_link, new_link)

        readme.write_text(text, encoding="utf-8")

        print("README links updated.")

print(f"\nDone! {count} folders moved.")
