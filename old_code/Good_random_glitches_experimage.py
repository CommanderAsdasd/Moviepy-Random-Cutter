# -*- coding: utf-8 -*-
# C:/Python27/python.exe
import random
import time
import pip
# from pillow import imageio
from generate_sequence import *
from files_scanner import *
from PIL import *
# import imageio

# pip.main(["install", "imageio"])
# imageio.plugins.ffmpeg.download()

class VideoEditor():
	pass

def test():
	pass


# =======================================================================OUT====================================
path = '../shaker/'
print(files_scanner_video(path))
exec_numb = 5
dur = []

def randclip(maxclips):
	return random.randint(0, maxclips)

def cut_logic(exec_numb):
	clips = []
	print(clips)
	clipsList = files_scanner_video(path)
	clipsCounter = len(clipsList) - 1
	for i, objects in enumerate(clipsList[::1]):
		clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, i + random.uniform(1, 4)))
	for i, objects in enumerate(clips):
		clips[i] = fl_image()
		# if i % 3 == 0:
			
	# 	if i % random.randint(1, 3) == 0:
	# 		if 1 == random.randint(1, 2):
	# 			clips[i] = speedx(clips[i], 4)
	# 		else:
	# 			clips[i] = speedx(clips[i], random.randint(1, 10) * 0.1)
				
		# try:
		# 	if i < len(clips)-5:
		# 		clips.append(clips_array([[clips[i], clips[i+1]],
	 #                          [clips[i+3], clips[i+4]]]))
		# except:
		# 	pass
	concat_and_write(clips, exec_numb)

def resulst_store(clips, exec_numb):
	pass
	# if i % 4 == 0:
	# 	clips[i] = time_symmetrize(clips[i])
	# clips.append(generate_rand_sequence(clipsList[i], 1, random.uniform(1, 1.1)))
# 	clips.append(generate_rand_sequence(clipsList[random.randint(0, len(clipsList)-1)], 1, i + random.uniform(0, 4)))
# 	clips.extend(generate_freeze(clipsList[i], [1.01, 1.02], 3))
# 	clips.append(generate_rand_sequence(clipsList[i], 1, 2))
# 	clips.append(generate_rand_sequence(clipsList[i], 1, random.uniform(0, 0.1)))
# 	clips += generate_freeze(clipsList[1], [1, 1.02, 3, 3.05, 7, 5.24], 2)
# randpoints = []
# clips = []
# print()
# 	currclipDuration = clipsList[i].duration
# 	for j in range(0,1):
# 		point1 = random.uniform(0, currclipDuration)
# 		point2 = point1 + 0.2
# 		randpoints.append(point1)
# 		randpoints.append(point2)
# 		print(randpoints)

def targets(x,y):
    yield (x,y) # Center
    yield (x+1,y) # Left
    yield (x-1,y) # Right
    yield (x,y+1) # Above
    yield (x,y-1) # Below
    yield (x+1,y+1) # Above and to the right
    yield (x+1,y-1) # Below and to the right
    yield (x-1,y+1) # Above and to the left
    yield (x-1,y-1) # Below and to the left


def changeImage():
	for x in range(width):
	    for y in range(height):
	        px = pixels[x][y]
	        if px[0] == 255 and px[1] == 255 and px[2] == 255:
	            for i,j in targets(x,y):
	                newpixels[i][j] = replacementColor



def concat_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	try:
		clipOut = concatenate_videoclips(clips, method='compose')
		clipOut.write_videofile("./" + write_data + "-out.mp4",fps=25)
	except Exception:
		print("An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			cut_logic(exec_numb)
		else:
			print("game over")


cut_logic(exec_numb)
"""
# Чета он вызывает не то, какую-то хуйню, пытается из "instance" отнять in
t# Потом надо потренироваться в композиции и
# Нужно сорганизовать всё это в структуру. Что будет неизменным, а что поменяется? Неизменным будет обращение к функции crop-a, а переменным - параметры, которые в неё передаются. Чтобы можно было вызывать рандомное количество склеек, точнее, склейки происходили в некое случайное время и склеивались в одну структуру. Должен объявляться некий список, в который подаётся случайное количество значений. Генерируется какое-то число случайных значений от нуля до конца клипа.
# Нужно сделать несколько секвенций, а ещё сделать
# как я в последний раз решил эту проблему с дюрейгенами, в какой-то либе метод отрабатывал не по видосу, а по интегеру, 
# Придумать прикольные числовые последовательон 
	Ещё надо намутить не, не то. Надо намутить эцсамое, балин, ща, надо сделать что-то для удобства, такую фичу, не то завернуть в классы, не то, а, даты прихуярить.
	Нужнна какая-то другая логика, типа "берёшь случайный кусочек видео и вставляешь его в случайное место(лол)" - для этого надо знать длительность клипа, потом выбрать нижнее значение, верхнее, вырезаешь, а потом надо 3 промежутка видео - от 0 до cut_low, cut_low-cut_top, cut_top-clip.Duration
- Лучше всего попробовать передавать туплами в функцию

# Можно потренироваться в паттернах добавив разные. Можно сделать 
Структуры данных
"""
