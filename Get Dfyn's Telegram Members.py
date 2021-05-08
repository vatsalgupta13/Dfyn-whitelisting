import csv
import pandas as pd


# get all members from telegram's group and save them in a csv file
def getTelegramGroupMembers():

    from telethon.sync import TelegramClient
    api_id = 0000000 # replace with your 7 digit api_id
    api_hash = '' # enter your api hash
    phone = '' # enter your phone number with international code
    client = TelegramClient(phone, api_id, api_hash)


    client.connect()  # a code will be sent to your telegram account
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))


    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
 
    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)


    for chat in chats:
        try:
            if chat.megagroup== True:
                groups.append(chat)
        except:
            continue


    print('Choose a group to scrape members from:') # will show you all the groups that you are listed in
    i=0
    for g in groups:
        print(str(i) + '- ' + g.title)
        i+=1

    g_index = input("Enter a Number: ") # choose the number correspoding to Dfyn_HQ telegram group
    target_group=groups[int(g_index)]

    print('Fetching Members...')
    all_participants = []
    all_participants = client.get_participants(target_group, aggressive=True)
    print(all_participants)

    print('Saving In file...')
    csv_file_directory = "./Data/Telegram Members.csv"
    with open(csv_file_directory,"w+",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
        for user in all_participants:
            if user.username:
                username= user.username
            else:
                username= ""
            if user.first_name:
                first_name= user.first_name
            else:
                first_name= ""
            if user.last_name:
                last_name= user.last_name
            else:
                last_name= ""
            name= (first_name + ' ' + last_name).strip()
            writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
    print('Members scraped successfully.')

def main():
    # get telegram group members and save it to a CSV file
    getTelegramGroupMembers() 

if __name__ == "__main__":
    main()
    

# this code has been sourced from https://python.gotrained.com/scraping-telegram-group-members-python-telethon/