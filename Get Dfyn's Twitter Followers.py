import tweepy
import time
import pandas as pd
import csv


# connect to tweepy
consumer_key = "" # enter the consumer key given by twitter
consumer_secret = ""  # enter the consumer secret key given by twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# the screen_name of the targeted user, in this case --> Dfyn
Dfyn_screen_name = "_DFyn"

# Below code will request for 5000 follower ids in one request and therefore will give 75K ids in every 15 minute window (as 15 requests can be made in each window)
dfyn_ids = []
for user in tweepy.Cursor(api.followers_ids, Dfyn_screen_name,count=5000).items():
    dfyn_ids.append(user)    
print(len(dfyn_ids))

# Below function could be used to make lookup requests for ids 100 at a time leading to 18K lookups in each 15 minute window
def get_usernames(userids, api):
    fullusers = []
    u_count = len(userids)
    print(u_count)
    try:
        for i in range(int(u_count/100) + 1):            
            end_loc = min((i + 1) * 100, u_count)
            fullusers.extend(
                api.lookup_users(user_ids=userids[i * 100:end_loc])              
            )
        return fullusers
    except:
        import traceback
        traceback.print_exc()
        print ('Something went wrong, quitting...')

# Calling the function below with the list of follower ids and tweepy api connection details
dfynusers = get_usernames(dfyn_ids,api)
dfynfollowers = []
for i in range(len(dfynusers)):
    dfynfollowers.append(dfynusers[i].screen_name)
column_names = ["username"]
df = pd.DataFrame((dfynfollowers), columns = column_names)
dir = "./Data/" 
df.to_csv(dir + 'Dfyn Twitter Followers.csv')