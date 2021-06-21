import vk_api, traceback, random, time
from datetime import datetime
from vk_api.bot_longpoll import  VkBotEventType, VkBotLongPoll

token='токен'

_vk_=vk_api.VkApi(token=token)
vk=_vk_.get_api()
_id_=vk.groups.getById()[0]['id']
longpoll=VkBotLongPoll(_vk_, group_id=_id_)

	
while True:
	try:
		for event in longpoll.listen():
			print(event)
			if event.type == VkBotEventType.MESSAGE_NEW:
				message=event.message
				text=message['text']
				peer_id=message['peer_id']
				time_=message['date']
				from_id=message['from_id']
				attachments=message['attachments']
				conversation_message_id=message['conversation_message_id']
				fwd_messages=message['fwd_messages']
				if text=='.пинг':
					pong=f'Понг бота: {abs(round(datetime.now().timestamp()-time_, 3))}'
					vk.messages.send(peer_id=peer_id, message=pong, random_id=random.randint(1, 10e9))
	except:
		print('Я падаю.')
		traceback.print_exc()
		time.sleep(5)
			
# Written with love. By Alexey Kuznetsov.
