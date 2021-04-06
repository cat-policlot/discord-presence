try:
	from pypresence import Client as Presence
except:
	import os
	os.system("python -m pip install pypresence")
	from pypresence import Client as Presence
import time
CONF_FILE = "discord_presence.conf"
RPC = Presence(750271599248408606)
print("reading config file...")
import configparser
config = configparser.ConfigParser()
if not CONF_FILE in config.read(CONF_FILE):
	print("config file not found,create conf file...")
	config["BUTTONS"] = {"button_example":"https://natribu.org/ru/"}
	config["DESC"] = {"desc":"example of desc"}
	with open(CONF_FILE, 'w') as configfile:
		config.write(configfile)
buttons = []
buttons_tmp = dict()
desc = None
if "BUTTONS" in config:
	for key in config["BUTTONS"]:
		buttons_tmp["label"] = key
		buttons_tmp["url"] = config["BUTTONS"][key]
		buttons.append(buttons_tmp)
	print(buttons)
else:
	buttons = None
if "DESC" in config:
	desc = list(config["DESC"].keys())[0]

RPC.start()
"""
Parameters
pid (int) – the process id of your game

state (str) – the user’s current status

details (str) – what the player is currently doing

start (int) – epoch time for game start

end (int) – epoch time for game end

large_image (str) – name of the uploaded image for the large profile artwork

large_text (str) – tooltip for the large image

small_image (str) – name of the uploaded image for the small profile artwork

small_text (str) – tootltip for the small image

party_id (str) – id of the player’s party, lobby, or group

party_size (list) – current size of the player’s party, lobby, or group, and the max in this format: [1,4]

join (str) – unique hashed string for chat invitations and ask to join

spectate (str) – unique hashed string for spectate button

match (str) – unique hashed string for spectate and join

buttons (list) – list of dicts for buttons on your profile in the format [{"label": "My Website", "url": "https://qtqt.cf"}, ...], can list up to two buttons

instance (bool) – marks the match as a game session with a specific beginning and end

Return type
pypresence.Response
"""
RPC.set_activity(buttons=buttons,state=desc)
while True:
	time.sleep(15)
