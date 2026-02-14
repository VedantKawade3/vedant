import os
import argparse
from pathlib import Path

# folders to show but NOT traverse inside
BLOCKED = {".git", "node_modules", "__pycache__"}

# colors (works in modern terminals)
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"


def build_tree(root: Path, dirs_only=False, prefix=""):
    lines = []

    try:
        entries = list(os.scandir(root))
    except PermissionError:
        return []

    # sort directories first
    entries.sort(key=lambda e: (not e.is_dir(), e.name.lower()))

    if dirs_only:
        entries = [e for e in entries if e.is_dir()]

    for i, entry in enumerate(entries):

        connector = "└── " if i == len(entries) - 1 else "├── "

        name = entry.name
        is_dir = entry.is_dir(follow_symlinks=False)

        # colored display
        display = f"{BLUE}{name}{RESET}" if is_dir else f"{GREEN}{name}{RESET}"

        lines.append(prefix + connector + display)

        # traverse unless blocked
        if is_dir and name not in BLOCKED:
            extension = "    " if i == len(entries)-1 else "│   "
            lines += build_tree(
                Path(entry.path),
                dirs_only,
                prefix + extension,
            )

    return lines


def main():

    parser = argparse.ArgumentParser(
        description="Show directory tree"
    )

    parser.add_argument(
        "--dirs-only",
        action="store_true",
        help="show only directories",
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="ask to save output",
    )

    args = parser.parse_args()

    lines = ["."]
    lines += build_tree(Path("."), dirs_only=args.dirs_only)

    output = "\n".join(lines)
    print(output)

    # ask user to save only if flag provided
    if args.save:
        choice = input("\nSave to vedant_tree.txt ? (y/n): ").lower()
        if choice == "y":
            # remove color codes before saving
            import re
            clean = re.sub(r"\033\[[0-9;]*m", "", output)

            with open("vedant_tree.txt", "w", encoding="utf-8") as f:
                f.write(clean)

            print("Saved → vedant_tree.txt")
