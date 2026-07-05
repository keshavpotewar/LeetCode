import shutil
from pathlib import Path

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

# Make a copy of the folder list because we'll be moving folders
folders = [f for f in ROOT.iterdir() if f.is_dir()]

for problem_folder in folders:

    # Skip language folders if script is run again
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

    # Skip if already moved
    if destination.exists():
        print(f"Already exists: {problem_folder.name}")
        continue

    shutil.move(str(problem_folder), str(destination))

    print(f"Moved: {problem_folder.name} -> {language}")
    count += 1

print(f"\nDone! {count} folders moved.")
