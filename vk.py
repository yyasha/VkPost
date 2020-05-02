import vk_api

vk_session = vk_api.VkApi('phone', 'password')
vk_session.auth()
vk = vk_session.get_api()

PostId = "336"
HalloMessage = f"-10 видео, которые я рекомендую посмотреть (обновляется каждый день)-\n{'-' * 35}\n"

# print(vk.wall.post(message="///"))

# print(vk.wall.edit(message="i", post_id=PostId))

# ------------------------ 2 ------------------------ #

from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.youtube.com/playlist?list=PLbvgU7in65s_F1DyneaGmwLTUrwkgIsKL'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# NowNumber = 0;
# for i, tr in enumerate(soup.select('tr.pl-video')):
# 	i += 1
# 	NowNumber = i
# NowPostNumber = NowNumber - 10
# Number = 1

# for i, tr in enumerate(soup.select('tr.pl-video')):
# 	if i >= NowPostNumber:
# 		# print('{}. {}'.format(Number, tr['data-title']))
# 		# print('https://www.youtube.com' + tr.a['href'])
# 		# print('-' * 35)
# 		UjgJK = tr['data-title']
# 		OIUhnJK = tr.a['href']
# 		Message = f"{Number}. {UjgJK}\nhttps://www.youtube.com{OIUhnJK}\n{'-' * 35}\n"
# 		print(f"{Number}. {UjgJK}\nhttps://www.youtube.com{OIUhnJK}\n{'-' * 35}")

# 		if Number == 1:
# 			Message1 = Message
# 		elif Number == 2:
# 			Message2 = Message
# 		elif Number == 3:
# 			Message3 = Message
# 		elif Number == 4:
# 			Message4 = Message
# 		elif Number == 5:
# 			Message5 = Message
# 		elif Number == 6:
# 			Message6 = Message
# 		elif Number == 7:
# 			Message7 = Message
# 		elif Number == 8:
# 			Message8 = Message
# 		elif Number == 9:
# 			Message9 = Message
# 		elif Number == 10:
# 			Message10 = Message

# 		Number += 1
# GMessage = HalloMessage + Message1 + Message2 + Message3 + Message4 + Message5 + Message6 + Message7 + Message8 + Message9 + Message10
# print(vk.wall.post(message=	GMessage))

# time.sleep(86400)

while True:
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
	GMessage = HalloMessage + Message1 + Message2 + Message3 + Message4 + Message5 + Message6 + Message7 + Message8 + Message9 + Message10

	print(vk.wall.edit(message= GMessage, post_id=PostId))

	time.sleep(43200)