# coding: utf8
"""
Содержит код для рамки с командами окна СМТ.
"""
if True:
	from tkinter import Frame as клсРамка, Button as клсКнопка
	
class клсРамкаКоманды(клсРамка):
	def __init__(сам, предок, якорь):
		сам.__якорь = якорь
		сам.__предок = предок
		клсРамка.__init__(сам, предок, border=3, relief="groove")
		сам.pack(fill='x', side='bottom')
		
		сам.кнпПринять = клсКнопка(сам, text="Принять", border=2)
		сам.кнпПринять.pack(side='left', fill='x')
		
		сам.кнпСброс = клсКнопка(сам, text="Сброс", border=2)
		сам.кнпСброс.pack(side='left', fill='x')
		
		сам.кнпВыход = клсКнопка(сам, text="Выход", border=2, command=предок.Скрыть)
		сам.кнпВыход.pack(side='right', fill='x')
