from github import Github as G

g = G("")#was unable to generate my access token of github

org1=input()#org1 is the name of orhganization whose repo need to be extracted
org = g.get_organization(org1)

# this small n is the no of top repos
n = int(input())
# this small is the number of oldest forks
m = int(input())

# Get all repositories of the organization
repos = org.get_repos()

# Sorted the repositories based on the number of forks
repossorted = sorted(repos, key=lambda repo: repo.forks_count, reverse=True)

# we selected the n most popular repositories based on the number of forks using this sort method of list class  sorting the lost of repos
mostpopularrepos = repossorted[:n]


for repo in mostpopularrepos:
    forks = repo.get_forks()
    forkss = sorted(forks, key=lambda fork: fork.created_at)
    oldestforks = forkss[:m]

#Unable to design the full backened code for the app so designed the frontend 
