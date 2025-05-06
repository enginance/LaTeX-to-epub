#!/usr/bin/env python3
# ╔════════════════════════════════════════════════════════════╗
# ║    LaTeX to EPUB Converter using Pandoc + Python          ║
# ║    Author: enginance                                      ║
# ║    Description: Converts a LaTeX file to EPUB using       ║
# ║    Pandoc with bibliography and citation processing.      ║
# ║    Notes:                                                 ║
# ║     - Requires Pandoc ≥ 2.11                              ║
# ║     - Make sure all \input or \include files exist       ║
# ║     - Figures and complex tables may need manual cleanup ║
# ╚════════════════════════════════════════════════════════════╝

import subprocess
import sys
from pathlib import Path

def convert_latex_to_epub(source_file: str, target_file: str, bibliography_file: str):
    """
    Converts a LaTeX source file to an EPUB using Pandoc.
    
    Args:
        source_file (str): Path to the LaTeX (.tex) file.
        target_file (str): Desired output EPUB file.
        bibliography_file (str): Path to the BibTeX (.bib) file.
    """

    # Check if source and bibliography files exist
    if not Path(source_file).is_file():
        print(f"❌ Error: Source file not found: {source_file}", file=sys.stderr)
        sys.exit(1)

    if not Path(bibliography_file).is_file():
        print(f"❌ Error: Bibliography file not found: {bibliography_file}", file=sys.stderr)
        sys.exit(1)

    # Construct the Pandoc command
    command = [
        "pandoc",
        "--bibliography", bibliography_file,
        "--citeproc",                    # Use Pandoc's built-in citation processor
        "-s", source_file,               # Standalone output
        "-o", target_file,               # Output file
        "--metadata", "link-citations=true",
        "--metadata", "link-bibliography=true"
    ]

    # Show the command being run (like `set -x` in Bash)
    print(f"🔧 Running command: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
        print(f"✅ Conversion complete: {target_file}")
    except subprocess.CalledProcessError as e:
        print("❌ Pandoc conversion failed.", file=sys.stderr)
        sys.exit(e.returncode)

if __name__ == "__main__":
    # ╔════════════════════════════════════════════════════════════╗
    # ║    🚨 USER INPUT AREA: Define your input/output filenames  ║
    # ║    Adjust the values below to match your files.            ║
    # ╚════════════════════════════════════════════════════════════╝

    SOURCE_FILE = "your_latex_document.tex"          # 📝 Input LaTeX file (change to your file)
    TARGET_FILE = "your_new_output.epub"             # 📂 Output EPUB file (change as needed)
    BIBLIOGRAPHY_FILE = "your_bibliography.bib"      # 📚 Bibliography file (change to your .bib file)

    convert_latex_to_epub(SOURCE_FILE, TARGET_FILE, BIBLIOGRAPHY_FILE)
