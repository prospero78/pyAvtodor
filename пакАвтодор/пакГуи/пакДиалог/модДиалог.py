# coding: utf8
'''
Класс диалогового окна
'''

if True:
	from tkinter import Toplevel as клсОкно

class клсДиалог(клсОкно):
	def __init__(сам):
		клсОкно.__init__(сам)
		сам.Скрыть()

	def Скрыть(сам):
		сам.state('withdraw')
		сам.grab_release()

	def Показать(сам):
		сам.state('normal')
		сам.lift()
		сам.focus_set()
		сам.grab_set()
