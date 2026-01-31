---
title: How I built this site
subject: technical note
date: 2026-01-01
authors:
  - name: Aubrey Moore
# exports:
#   - format: pdf
#     template: arxiv_two_column
#     output: exports/relationship_between_wind_and_CRB_trap_catch.pdf
---

# Installing Jupyter Book

I used the [Jupyter Book - Getting Started docs](https://jupyterbook.org/stable/get-started/) as a reference.

```bash
cd ~/Desktop
uv init jb
cd jb
uv venv
source .venv/bin/activate
uv add jupyter-book
jupyter-book init
```

Now, open the ~/Desktop/jb folder with the VS Code test editor.
```bash
code .
```

Edit myst.yml as needed and autogenerate a table of contents using:
```bash
jupyter-book init --write-toc
```

# Initialize Local Git
```bash
git add .
git commit -m 'intitial commit'
```

# Create GitHub Repository

Create a new GitHub repo called `jb` and enable GitHub pages.  
The 'Build and Deployment' source should be `GitHub Actions` and the git branch should be `main`.

Then push the local repo using the commands suggested by GH:
```
git remote add origin https://github.com/aubreymoore/jb.git
git branch -M main
git push -u origin main
```

Create a GitHub action in the local repo and push it to GH:
```bash
jupyter-book init --gh-pages
git add .
git commit -m 'added deploy.yml'
git push
```

# Adding Sphinx documentation

[use uv to enable automatic python code documentation using sphinx](https://share.google/aimode/wMmU4zbsdFmHQscsh)

[Find me an example of a github repository template which contains a simple python package with tests and automated documentation provided by Sphinx.](https://share.google/aimode/9iSPyS6hDBkck4Sli)

## [example-sphinx-basic](https://www.google.com/url?sa=i&source=web&rct=j&url=https://github.com/readthedocs-examples/example-sphinx-basic&opi=89978449&psig=AOvVaw0BpRGYcUtnluTiu5q0z7vH&ust=1768976372873000)

- Example: Basic Sphinx project for Read the Docs: This template, provided by Read the Docs, is a straightforward example that includes a basic Sphinx project in the docs/ folder and an example Python module (lumache.py). It demonstrates how Sphinx can automatically scan and generate API documentation from docstrings using autodoc and autosummary directives, which is ideal for a simple setup.

## [palmoreck/example-python-package-and-sphinx-doc](https://www.google.com/url?sa=i&source=web&rct=j&url=https://github.com/palmoreck/example-python-package-and-sphinx-doc&opi=89978449&psig=AOvVaw0BpRGYcUtnluTiu5q0z7vH&ust=1768976372873000) 

- This repository specifically shows how to set up Sphinx documentation for a Python 3 package and publish it using GitHub Pages via GitHub Actions. The README provides clear, actionable steps for forking and deploying the documentation.

## [docathon/sphinx-template](https://www.google.com/url?sa=i&source=web&rct=j&url=https://github.com/docathon/sphinx-template&opi=89978449&psig=AOvVaw0BpRGYcUtnluTiu5q0z7vH&ust=1768976372873000)

- This is a robust template for a fully-functioning Sphinx deployment. It includes a structured layout with a docs/ directory for the Sphinx source and an example Python package (my_package/) from which docstrings are used to generate documentation.

## [AlexIoannides/py-package-template](https://www.google.com/url?sa=i&source=web&rct=j&url=https://github.com/AlexIoannides/py-package-template&opi=89978449&psig=AOvVaw0BpRGYcUtnluTiu5q0z7vH&ust=1768976372873000)

- This template provides a comprehensive skeleton for a new Python project, including testing with PyTest, Sphinx documentation generation (HTML and PDF), and automated testing/deployment using Travis CI. It's a great option for a more feature-complete project structure
- contains tests
- outdated??
