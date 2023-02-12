import praw

def main():

    #Initialize
    reddit = praw.Reddit(client_id='WDpM4jQf4sNq0pEbH98vkg',
    client_secret='uwCVG27Wiko3MxK6mzVsW68xQnL15g',
    username='AkatsukiAke',
    password='hxnVXVQUYnsD',
    user_agent='Moderator Action Toolkit')

    #Define Variables
    subreddit = reddit.subreddit("GamingCirclejerk")
    user_name = input("Please enter the username of the user you would like to send a modmail to: ")
    user = reddit.redditor(user_name)

    subject = input("Please enter a subject for the modmail: ")
    body = input("What is the message you would like to send? ")
    reddit.subreddit("GamingCirclejerk").modmail.create(subject=subject, body=body, recipient=user)
    
    cycle = input("Would you like to send another one? ")
    if cycle == "yes" or "y":
        main()
    else:
        print("Goodbye!")
        exit()


main()
