# 2i2c Community Showcase

> [!NOTE]
> This is not currently in use as we decide what kind of content should go here.
> Instead, look at [the `docs/` repository](https://github.com/2i2c-org/docs) for learning and training content.

This repo manages the images behind https://showcase.2i2c.cloud and supports Community of 2i2c Hub Champions using 2i2c infrastructure.

## About this repository :information_source:

This repository enables [jupyterhub/repo2docker-action](https://github.com/jupyterhub/repo2docker-action).
This GitHub action builds a Docker image using the contents of this repo and pushes it to the [Quay.io](https://quay.io/) registry.

### Adding a new image to this repo

All images build from this repository are stored in the `images/` directory.
To add a new image to be built, follow these steps:

1. Create a new subfolder under the `images/` directory.
   **The name of this folder will be the name your image will be given and pushed to quay.io with!**
2. Under this new subfolder, you can add any [repo2docker configuration files](https://repo2docker.readthedocs.io/en/latest/config_files.html) to describe the image you'd like to build.
   Open up a Pull Request to add these files to the repo.
3. Create a [new image repository](https://quay.io/new/?namespace=2i2c) under the 2i2c organisation on quay.io.
   The name of this repository **MUST** match the name you gave the subfolder in step 1.
   Make the repository _public_.
4. Give the [`2i2c+community_showcase_image_pusher` robot account](https://quay.io/organization/2i2c?tab=robots) **write** permissions to this new image repository.
5. When you merge the PR you created in step 2, our [GitHub Actions workflow](https://github.com/2i2c-org/community-showcase/blob/main/.github/workflows/build-images.yaml) will build your image, using repo2docker, and push it to the new image repository on quay.io
