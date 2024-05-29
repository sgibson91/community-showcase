FROM quay.io/jupyter/scipy-notebook

USER root

RUN apt-get -qq update && \
    apt-get -qq install --yes --no-install-recommends \
       gettext-base \
       less \
       unzip \
       > /dev/null && \
    apt-get -qq purge && \
    apt-get -qq clean && \
    rm -rf /var/lib/apt/lists/*

# Install from the environment.yml file
COPY --chown=${NB_UID}:${NB_GID} environment.yml /tmp/
RUN mamba env update -n base --file /tmp/environment.yml && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
