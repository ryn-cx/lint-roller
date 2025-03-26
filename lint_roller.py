import subprocess
from pathlib import Path

def extract_error_codes(input_file: Path) -> list[str]:
    """Extract error codes from markdown file."""
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
    return codes

def update_pylint_config(error_codes: list[str], config_file: Path) -> None:
    """Update pylint config file with error codes to disable."""
    disable_codes = ", ".join(error_codes)
    
    # Generate default config
    subprocess.run(
        ["uv", "run", "pylint", "--generate-rcfile"], 
        stdout=config_file.open("w"),
        check=True
    )

    # Update disable section
    lines = config_file.read_text().splitlines()
    with config_file.open("w") as f:
        for line in lines:
            if line.startswith("disable="):
                line = f"disable={disable_codes}"
            f.write(line + "\n")

def main() -> None:
    """Main function."""
    input_file = Path("input.md")
    config_file = Path(".pylintrc")
    
    error_codes = extract_error_codes(input_file)
    update_pylint_config(error_codes, config_file)

if __name__ == "__main__":
    main()
