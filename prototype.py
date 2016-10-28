from github import Github, Repository
import os

# First create a Github instance:
g = Github("nateGeorge", os.environ['GIT_PASS'])

GITHUB_REPO_NAME = 'cstainbrook/fraud-detection-case-study'
github_user, repo_name = GITHUB_REPO_NAME.split('/')

user = g.get_user(github_user)

repo = user.get_repo(repo_name)
commits = list(repo.get_commits())

commit = repo.get_commit(commits[0].sha)

commit.author.login # get's user name

commit.files # can check if a code file or pdf or whatever

# if it's code, see how many lines added deleted

commit.stats.additions # gets number of lines added

# as a first approximation, let's just add up number of lines added per user



# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print repo.name
    #repo.edit(has_wiki=False)
