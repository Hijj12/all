import amino
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.THISTLE_1 + style.BOLD)
print(""" Join Vc Bot Id  Scrpit by """)
print(pyfiglet.figlet_format("ViCious", font="slant"))
client = amino.Client()
emails = open("email.txt", "r")
chatlink = input("Chat Link >> ")
password = input("Password For All Accounts >> ")
for line in emails:
	email = line.strip()
	try:
		client.login(email=email, password=password)
		chat_info = client.get_from_code(chatlink)
		chat_id = chat_info.objectId
		community_id = chat_info.path[1:chat_info.path.index('/')]
		client.join_voice_chat(comId=community_id, chatId=chat_id, joinType=2)
		print(f"{email} Joined To Voice Chat")
	except amino.lib.util.exceptions.VerificationRequired as e:
		print(f"VerificationRequired for {email}")
		url = re.search("(?P<url>https?://[^\s'\"]+)", str(e)).group("url")
		print(f"Verification Link = {url}")
	except amino.lib.util.exceptions.ActionNotAllowed:
		print(f"ActionNotAllowed {email}")
	except:
		print(f"{email} Can't Join To Voice Chat")
		pass