"""
This script expects a comma delimited string as an input that describes a list
of files that will be added or modified by a git operation. It will manipulate
this string to find the unique folders these files belong to, and create a list
of dictionaries where the key name of each dict is 'image-name' and the values
are one of the unique folder names in turn. This will form a matrix job
definition for GitHub Actions.
"""
import os
import json
import typer
from pathlib import Path

REPO_ROOT_PATH = Path(__file__).parent.parent


def main(changed_filepaths: str):
    # Split the CSV string into a list
    changed_filepaths = changed_filepaths.split(",")

    # Convert changed filepaths into absolute Posix Paths
    changed_filepaths = [
        REPO_ROOT_PATH.joinpath(filepath) for filepath in changed_filepaths
    ]

    # Find the parent folder of each filepath in changed filepaths
    changed_filepaths = [
        path.parent for path in changed_filepaths
    ]

    # Ensure this list only contains unique elements by calling set() upon it
    changed_filepaths = set(changed_filepaths)

    # Construct a list of dicts detailing the subfolders, and hence images,
    # to be built
    matrix_jobs = [
        {"image-name": path.parts[-1]}
        for path in changed_filepaths
    ]

    # The existence of the CI environment variable is an indication that we are
    # running in an GitHub Actions workflow
    # https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#example-defining-outputs-for-a-job
    # This will avoid errors trying to set CI output variables in an environment
    # that doesn't exist.
    ci_env = os.environ.get("CI", False)
    # We share variables between steps/jobs by writing them to GITHUB_ENV
    # More info on GITHUB_ENV: https://docs.github.com/en/actions/learn-github-actions/environment-variables
    env_file = os.getenv("GITHUB_ENV")

    if ci_env:
        # Add matrix job as output for use in another job
        with open(env_file, "a") as f:
            f.write(f"images-to-build={json.dumps(matrix_jobs)}")
            f.write("\n")


if __name__ == "__main__":
    typer.run(main)
