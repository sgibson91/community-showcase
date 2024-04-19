# Inherit from an upstream image
FROM quay.io/jupyter/pytorch-notebook:2024-04-19

COPY environment.yml /tmp/environment.yml

RUN mamba env update --prefix ${CONDA_DIR} --file /tmp/environment.yml
