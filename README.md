# Project Specification

This repository contains the system specification documentation.

## Prerequisites

- [uv](https://github.com/astral-sh/uv)
- Pandoc (for PDF generation)
- LaTeX (e.g., MacTeX/BasicTeX for PDF generation)

## Setup

```bash
uv sync
```

## Commands

All commands should be run from the `doc/` directory.

### Build HTML

Generates the documentation as a single HTML file.

```bash
cd doc
make singlehtml
```
Output: `doc/_build/singlehtml/index.html`

### Build PDF

Generates the documentation as a PDF file using Pandoc.

```bash
cd doc
make pdf
```
Output: `specification.pdf` (in the project root)

### Linting (Check Syntax)

Checks the reStructuredText files for syntax errors and broken links.

```bash
uv run rstcheck -r doc
```
