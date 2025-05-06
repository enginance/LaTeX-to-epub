<!-- badges -->
<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-v3-brightgreen.svg" alt="python"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="MIT license"></a> &nbsp;
</p>

<!-- content -->

# LaTeX to EPUB Converter

A simple Python script to convert LaTeX `.tex` documents into EPUB format using Pandoc, with support for BibTeX citations and bibliography management. Perfect for academic papers, e-books, and any document that requires smooth transition from LaTeX to EPUB.

## Graphical output

<p align="center">
    <img width=60% src="https://github.com/enginance/latex-to-epub/blob/main/images/sample_output.png">
</p>

## Installation

Make sure you have Python 3.6+ and [Pandoc](https://pandoc.org/installing.html) installed.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies:

```bash
pip install subprocess
pip install pathlib
