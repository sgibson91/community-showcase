FROM jupyter/minimal-notebook

RUN mamba install --yes jupyterlab=3 \
    numpy matplotlib

RUN npm install -g mystmd && \
    pip install jupyterlab_myst
