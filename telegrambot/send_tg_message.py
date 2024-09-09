import requests
from .models import TelegramSettings
import logging


logger = logging.getLogger('telegrambot')


def send_message_telegram(name, email, phone):
    try:
        api = 'https://api.telegram.org/bot'
        settings = TelegramSettings.objects.first()
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        url = api + token + '/sendMessage' + '?&chat_id=' + chat_id + '&text=' + text + '\nИмя: ' + name + '\nE-mail: ' + email + '\nТелефон: ' + phone
        response = requests.post(url, data={
            'chat_id': chat_id,
            'text': text
        })
    except Exception as e:
        logger.error(e)

    finally:

        if response.status_code == 200:
            logger.info('Сообщение отправлено')

        elif response.status_code in list(range(400, 411)):
            logger.info(f'{response.json()}')

        elif response.status_code == 500:
            logger.info('Сервер вернул 500')
