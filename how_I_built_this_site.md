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

Edit myst.yml and autogenerate a table of contents using:
```bash
jupyter-book init --write-toc
```

# Iniitialize Local Git
```bash
git add .
git commit -m 'intitial commit'
```

# GitHub Pages Configuration

