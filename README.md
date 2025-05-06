<!-- badges -->
<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-v3-brightgreen.svg" alt="python"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="MIT license"></a> &nbsp;
</p>

<!-- content -->

# LaTeX to EPUB Converter

A simple and efficient Python script that converts LaTeX `.tex` documents into EPUB format, leveraging the power of [Pandoc](https://pandoc.org/). This tool supports seamless conversion of academic papers, e-books, and any LaTeX document with full bibliography and citation management using BibTeX. It's perfect for authors, researchers, and anyone looking to publish LaTeX-based content as an EPUB.

LaTeX is a popular typesetting system used for creating documents with complex mathematical formulas, academic papers, and technical documentation. However, when it comes to distributing LaTeX content digitally, converting it into a universally readable format like EPUB can be challenging. This script streamlines the process and ensures that citations and bibliographies are handled properly during conversion.

## Features

- ✅ **Automatic LaTeX to EPUB conversion** using Pandoc.
- 📚 **Full support for BibTeX citations and bibliography** using `--citeproc`.
- 🚀 Easy to use: Just define input/output files and run the script.
- 🖥 Works for academic papers, research articles, e-books, and any LaTeX-based documents.
- ⚙️ Simple Python script with minimal dependencies.

## Installation

Ensure you have **Python 3.6+** and [Pandoc](https://pandoc.org/installing.html) installed on your system.

### Install Python dependencies

Use [pip](https://pip.pypa.io/en/stable/) to install the required packages:

```bash
pip install subprocess
pip install pathlib
