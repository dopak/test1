import vk_api
import requests
import datetime

vk_session = vk_api.VkApi(token=f3caee452f620cabce7d7cd684195e431c6463557dab3b284572ac4aface7331a6d7b049fe78dba961737)
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)

vk = vk_api.VkApi(token=token)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:			
        if event.text == 'Привет' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Ваш текст'
		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='Ваш текст'
		)
attachments = []
from vk_api import VkUpload 
upload = VkUpload(vk_session)
image_url = 'Ссылка на картинку'
image = session.get(image_url, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
attachments.append(
    'photo{}_{}'.format(photo['owner_id'], photo['id'])
)
vk.messages.send(
    user_id=event.user_id,
    attachment=','.join(attachments),
    message='Ваш текст'
)