import os
import sys
import base64

import github3

APP = "documentation/content/application"
COMMON = "documentation/content/application"
MAIN_BRANCH = 'master'
user = os.environ['GITHUB_USER']
repos = ['test1', 'test2']

token = id = ''
# run get-creds.py first
with open('ghcreds', 'r') as fd:
    token = fd.readline().strip()
    id = fd.readline().strip()

github = github3.login(token=token)
for repo_name in repos:
    readme_path = APP + "/aws/" + repo_name + "/README.md"
    repo_dir = os.path.dirname(readme_path)
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)
    repository = github.repository(user, repo_name)
    repo_readme = repository.file_contents('/README.md', ref=MAIN_BRANCH)
    with open(readme_path, "w") as f:
        base64_bytes = repo_readme.content.encode('ascii')
        readme_bytes = base64.b64decode(base64_bytes)
        readme = readme_bytes.decode('ascii')
        f.write(readme.encode('utf-8'))
