import AminoLab
import asyncio

import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.THISTLE_1 + style.BOLD)
print("""       Chat Report       Scrpit by """)
print(pyfiglet.figlet_format("ViCious", font="slant"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
ndcId = clients.ndcId[int(input("Select the community >> "))-1]
chatlink = input("Chat Link >> ")
chat_info = client.get_from_link(chatlink)
userId = chat_info.objectId

while True:
	print("Report Sended...")
	with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
		_ = [executor.submit(client.report,ndcId,reason="Trolling, Pornography, Inappropriate content", flagType=5, userId=userId) for _ in range(100)]