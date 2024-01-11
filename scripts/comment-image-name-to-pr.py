"""
This script is a helper script to improve the discoverability of image names and
tags pushed to a registry by our build-images workflow.

It takes the following actions:
- Establishes which PR created the changes by extracting the number from the
  head commit message
- Downloads all artifacts associcated with a previous workflow run
- Extracts the contents of each artifact and composes them into a comment body
- Posts the comment body to the PR that was merged and built the images
"""
import io
import os
import re
import sys
import json
import requests
import zipfile
from textwrap import dedent

api_url = "https://api.github.com"

# GITHUB_TOKEN = ${{ secrets.GITHUB_TOKEN }} in workflow file
token = os.environ.get("GITHUB_TOKEN", None)
if token is None:
    raise ValueError("GITHUB_TOKEN must be set!")

# WORKFLOW_RUN = ${{ github.event.workflow_run }} in workflow file
workflow_run = os.environ.get("WORKFLOW_RUN", None)
if workflow_run is None:
    raise ValueError("WORKFLOW_RUN must be set!")
workflow_run = json.loads(workflow_run)

# Set headers to send with requests
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
}

# Use regex to extract the PR number from the commit message
match = re.search("(?<=#)[0-9]*", workflow_run["head_commit"]["message"])
pr_number = None if match is None else match.group(0)

# Check if 'Merge pull request' appears in the commit message. Continue execution
# if it DOES.
if "Merge pull request" not in workflow_run["head_commit"]["message"]:
    sys.exit()

# List all artifacts for the workflow run
resp = requests.get(
    workflow_run["artifacts_url"], headers=headers, params={"per_page": 100}
)
all_artifacts = resp.json()["artifacts"]

# If "Link" is present in the response headers, that means that the results are
# paginated and we need to loop through them to collect all the results.
# It is unlikely that we will have more than 100 artifact results for a single
# worflow ID however.
while ("Link" in resp.headers.keys()) and ('rel="next"' in res.headers["Link"]
):
    next_url = re.search(r'(?<=<)([\S]*)(?=>; rel="next")', resp.headers["Link"])
    resp = requests.get(next_url.group(0), headers=headers)
    all_artifacts.extend(resp.json()["artifacts"])

# Filter for the artifact with the name we want: ending in '-image-name'
filtered_artifacts = [
    i
    for i, artifact in enumerate(all_artifacts)
    if artifact["name"].endswith("-image-name")
]

if len(filtered_artifacts) == 0:
    print(f"No artifacts found ending with '-image-name' for workflow run: {run_id}")
    sys.exit()

# Empty list to store artifact contents in
artifact_contents = []

# Download the artifacts
for artifact in filtered_artifacts:
    resp = requests.get(
        all_artifacts[artifact]["archive_download_url"],
        headers=headers,
        stream=True
    )

    # Extract the zip archive
    with zipfile.ZipFile(io.BytesIO(resp.content)) as zip_ref:
        zip_ref.extractall(os.getcwd())

    # Read in file
    with open(f"image-name.txt") as f:
        artifact_contents.append(f.read().strip("\n"))

artifact_contents = "\n- ".join(artifact_contents)

# Comment artifact content to merged PR
comment = dedent(f"""Pushed images and tags:

- {artifact_contents}""")

url = "/".join([api_url, "repos", workflow_run["repository"]["full_name"], "issues", pr_number, "comments"])
requests.post(url, headers=headers, json={"body": comment})
