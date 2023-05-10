import requests
import schedule
import time
import telebot
import datetime
import json
import os

# telegram_bot API_KEY
API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)
# 每個帳號對應的聊天 ID
chat_ids = os.environ['CHAT_ID']
# 星穹鐵道每個帳號對應的 cookie
cookies = os.environ['COOKIES'].split(',')

# 設置簽到項目，True為啟用，False為停用
HSR = True # 星穹鐵道
GS = True # 原神
HI3 = True # 崩壞3

# HoYoLab簽到
def sign_send():
    for i, cookie in enumerate(cookies):
        # 取得日期(當天日期，用於回傳簽到結果)
        # today = datetime.date.today()
        # today_str = today.strftime('%Y-%m-%d')
        # 取得日期(明天日期，依伺服器時區為準，用於簽到)
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%Y-%m-%d')
        # 設定 cookie
        headers = {'cookie': cookie}
        # 發送簽到請求，並回傳簽到結果至telegram_bot，並附上簽到日期(使用today_str或是tomorrow_str依伺服器時區為準)
        if HSR:
            response = requests.post("https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=zh-tw&act_id=e202303301540311", headers=headers)
            response_text = response.text
            response_dict = json.loads(response_text)
            message = response_dict['message']
            bot.send_message(chat_ids, tomorrow_str + '帳號' + str(i) + ' HSR簽到成功' + '\n' + message)
        if GS:
            response = requests.post("https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=zh-tw&act_id=e202102251931481", headers=headers)
            response_text = response.text
            response_dict = json.loads(response_text)
            message = response_dict['message']
            bot.send_message(chat_ids, tomorrow_str + '帳號' + str(i) + ' GS簽到成功' + '\n' + message)
        if HI3:
            response = requests.post("https://sg-public-api.hoyolab.com/event/mani/sign?lang=zh-tw&act_id=e202110291205111", headers=headers)
            response_text = response.text
            response_dict = json.loads(response_text)
            message = response_dict['message']
            bot.send_message(chat_ids, tomorrow_str + '帳號' + str(i) + ' HI3簽到成功' + '\n' + message)

# 簽到時間，可依伺服器時間自行修改
schedule.every().day.at('16:03').do(sign_send)

while True:
    schedule.run_pending()
    time.sleep(1)