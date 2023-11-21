FROM jupyter/minimal-notebook

RUN mamba install --yes jupyterlab=3 \
    numpy matplotlib jupyter-book jupyterlab-git 

RUN npm install -g mystmd && \
    pip install jupyterlab_myst && \
    pip install jupyter-server-proxy

