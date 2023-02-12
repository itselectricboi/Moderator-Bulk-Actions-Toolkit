import praw

# Connect to Reddit API
reddit = praw.Reddit(client_id='WDpM4jQf4sNq0pEbH98vkg',
client_secret='uwCVG27Wiko3MxK6mzVsW68xQnL15g',
username='AkatsukiAke',
password='hxnVXVQUYnsD',
user_agent='Moderator Action Toolkit')

# Define the subreddit you want to moderate
subreddit = reddit.subreddit("subreddit_name")

# Define the user you want to remove all posts and comments from
user = reddit.redditor("username")

# Get all the comments and posts made by the user
posts_and_comments = []
for post in user.submissions.new():
    posts_and_comments.append(post)
for comment in user.comments.new():
    posts_and_comments.append(comment)

# Remove all posts and comments made by the user
for item in posts_and_comments:
    item.mod.remove()

print("All posts and comments made by the user have been removed.")