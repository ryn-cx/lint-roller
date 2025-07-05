from pathlib import Path


def main() -> None:
    """Main function."""
    input_file = Path("input.md")

    text = input_file.read_text()
    codes: list[str] = []
    for section in text.split("["):
        if not section.startswith("x"):
            continue
        try:
            # Get text between second set of backticks
            codes.append(section.split("`")[3])
        except IndexError:
            continue

    disable_codes = ", ".join(codes)
    Path("rules.md").write_text(disable_codes)


if __name__ == "__main__":
    main()
