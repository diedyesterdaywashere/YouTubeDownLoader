from os import system
from time import sleep
system('pip3 install pytube')
system('cls')
from pytube import YouTube
print('Welcome to the YouTube Downloader! Choose your language:')
print('1 - English, 2 - Русский, 3 - Українська')
print('Created by diedyesterday! github.com/diedyesterdaywashere')
print('Current Version: 1.0')
languagenum = int(input('Choose Your Language: '))
if languagenum < 1:
	system('cls')
	print('You have chosen invalid number')
	sleep(1)
	print('Time to reload script!')
	sleep(1)
	print('Please restart script! (Auto-reload will be added in future)')
	sleep(10)
	stop
if languagenum == 1:
	system('cls')
	print('You have chosen English language')
	sleep(2)
	while True:
		link = input("Enter YouTube Link: ")
		yt = YouTube(link)
		ys = yt.streams.get_highest_resolution()
		ys.download()
		sleep(1)
		print('Download Finished!')
		sleep(20)
		system('cls')
if languagenum == 2:
	system('cls')
	print('Вы выбрали русский язык')
	sleep(2)
	while True:
		link = input("Введите ссылку на видео: ")
		yt = YouTube(link)
		ys = yt.streams.get_highest_resolution()
		ys.download()
		sleep(1)
		print('Видео скачано!')
		sleep(20)
		system('cls')
if languagenum == 3:
	system('cls')
	print('Ви обрали Україньску мову')
	sleep(2)
	while True:
		link = input("Введіть посилання на відео: ")
		yt = YouTube(link)
		ys = yt.streams.get_highest_resolution()
		ys.download()
		sleep(1)
		print('Відео завантажено!')
		sleep(20)
		system('cls')
if languagenum > 3:
	system('cls')
	print('You have chosen invalid number')
	sleep(1)
	print('Time to reload script!')
	sleep(1)
	print('Please restart script! (Auto-reload will be added in future)')
	sleep(10)
	stop