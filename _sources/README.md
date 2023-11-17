# 2i2c Community Showcase Handbook

This JupyterBook showcases what is possible with a 2i2c managed JupyterHub for advancing Open Science.

## Usage

### Building the book

If you'd like to develop and/or build the Introduction to 2i2c book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. (Optional) Edit the books source files located in the `introduction_to_2i2c/` directory
4. Run `jupyter-book clean introduction_to_2i2c/` to remove any existing builds
5. Run `jupyter-book build introduction_to_2i2c/`

A fully-rendered HTML version of the book will be built in `introduction_to_2i2c/_build/html/`.

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
