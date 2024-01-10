(content/authoring)=
# Authoring Content using Jupyter Book

This guide shows you how to author and preview content using Jupyter Book within your 2i2c Managed JupyterHub Service.

```{note}
A separate guide will follow describing how to deploy and publish Jupyter Book to a website. 
```

## Set up Jupyter Book

1. From your hub homepage, select the server option you require for your work and select the `Handbook Authoring` image from the dropdown selection box.

```{margin} Server options
We recommend minimal CPU resources since authoring content is not computationally intensive.
```

![server-options](./images/server-options.png)

2. Once your JupyterHub service has launched, open a `Terminal` from the launcher.

3. In the terminal, use the command

```bash
$ jupyter-book create mynewbook
```

to create a template for your Jupyter Book documentation. This creates a new folder called `mynewbook` in your home directory, which will appear in the file explorer to the left-hand side. The contents of this template folder is as follows:

```
$ tree mybookname
mybookname/
├── _config.yml
├── _toc.yml
├── intro.md
├── logo.png
├── markdown-notebooks.md
├── markdown.md
├── notebooks.ipynb
├── references.bib
└── requirements.txt
```

The `_config.yml` and `_toc.yml` files are essential to the Jupyter Book system, and we will configure each of these files in the next section.

## Edit configuration (`_config.yml`)

The `_config.yml` is a YAML configuration file for setting various options for your Jupyter Book (see [Jupyter Book docs](https://jupyterbook.org/en/stable/customize/config.html) for a definitive list of options).

For the purpose of authoring a Jupyter Book on a 2i2c Managed JupyterHub service, we can leave the default settings as they are. At the very least, you may want to change the following:

```yaml
# In _config.yml
title                       : My Community Showcase Handbook  # The title of the book. Will be placed in the left navbar.
author                      : 2i2c  # The author of the book
copyright                   : "2024"  # Copyright year to be placed in the footer
logo                        : "logo.png"  # A path to the book logo
```

```{warning}
Might want to talk about version control here, since you can specify the repo in the `_config.yml` file.
```