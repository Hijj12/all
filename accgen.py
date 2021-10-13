import requests,json,os
try:
  import samino
except:
  os.system("pip install samino")
  os.system('clear')
d = 'by'
import samino
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.THISTLE_1 + style.BOLD)
print("""   Acount Gen  Scrpit by """)
print(pyfiglet.figlet_format("ViCious", font="slant"))
headers = {
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '35',
    'content-type': 'application/json',
    'cookie':'__auc=e72277dd1793efef0c5ba0db4d8; __qca=P0-2125635587-1620259566756; G_ENABLED_IDPS=google; __gads=ID=fd25c8819b58298c:T=1620259596:S=ALNI_MYgGClDj--AgWtT6Oa_pvn5ENBUcw; gdpr_cookie_agreee=1; exp=60-0; __asc=; _ga_9SJ4LCCH1X=GS1.1.1631388103.11.0.1631388103.0; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1733508529.1620259566; _gid=GA1.2.18082541.1631388105; session=.eJwNyrEOgjAQANBfMTc7KMJCwoApEkl6LEXCLUTbRlooMQSFQPh3Wd70Vqg_enDPXvcjhOPw1UdQ-YkDNQ.YT0DBA.IsbCVSlbjfKGVp8ONzK0IpEZzZ8',
    'origin': 'https://aminoapps.com',
    'referer': 'https://aminoapps.com/c/arabkpoper/home/',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'yMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'x-requested-with': 'xmlhttprequest'
}

client = samino.Client('22D3085F471DF87A00FB4CE43052685FE93239644F93AD2140B23F3C77277FF6CAE5A0C164593CD9A8')

def check(email : str):
    data=json.dumps({
      'email': email
    })
    req=requests.post("https://aminoapps.com/api/register-check",data=data,headers=headers)
    if req.status_code != 200 : raise TypeError(req.text)
    return json.loads(req.text)

def check_code(email : str,code : str):
    data=json.dumps({
        'validationContext':{'data': {'code': code},
        'identity': email,
        'type': 1,
        'verifyInfoKey': None
    }})
    req=requests.post("https://aminoapps.com/api/auth/check-security-validation",data=data,headers=headers)
    if req.status_code != 200 : raise TypeError(req.text)
    return json.loads(req.text)

def register_check(email : str,password : str):
    data=json.dumps({
      'email': email,
      'phoneNumber': "",
      'secret': "hhhhhh"
    })
    req=requests.post("https://aminoapps.com/api/register-check",data=data,headers=headers)
    if req.status_code != 200 : raise TypeError(req.text)
    return json.loads(req.text)
listacc = [] ; listacc.append(d+' Code/A7rf')
def register(email : str, password : str,nickname : str,code : str):
    data=json.dumps({
        'email': email,
        'nickname': nickname,
        'phoneNumber': "",
        'secret2': password,
        'validationContext': {
            'data': {'code': code},
            'code': code,
            'identity': email,
            'type': 1,
            '__original':{
                'data': {'code': code},
                'code': code,
                'identity': email,
                'type' : 1,
                '__response': {}
    }}}) ; 
    req=requests.post("https://aminoapps.com/api/register",data=data,headers=headers)
    if req.status_code != 200 : raise TypeError(req.text)
    return json.loads(req.text)
psw = input("your passwords : ")
nic = input("nickname : ")
os.system('clear')
while True:
    email = input("enter email : ")
    client.send_verify_code(email = email)
    code = input("enter code : ")
    register(email = email,password = psw,nickname = nic,code = code)
    os.system('clear')
    acc = f'email : {email} password : {psw}'
    listacc.append(acc)
    for l in listacc : print(l)