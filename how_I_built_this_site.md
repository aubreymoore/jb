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

# Initialize Local Git
```bash
git add .
git commit -m 'intitial commit'
```

# Create GitHub Repository

Create a new GitHub repo called `jb`. Then push the local repo using the commands suggested by GH:
```
git remote add origin https://github.com/aubreymoore/jb.git
git branch -M main
git push -u origin main
```

# Create a GitHub action in the local repo
```bash
jupyter-book init --gh-pages
git add .
git commit -m 'added deploy.yml'
git push
```

# GitHub Pages Configuration

Follow [these instructions](https://jupyterbook.org/stable/get-started/publish/) 

