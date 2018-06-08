# coding: utf8
'''
Главный модуль пакАвтодор. Содержит в себе все остальные модули.
'''

if True:
	from . пакГуи.модГуи import клсГуи
	from . пакРесурс.модРесурс import клсРесурс
	from . пакОбработка.модОбработка import клсОбработка

class клсАвтодор:
	'''
	Главный класс приложения содержит в себе графику, контроллер событий,
	логику и необходимые ресурсы.
	'''
	def __init__(сам):
		сам.рес = клсРесурс(сам)
		сам.обр = клсОбработка(сам)
		сам.гуи = клсГуи(сам)

	def Начать(сам):
		сам.гуи.Начать()
