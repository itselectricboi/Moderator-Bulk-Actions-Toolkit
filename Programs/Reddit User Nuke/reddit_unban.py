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
    user_name = input("Please enter the username of the user you would like to unban: ")
    user = reddit.redditor(user_name)

    subreddit.banned.remove(user)

    mmessage = input("Would you like to send this user a modmail giving a reason for unbanning?").lower
    if mmessage == "yes" or "y":
        subject = input("Please enter a subject for the modmail: ")
        body = input("What is the message you would like to send? ")
        reddit.subreddit("GamingCirclejerk").modmail.create(subject=subject, body=body, recipient=user)
    else:
        print("Cya!")
        exit()

main()