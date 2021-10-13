import samino
from threading import Thread as TH
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.THISTLE_1 + style.BOLD)
print("""Ghost Massage Scrpit by """)
print(pyfiglet.figlet_format("ViCious", font="slant"))	

client = samino.Client("22D3085F471DF87A00FB4CE43052685FE93239644F93AD2140B23F3C77277FF6CAE5A0C164593CD9A8")

client.login(input("email : "), input("password : ")); print("Logged in")
blogLink=client.get_from_link(input("Chat Link: "))
comId=blogLink.comId

print(comId)
comId=blogLink.comId
chatId=blogLink.objectId
local =samino.Local(comId)
print("\nJoined Community...")

while True:
    mssg=input("\n>> ")
    local.send_message(chatId=chatId,message=mssg,messageType=109,asWeb=True,comId=comId)
    print("\nMessage send succesfully...")