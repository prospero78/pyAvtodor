# coding: utf8
'''
Содержит пакет обработки всей логики программы.
'''

if True:
	import sys as мСис

class клсОбработка:
	def __init__(сам, якорь):
		сам.__якорь = якорь

	def Выход(сам):
		мСис.exit()

	def О_Программе_Показать(сам):
		гуи = сам.__якорь.гуи
		гуи.длгО_Программе.Показать()

	def СМТ_Уст(сам):
		гуи = сам.__якорь.гуи
		гуи.длгСмт.Показать()

	def Авто_Уст(сам):
		гуи = сам.__якорь.гуи
		гуи.длгАвто.Показать()

	def Авто_Добавить(сам):
		гуи = сам.__якорь.гуи
		гуи.длгАвтоДобав.Показать()
