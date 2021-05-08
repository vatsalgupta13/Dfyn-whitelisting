import tweepy
import csv
import pandas as pd
import numpy as np


# connect to twitter api
def connectTweepy():
    consumer_key = ""  # enter the consumer key given by twitter
    consumer_secret = "" # enter the consumer secret key given by twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    global api
    api = tweepy.API(auth, wait_on_rate_limit=True)



def main():
    connectTweepy() # connect to tweepy's twitter API
    dir = './Data/' # change this to the directory where the data is kept
    df = pd.read_csv(dir + 'Level 1 Filtered Applications.csv')
    telegramGroup = pd.read_csv(dir + 'Telegram Members.csv', usecols=["username"])
    telegram_usernames = telegramGroup.username.tolist() # complete list of our telegram group members on May 4th 3:00 GMT
    telegram_usernames.remove(np.nan) # removing entries without username
    dfynFollow = pd.read_csv(dir + 'Dfyn Twitter Followers.csv', usecols=["username"])
    dfyn_followers = dfynFollow.username.tolist() # complete list of Dfyn twitter followers on May 4th 3:00 GMT
    following_Dfyn = [] # to save all level 1 filtered applicants following Dfyn on twitter
    telegram_Member = [] # to save all level 1 filtered applicants who are members of Dfyn's telegram group
    submission_date = []
    first_name = [] 
    last_name = []
    twitter_username = []
    tg_username = []
    email = []
    country= []
    erc20_address = []
    for ind in df.index:
        user_screen_name = df['Twitter username'][ind]  # applicant's twitter username
        
        # since many applicants submitted their twitter urls or their username with @, we needed to get the user's actual screen name
        if('@' in user_screen_name):
            user_screen_name = user_screen_name.replace('@','')
        if('://' in user_screen_name):
            user_screen_name = user_screen_name.rsplit('/',1)[1]
            if('?' in user_screen_name):
                user_screen_name = user_screen_name.split('?',1)[0]
        
                
        user_telegram_handle = df['Telegram username'][ind]  # applicant's telegram handle
        
        # same reason as above
        if('@' in user_telegram_handle):
            user_telegram_handle = user_telegram_handle.replace('@','')
        if('://' in user_telegram_handle):
            user_telegram_handle = user_telegram_handle.rsplit('/',1)[1]
        print('Final telegram handle: ' + user_telegram_handle)


        # check if user is following Dfyn
        is_following_Dfyn = False # default value
        if user_screen_name in dfyn_followers:      
            is_following_Dfyn = True
        following_Dfyn.append(is_following_Dfyn)


        # check if user is in Dfyn's telegram main group
        is_telegram_member = False # default value
        if user_telegram_handle in telegram_usernames:
            is_telegram_member = True
        telegram_Member.append(is_telegram_member)

        # if both conditions are satisfied
        if(is_following_Dfyn and is_telegram_member):
            submission_date.append(df['Submission Date'][ind])
            first_name.append(df['First Name'][ind])
            last_name.append(df['Last Name'][ind])
            twitter_username.append(df['Twitter username'][ind])
            tg_username.append(df['Telegram username'][ind])
            email.append(df['Email'][ind])
            erc20_address.append(df['ERC20 Wallet Address'][ind])
            country.append(df['Country'][ind])


    column_names = ["Submission Date", "First Name","Last Name", "Email", "Twitter username","Telegram username", "ERC20 Wallet Address", "Country"]
    df2 = pd.DataFrame(list(zip(submission_date,first_name,last_name,email,tg_username,twitter_username,erc20_address, country)), columns = column_names) 
    df2.to_csv(dir + 'Level 2 Filtered Applications.csv')



if __name__ == "__main__":
    main()