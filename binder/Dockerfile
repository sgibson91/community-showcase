FROM jupyter/minimal-notebook

RUN mamba install --yes jupyterlab=3

RUN npm install -g mystmd && \
    pip install jupyterlab_myst
