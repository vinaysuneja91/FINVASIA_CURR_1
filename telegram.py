import requests


def telegram_bot_sendtext(bot_message):
    # https://api.telegram.org/bot1572005733:AAGcVMSFhF4ZETjf3zgRUOolNQM6mwUyIv4/getUpdates

    bot_token = '1572005733:AAGcVMSFhF4ZETjf3zgRUOolNQM6mwUyIv4'
    bot_chatID = '-1001279275433'  # -465990036
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


#test = telegram_bot_sendtext("Hello from Telegram bot")
# print(test)
