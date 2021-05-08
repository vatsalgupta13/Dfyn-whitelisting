# Dfyn-whitelisting

Packages used:
1) csv
2) pandas
3) numpy
4) tweepy
5) web3
6) json
7) telethon


Steps to follow:
1) Run Level 0 Filtering.py directly on Dfyn Whitelist Form 1 Responses.csv
2) Do Level 1 filtering using MS Excel. Link to the medium article: 
3) Before Level 2 filtering, run Get Dfyn's Twitter Followers.py and Get Dfyn's Telegram Members.py files.
4) You will need to request for a twitter developer account to get your own access keys to run the code. Steps required to get access key from twitter are listed here:
https://towardsdatascience.com/how-to-access-twitters-api-using-tweepy-5a13a206683b#:~:text=Step%203%3A%20Get%20your%20authentication,token%20and%20access%20token%20secret
5) Similarly you need to get access keys from telegram. Follow the steps given here: https://telethonn.readthedocs.io/en/latest/extra/basic/creating-a-client.html.
6) After getting your api keys, add them to the code and run both the codes to get Dfyn's telegram group memebers and twitter followers.
7) Run Level 2 Filtering.py to get the filter out all the candidates that do not follow Dfyn on twitter or are not part of Dfyn's telegram group.

Important Notes
1) Kindly change the dir (directory) variable. Set it to wherever your csv files are kept.
2) Datasets relevant to the code have been added to the repository itself. You can view the entire data at:
https://docs.google.com/spreadsheets/d/11wJB4-ycHqOrA28pbaxhL-ZuXc4SFE2zdHDGrkjcjto/edit#gid=1748858189
3) Sensitive information of the users have been omitted from both - the spreadsheet and the repository itself. The code has references to some columns which are no longer present in the data. Kindly remove all such references before running the code. You will still be able to perform Level 0 and Level 1 screening, but Level 2 screening won't be possible. 
