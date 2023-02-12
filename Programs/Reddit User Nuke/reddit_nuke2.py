import praw

reddit = praw.Reddit(client_id='WDpM4jQf4sNq0pEbH98vkg',
client_secret='uwCVG27Wiko3MxK6mzVsW68xQnL15g',
username='AkatsukiAke',
password='hxnVXVQUYnsD',
user_agent='Moderator Action Toolkit')

subreddit_name=input("Enter the name of the subreddit that you want to remove the user's comments and posts from: ")
user = reddit.subreddit(subreddit_name)

user_name = input("Enter the username of the user whose comments and posts you want to remove: ")
user = reddit.redditor(user_name)

for comment in user.comments.new(limit=None):
    if comment.subreddit.display_name==subreddit_name:comment.mod.remove()

for submission in subreddit_name.submissions(start=0, end=None):
    if submission.author==user.name:submission.mod.remove()

print(f"All comments and posts from u/{user_name} have been removed from r/{subreddit_name}.") 
