import requests
import random
import string
import os
try:
    import requests
except:
    os.system("pip install requests")
try:
    import getuseragent
except:
    os.system("pip install getuseragent")
import requests
import getuseragent
from getuseragent import UserAgent
ua = UserAgent('android').Random()
post_link = input('TikTok Views [!] Enter Link: ')
def create_username():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=15))
username = create_username()
response = requests.post('https://api.likesjet.com/freeboost/3',
                         json={"link": post_link, "tiktok_username": username, 'email': f'datahack{random.randint(100000, 999999)}@gmail.com'},
                         headers={"Host": "api.likesjet.com",
                                  "content-length": "137",
                                  "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
                                  "accept": "application/json, text/plain, */*",
                                  "content-type": "application/json",
                                  "sec-ch-ua-mobile": "?1",
                                  "user-agent": ua,
                                  "sec-ch-ua-platform": "\"Android\"",
                                  "origin": "https://likesjet.com",
                                  "sec-fetch-site": "same-site",
                                  "sec-fetch-mode": "cors",
                                  "sec-fetch-dest": "empty",
                                  "referer": "https://likesjet.com/",
                                  "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"})
print(response.json()['message'])

