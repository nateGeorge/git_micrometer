# quantifies relative contributions to a github repo on a per-user basis
# uses PyGithub: https://github.com/PyGithub/PyGithub
# docs: http://pygithub.readthedocs.io/en/latest/introduction.html
# example I used to get here: https://gist.github.com/rmcgibbo/3433798

from github import Github, Repository
import os
import pandas as pd

# First create a Github instance:
g = Github("nateGeorge", os.environ['GIT_PASS'])

GITHUB_REPO_NAME = 'cstainbrook/fraud-detection-case-study'
github_user, repo_name = GITHUB_REPO_NAME.split('/')

user = g.get_user(github_user)

repo = user.get_repo(repo_name)
commits = list(repo.get_commits())

#commit = repo.get_commit(commits[0].sha)


authors = []
additions = []
for commit in commits:
    #print commit
    if commit.author is not None:
        author = commit.author.login # get's user name
        addition = commit.stats.additions # gets number of lines added)
        #print author, addition
        authors.append(author)
        additions.append(addition)

commit_df = pd.DataFrame({'author':authors, 'additions':additions})

# in this case we only care about the first few authors
ourteam = list(commit_df.author.unique()[:4])

commit_df_team = commit_df[commit_df['author'].isin(ourteam)]

total_add = commit_df_team.groupby('author').sum()

print total_add

#commit.files # can check if a code file or pdf or whatever

# if it's code, see how many lines added deleted



# as a first approximation, let's just add up number of lines added per user



# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print repo.name
    #repo.edit(has_wiki=False)
