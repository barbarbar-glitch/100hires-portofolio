from pathlib import Path
import sys


def print_tree(root: Path) -> int:
    if not root.exists():
        print(f"Path not found: {root}")
        return 1

    print(root)
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        depth = len(relative.parts)
        indent = "  " * depth
        suffix = "/" if path.is_dir() else ""
        print(f"{indent}{path.name}{suffix}")
    return 0


def main() -> int:
    target = Path("research/linkedin-posts")
    return print_tree(target)


if __name__ == "__main__":
    raise SystemExit(main())
