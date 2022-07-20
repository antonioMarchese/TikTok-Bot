from utilities.TikTok import equals
from utilities.TikTok import TikTok
from utilities import constant as const
import os
import time
import telebot

bot = telebot.TeleBot(const.HTTP_API)
bot.config['api_key'] = const.HTTP_API
default_msg = 'Nada de alterações na bio por enquanto.'
i = 0
while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear') # Just to clean the terminal
        print("Extraíndo bio...\n")
        aux = TikTok()
        coupon = aux.extract()
        if equals(coupon) == False:
            with open('cupom.txt', 'w') as file:
                file.write(coupon)
                file.close()
            message = f'Essa é a bio atual do TikTok da Shopee. Seu cupom pode estar ai:\n{coupon}\n'
            bot.send_message(const.CHAT_ID, message)
        else:
            if (i % 10 == 0):
                print(f'{default_msg}\n')
        print("Dados extraídos com sucesso. Próxima execução em 3 minutos...")
    except:
        print('Ocorreu um erro durante a execução do programa. Vamos tentar de novo. Caso o erro persista, reinicie o aplicativo.')
        pass
    time.sleep(180)