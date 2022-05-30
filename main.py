from pyrogram import Client
from pyrogram import types
import time
from pyrogram import filters
import os

app = Client("channelonly_bot", api_id=8877748487, api_hash="gbfvfgbvhthfbgthbjnthjbtyhr", bot_token="rtgyt:AAHcvFPFx9u_-gfgffg--MPE") # FAKE CREDENTIALS # PUT YOUR OWN #

@app.on_message(filters.private)
async def my_handler(client, message): 
	await app.send_message(chat_id=message.from_user.id, text="This bot is meant to be used in groups. Nothing is possible through PMs.\n\n#StandWithUkraine")

@app.on_message(filters.new_chat_members)
async def my_handler2(client, message):
	user = message.new_chat_members[0] # Declare user
	warning = await app.send_message(chat_id=message.chat.id, text=user.mention() + ", this group is only here for commenting in the linked channel. You will be removed from this group (not the channel) in a few seconds. You will still be able to comment in the linked channel.") # Show warning
	await app.restrict_chat_member(chat_id=message.chat.id, user_id=user.id, permissions=types.ChatPermissions(can_send_messages=False, can_send_media_messages=False, can_send_other_messages=False, can_send_polls=False, can_add_web_page_previews=False, can_change_info=False, can_invite_users=False, can_pin_messages=False)) # Restrict user
	time.sleep(5) # Wait 5 seconds
	await app.restrict_chat_member(chat_id=message.chat.id, user_id=user.id, permissions=types.ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_send_polls=True, can_add_web_page_previews=True, can_change_info=True, can_invite_users=True, can_pin_messages=True)) # Free user
	await app.ban_chat_member(chat_id=message.chat.id, user_id=user.id) # Kick user (1/2)
	await app.unban_chat_member(chat_id=message.chat.id, user_id=user.id) # Kick user (2/2)
	await warning.delete() # Clear warning messsage
 
app.run()