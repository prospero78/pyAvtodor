# coding: utf8
'''
Содержит пакет обработки всей логики программы.
'''

if True:
	import sys as мСис
	from . пакСобытия.модСобытия import клсСобытия

class клсОбработка:
	def __init__(сам, якорь):
		сам.__якорь = якорь
		сам.соб = клсСобытия(сам, якорь)

	def Закончить(сам):
		мСис.exit()
