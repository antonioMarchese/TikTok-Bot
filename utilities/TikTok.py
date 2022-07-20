from utilities import constant as const
from requests_html import HTMLSession

class TikTok:

    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    def extract(self):
        # Gets the bio
        r = self.session.get(const.BASE_URL, headers=self.headers)
        r.html.render(sleep=1, timeout=60)
        coupon = r.html.find('h2[data-e2e="user-bio"]', first=True).text
        # Returns the bio without the last character
        return coupon[:-1]

def equals(coupon):
    # This function reads the previous bio to check if its equal to the actual bio
    try:
        with open('cupom.txt', 'r') as file:
            cupom = file.read()
            file.close()
        if cupom == coupon:
            print('Não houve alteração na bio, portanto o arquivo não será alterado.\n')
            return True
        else:
            return False
    except:
        return False