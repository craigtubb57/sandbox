import os
import sys
import base64

import github3

APP = "documentation/content/application"
COMMON = "documentation/content/application"
MAIN_BRANCH = 'master'
user = os.environ['GITHUB_REPOSITORY'].split('/')[0]
token = os.environ['GITHUB_TOKEN']
repos = ['test1', 'test2']

github = github3.login(token=token)
# org = github3.organization(name)
# repos = org.repositories()
# owner = repos[i].owner()
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
        title_i = readme.find('# ') + 2
        title_end_i = readme.find('\n', title_i)
        title_end_i = title_end_i if title_end_i != -1 else len(readme)
        print("{}: {}".format("TITLE INDEX", title_i))
        print("{}: {}".format("TITLE END INDEX", title_end_i))
        title = readme[title_i:title_end_i]
        front_title = "\ntitle: \"" + title + "\""
        front_url = "\nurl: \"" + repo_name + "\""
        front_matter = [
            "---",
            front_title,
            front_url,
            "\n---"
        ]
        readme = "".join(front_matter) + readme[title_end_i:len(readme)]
        f.write(readme.encode('utf-8'))
