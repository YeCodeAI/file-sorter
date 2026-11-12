# FileSorter

> A smart CLI utility to automatically organize and sort files into designated folders based on their extensions, powered by a local database. Built with Python.

## Tech Stack

* **Python 3.13**
* **uv**: — Extremely fast Python package and project manager.
* **Typer**: — For building intuitive and robust CLI applications.
* **Rich**: — For gorgeous terminal formatting, tables, and colored output.
* **TinyDB**: — Lightweight document-oriented database for storing format rules.

---

## Features

* **Format Management (`db`):** Register, view, and delete sorting rules (association between file extensions and target directories) stored securely in your home directory.
* **Smart Sorting (`sorter`):** Automatically scans a source folder, matches file extensions against your database rules, creates target directories if they don't exist, and moves files safely using `shutil`.
* **Rich UI/UX:** Clean status logs, warning alerts, and beautifully formatted tables displaying all registered formats.

---

##  Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/YeCodeAI/file-sorter.git](https://github.com/YeCodeAI/file-sorter.git)
cd file-sorter
```
2. **Install CLI with uv**:
```bash
uv tool install .
```

## Usage

1. **Check all formats**
```bash
file-sorter db get-all
```

2. **Add new format**
```bash
file-sorter db add -f <FORMAT> -p <PATH>
```

3. **Remove format**
```bash
file-sorter db remove -n <NAME_FORMAT>
```

4. **Sort files**
```bash
file-sorter sorter -o <OUTPUT_DIR>
```