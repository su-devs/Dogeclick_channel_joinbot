import asyncio
import logging
import re
import time
import os
import sys
import requests
from time import sleep
logging.basicConfig(level=logging.ERROR)
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.errors.rpcerrorlist import UsernameInvalidError, UsernameNotOccupiedError, UsernameInvalidError, FloodWaitError, YouBlockedUserError
from datetime import datetime
import colorama
import random
from colorama import Fore,Back,Style
from bs4 import BeautifulSoup
#colors using colorama
colorama.init(autoreset=True)
green = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
carol = Style.RESET_ALL
white = Style.RESET_ALL+Style.BRIGHT+Fore.WHITE
magenta = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
blue = Style.RESET_ALL+Style.BRIGHT+Fore.BLUE
os.system('cls' if os.name=='nt' else 'clear')
cols = [green,blue,yellow,magenta,red,white]
logo_a = (green+'''                         z$b
                .e$$$b.  $$$F  .d$$be
            .d$$$$$$$$$$e$$$be$$$$$$$$$$e.
        .e$$$$$$$$$$$ '''+red+'''g1ng3rb1t3'''+green+''' $$$$$$$$$$b.
      z$$$$$$$P**""**$$$$$$$$$$$P*""""***$$$$$b.
    z$$$$*"            "$$$$$$"            "*$$$$c
  z$$*"                 ^$$$$                  "*$$.
 ^"                      $$$F                      ^%
                         $$$b
                         $P*$
                        4P  *r
                        4    %''')
logo_b =('''
:=====================================================:
|Script version: 1.0		       	by g1ng3rb1t3 |
|======================multibot=======================|
|      Github: https://www.github.com/g1ng3rb1t3      |
:======================Channels=======================:
''')
try:
	print(logo_a)
	print(f'{random.choice(cols)}{logo_b}')
	#print(f'{random.choice(cols)}{random.choice(logos)}')
	def _time(message):
		print( f'{blue}[{yellow}{datetime.now().strftime("%I:%M:%S,%p")}{blue}] {carol}{message}')
	# Get your own values from my.telegram.org
	api_id = 800812
	api_hash = 'db55ad67a98df35667ca788b97f771f5'
	option = ["Dogecoin_click_bot", "Litecoin_click_bot", "BCH_clickbot", "Zcash_click_bot", "Bitcoinclick_bot"] #Bot option list
	# Print bot options list with numberings
	for number, letter in enumerate(option):
	    print(f'{blue}[{yellow}{number}{blue}] {white}{letter}')
	# Ask user to select bot
	print("")
	ask = int(input(f'{blue}[{yellow}+{blue}] {white}Choose a bot>>> {green}'))
	answer = (option[ask])
	url_channel = answer
	
	
	def get_response(url, method='GET'):
		response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=15)
		text_response = response.text
		status_code = response.status_code
		return[status_code, text_response]
			
	async def main():
		print("")
		print(f'{blue}[{yellow}+{blue}] {white}Openning {green}@{url_channel}\n')
		# Bot options
		action = ["Join"] #Bot option list
		# Print bot options list with numberings
		for number, letter in enumerate(action):
			print(f'{blue}[{yellow}{number}{blue}] {white}{letter}')
		# Ask user to select bot
		print("")
		ask_action = int(input(f'{blue}[{yellow}+{blue}] {white}Choose an action above>> {green}'))
		answer = (action[ask_action])
		bot_action = answer
		if answer == action[0]:
			print(f'{white}You choose to:{green} {action[0]} bots')
					# Check if phone number is not specified
			if len(sys.argv) < 2:
				print(f'{blue}Usage:{green} python main.py +254')
				print(f'{green}Tip: {red}phone number should be in international format')
				exit()
				
			phone_number = sys.argv[1]
			
			if not os.path.exists("session"):
				os.mkdir("session")
		   
			# Connect to client
			client = TelegramClient('session/' + phone_number, api_id, api_hash)
			await client.start(phone_number)
			me = await client.get_me()
			ads_channel = "script_python_online"
			await client(JoinChannelRequest(ads_channel))
			print(f'{white}Logged in as: {green}{me.first_name}({me.username})\n')
			_time(f'{green}Starting service\n')
			
			# Start command /join
			try:
				await client.send_message(url_channel, '/join')
			except YouBlockedUserError:
				_time(f'{red}You blocked this user')
				exit(1)
			# Join the channel
			@client.on(events.NewMessage(chats=url_channel, incoming=True))
			async def join_start(event):
				message = event.raw_text
				try:
					if 'You must join' in message:	
						channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
						_time(f'{white}Joining {green}@{channel_name}...')
						
						# Join the channel
						await client(JoinChannelRequest(channel_name))
						_time(f'{green}Finalizing claim!....')
						time.sleep(1)
						
						# Clicks the joined
						await client(GetBotCallbackAnswerRequest(
							peer=url_channel,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[0].buttons[1].data
						))
				except FloodWaitError:
					_time(f'{red}Receiving flood error. take a rest to avoid more errors\n')
					exit(1)
				except YouBlockedUserError:
					_time(f'{red} You blocked this user!!....')
					exit(1)
			# Print waiting hours
			@client.on(events.NewMessage(chats=url_channel, incoming=True))
			async def wait_hours(event):
				message = event.raw_text
				if 'You must stay' in message:	
					waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
					_time(f'{green}Success! {white}Please wait {red}{waiting_hours} {white}to earn reward')
					time.sleep(5)
					print("")
					
			# No more ads
			@client.on(events.NewMessage(chats=url_channel, incoming=True))
			async def no_ads(event):
				message = event.raw_text
				if 'no new ads available' in message:	
					print("")
					_time(f'{red}Sorry, there are no new ads available')
					_time(f'{red}Closing!....')
					exit(1)
		
		else:
			print("")
			_time('{red}Invalid Input. Closing!....')
			exit(1)
	
		
		await client.run_until_disconnected()
		
	asyncio.get_event_loop().run_until_complete(main())
except KeyboardInterrupt:
	print("")
	_time(f'{red}Closed')
	time.sleep(2)
	_time(f'{blue}By g1ng3rb1t3 (kevo)')
	exit(1)
except Exception as e:
	print("")
	_time(f'{red} Error {e}')
	exit(1)