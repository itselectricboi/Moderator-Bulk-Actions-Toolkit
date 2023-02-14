import praw

print("\nWelcome to the Reddit User Comments and Post Nuke Tool!\n")

def main():

    # Initialize Reddit instance
    reddit = praw.Reddit(client_id='WDpM4jQf4sNq0pEbH98vkg',
    client_secret='uwCVG27Wiko3MxK6mzVsW68xQnL15g',
    username='AkatsukiAke',
    password='hxnVXVQUYnsD',
    user_agent='Moderator Action Toolkit')

    # Define the subreddit
    subreddit = reddit.subreddit("GamingCirclejerk")

    # Define the user
    #user = ["Mons00n_909", "New_Inspection619", "JimmyOmega111","LMayhem","SilverMoxxi","Chinnpoo","6sbeepboop","FitzyFarseer","Main-Reach-5325"]
    user_name = input("Enter the username of the user whose comments and posts you want to remove: ")
    user = reddit.redditor(user_name)


    # Get the user's posts and comments
    posts = user.submissions.new(limit=None)
    comments = user.comments.new(limit=None)

    # Loop through all the posts and remove them
    for post in posts:
        if post.subreddit == subreddit:
            post.mod.remove()

    # Loop through all the comments and remove them
    for comment in comments:
        if comment.subreddit == subreddit:
            comment.mod.remove()

    subreddit.banned.add(user, ban_message=" ", ban_duration=None, ban_note=" ")

    print(f"\nAll comments and posts from u/{user} have been removed from r/{subreddit} and the user has been.\n") 

    #Use this block if you wish for it to ask everytime you execute the command
    #cycle = input("Would you like to ban another user? ").lower
    #if cycle == "yes" or "y":
    #    main()
    #else:
    #    print("Goodbye!")
    #    exit()
    main()

main ()        
