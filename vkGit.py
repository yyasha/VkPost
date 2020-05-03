import vk_api

vk_session = vk_api.VkApi('phone', 'password')
vk_session.auth()
vk = vk_session.get_api()

HalloMessage = f"-10 видео, которые я рекомендую посмотреть (обновляется каждый день)-\n{'-' * 35}\n"
commentMessage = "код проекта - https://github.com/yyasha/VkPost"

# ------------------------ 2 ------------------------ #

from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.youtube.com/playlist?list=PLbvgU7in65s_F1DyneaGmwLTUrwkgIsKL'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

NowNumber = 0;
for i, tr in enumerate(soup.select('tr.pl-video')):
	i += 1
	NowNumber = i
NowPostNumber = NowNumber - 10
Number = 1
TableNumber = 10

for i, tr in enumerate(soup.select('tr.pl-video')):
	if i >= NowPostNumber:
		# print('{}. {}'.format(Number, tr['data-title']))
		# print('https://www.youtube.com' + tr.a['href'])
		# print('-' * 35)
		UjgJK = tr['data-title']
		OIUhnJK = tr.a['href']
		Message = f"{TableNumber}. {UjgJK}\nhttps://www.youtube.com{OIUhnJK}\n{'-' * 35}\n"
		print(f"{TableNumber}. {UjgJK}\nhttps://www.youtube.com{OIUhnJK}\n{'-' * 35}")
		TableNumber -= 1

		if Number == 1:
			Message1 = Message
		elif Number == 2:
			Message2 = Message
		elif Number == 3:
			Message3 = Message
		elif Number == 4:
			Message4 = Message
		elif Number == 5:
			Message5 = Message
		elif Number == 6:
			Message6 = Message
		elif Number == 7:
			Message7 = Message
		elif Number == 8:
			Message8 = Message
		elif Number == 9:
			Message9 = Message
		elif Number == 10:
			Message10 = Message

		Number += 1
GMessage = HalloMessage + Message10 + Message9 + Message8 + Message7 + Message6 + Message5 + Message4 + Message3 + Message2 + Message1
i = vk.wall.post(message=GMessage)      #первый пост / first post
PostId = i['post_id']
vk.wall.createComment(post_id=PostId, message=commentMessage)
vk.wall.pin(post_id=PostId)
time.sleep(43200)

while True:
	vk_session.auth()

	NowNumber = 0;
	for i, tr in enumerate(soup.select('tr.pl-video')):
		i += 1
		NowNumber = i
	NowPostNumber = NowNumber - 10
	Number = 1

	for i, tr in enumerate(soup.select('tr.pl-video')):
		if i >= NowPostNumber:
			# print('{}. {}'.format(Number, tr['data-title']))
			# print('https://www.youtube.com' + tr.a['href'])
			# print('-' * 35)
			UjgJK = tr['data-title']
			OIUhnJK = tr.a['href']
			Message = f"{Number}. {UjgJK}\nhttps://www.youtube.com{OIUhnJK}\n{'-' * 35}\n"
			print(f"{Number}. {UjgJK}\nhttps://www.youtube.com{OIUhnJK}\n{'-' * 35}")

			if Number == 1:
				Message1 = Message
			elif Number == 2:
				Message2 = Message
			elif Number == 3:
				Message3 = Message
			elif Number == 4:
				Message4 = Message
			elif Number == 5:
				Message5 = Message
			elif Number == 6:
				Message6 = Message
			elif Number == 7:
				Message7 = Message
			elif Number == 8:
				Message8 = Message
			elif Number == 9:
				Message9 = Message
			elif Number == 10:
				Message10 = Message

			Number += 1
	GMessage = HalloMessage + Message10 + Message9 + Message8 + Message7 + Message6 + Message5 + Message4 + Message3 + Message2 + Message1

	print(vk.wall.edit(message= GMessage, post_id=PostId))

	time.sleep(43200)
