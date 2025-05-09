<!-- badges -->
<p align="center">
    <a href="https://github.com/enginance/LaTeX-to-epub/stargazers">
        <img src="https://img.shields.io/github/stars/enginance/LaTeX-to-epub?style=social" alt="Stars"></a> &nbsp;
    <a href="https://github.com/enginance/LaTeX-to-epub/commits/main">
        <img src="https://img.shields.io/github/last-commit/enginance/LaTeX-to-epub?style=flat" alt="Last Commit"></a> &nbsp;
    <a href="https://github.com/enginance/LaTeX-to-epub/issues">
        <img src="https://img.shields.io/github/issues/enginance/LaTeX-to-epub" alt="Open Issues"></a> &nbsp;
    <a href="https://github.com/enginance/LaTeX-to-epub/network/members">
        <img src="https://img.shields.io/github/forks/enginance/LaTeX-to-epub" alt="Forks"></a> &nbsp;
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-v3-brightgreen.svg" alt="python"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="MIT license"></a> &nbsp;
    <a href="https://www.pandoc.org/">
        <img src="https://img.shields.io/badge/Pandoc-%3E%3D%202.11-blue" alt="Pandoc version"></a> &nbsp;
</p>

<!-- content -->

# LaTeX to EPUB Converter

A **simple and efficient Python script** that converts LaTeX `.tex` documents into EPUB format, leveraging the power of [Pandoc](https://pandoc.org/). This tool is ideal for authors, researchers, and anyone looking to publish LaTeX-based content as an EPUB eBook. It fully supports bibliography and citation management using BibTeX, along with enhanced handling of formulas, figures, and other LaTeX-specific elements.

## Key Features

- ✅ **Automatic LaTeX to EPUB conversion** using [Pandoc](https://pandoc.org/).
- 📚 **Full support for BibTeX citations and bibliography** using the `--citeproc` option.
- 🚀 **Simple and easy to use**: Just define input/output files and run the script.
- 🖥 **Works for academic papers, research articles, e-books, and any LaTeX-based documents**.
- ⚙️ **Minimal Python dependencies**: Only requires `subprocess`, `pathlib`, and `os` (all are part of the standard library).
- 📑 **Metadata Generation**: Automatically generates a basic EPUB metadata file if not present.
- 🧮 **Formula Handling**: Converts LaTeX math formulas into MathML for better EPUB compatibility.
- 🖼️ **Figure Conversion**: Handles LaTeX figures (e.g., `\includegraphics`), ensuring they are properly included in the EPUB file.
- 💡 **Customizable**: Allows you to adjust paths for the LaTeX source, target EPUB, bibliography, and metadata.

## Installation

To get started with this script, you need to ensure that both **Pandoc** and Python dependencies are properly installed on your system.

### Step 1: Install Pandoc

**Pandoc** is required for the actual conversion process. You can install it by following the instructions on the official [Pandoc installation page](https://pandoc.org/installing.html).

For example, if you're on a Linux-based system (e.g., Ubuntu), you can use the following command:

```bash
sudo apt-get install pandoc
````

For **macOS**, you can install Pandoc via Homebrew:

```bash
brew install pandoc
```

For **Windows**, you can download the Pandoc installer from the [Pandoc download page](https://pandoc.org/installing.html).

### Step 2: Install Python Dependencies

The script uses Python 3, and it requires a few basic modules which are part of the Python standard library. However, if you're using other modules (like `subprocess`), here’s how to install them using `pip`:

```bash
pip install subprocess pathlib
```

These dependencies should be installed automatically as they're part of Python's built-in libraries, but you can install them explicitly if needed.

### Step 3: Install Lua Filter (Optional)

For enhanced formula handling, you can optionally use a Lua filter. This step is not required but is recommended if you have complex math formulas in your LaTeX file.

1. Download the Lua filter from [this link](https://raw.githubusercontent.com/jgm/pandoc-lua-filters/master/latex-to-unicode/latex-to-unicode.lua).
2. Place the downloaded `latex-to-unicode.lua` file in the same directory as the script.

### Step 4: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/enginance/LaTeX-to-epub.git
```

### Step 5: Modify the Script's File Paths

Before running the script, you need to set the correct file paths for the LaTeX source, output EPUB, bibliography (optional), and metadata (optional) files. You can modify these paths directly in the **`latex_to_epub.py`** script.

Here's how you can set the file paths:

1. **`SOURCE_FILE`**: Set this to the path of your LaTeX `.tex` document.
2. **`TARGET_FILE`**: Set this to the desired output path for your EPUB file.
3. **`BIBLIOGRAPHY_FILE`**: Set this to the path of your BibTeX `.bib` file (optional).
4. **`METADATA_FILE`**: Set this to the path of your EPUB metadata file (optional).

For example, inside the script, you will modify these lines:

```python
SOURCE_FILE = "your_document.tex"          # 📝 Input LaTeX file
TARGET_FILE = "your_ebook.epub"            # 📂 Output EPUB file
BIBLIOGRAPHY_FILE = "references.bib"       # 📚 Bibliography file (or None)
METADATA_FILE = "metadata.xml"             # 📄 EPUB metadata file
```

### Run the Script

Once you've configured your file paths, you can convert your LaTeX document to EPUB with a simple command.

```bash
python latex_to_epub.py
```

The script will:

1. Validate the LaTeX input file.
2. Generate a table of contents for the EPUB.
3. Convert LaTeX math formulas into MathML for EPUB compatibility.
4. Handle LaTeX figures and bibliography.
5. Produce an EPUB file at the specified output path.

### Example Output

Upon running the script, you will see a log like the following in the terminal:

```
╔══════════════════════════════════════════════════╗
║  LaTeX to EPUB Conversion Process Started       ║
╚══════════════════════════════════════════════════╝

[SECTION 1] Input File Validation
✅ Source file found: 00 Main Holdings.tex

[SECTION 2] Constructing Pandoc Command
   Base Pandoc command: pandoc -s 00 Main Holdings.tex ...

[SECTION 3] Handling Bibliography
   Bibliography file provided.  Enabling citation processing...

[SECTION 4] Handling Figures and Formulas
   Figures: Pandoc will attempt to convert figures using \includegraphics.
            Complex figures may require manual adjustment.
   Formulas: Converting LaTeX formulas to MathML for better EPUB compatibility.

[SECTION 5] Handling Lua Filter
   Lua filter 'latex-to-unicode.lua' not found.  Continuing without it.
   Download the filter from https://raw.githubusercontent.com/jgm/pandoc-lua-filters/master/latex-to-unicode/latex-to-unicode.lua
   and place it in the same directory as this script for improved formula conversion.

[SECTION 6] Executing Pandoc Conversion
   Full Pandoc command: pandoc -s 00 Main Holdings.tex -o your_ebook.epub --to epub --toc --number-sections --epub-metadata metadata.xml --wrap=preserve --mathml
✅ Conversion complete: your_ebook.epub

╚══════════════════════════════════════════════════╝
║  LaTeX to EPUB Conversion Process Finished        ║
╚══════════════════════════════════════════════════╝
```

## Configuration Options

### Source File

* **`SOURCE_FILE`**: Path to the LaTeX `.tex` file to be converted.

### Output File

* **`TARGET_FILE`**: Path where the converted EPUB file will be saved.

### Bibliography File (Optional)

* **`BIBLIOGRAPHY_FILE`**: Path to the `.bib` file if you're using BibTeX citations.

### Metadata File (Optional)

* **`METADATA_FILE`**: Path to the EPUB metadata XML file. If it doesn't exist, the script will create a basic one.

### Lua Filter (Optional)

* **`latex-to-unicode.lua`**: Optional Lua filter that improves Unicode math handling. You can download it from the provided link and place it in the


same directory as the script.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Enjoy converting your LaTeX documents to EPUB with ease!**

```
