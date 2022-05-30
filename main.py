from pyrogram import Client

# After 1st run, remove the 3 lines after this one
api_id = 123456789 # Insert API ID here
api_hash = "hgbjfdfgbv47ghfhg48fdbh45" # Insert API hash here
bot_token = "5415593491:gregggreeg-ZhY0bfS2OOaEskLd4--MPE" # Insert bot token here


app = Client("channelonly_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token) # After 1st run, remove this line
# app = Client("channelonly_bot") # Uncomment this line after 1st run


app.run()