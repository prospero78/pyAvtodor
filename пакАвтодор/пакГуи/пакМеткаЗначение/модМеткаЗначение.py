# coding: utf8
"""
Модуль графического элемента "метка-значение"
"""
if True:
	from tkinter import Frame as клсРамка, Label as клсМетка, Entry as клсВвод
	
class клсМеткаЗначение(клсРамка):
	def __init__(сам, предок, якорь, метка, значение):
		сам.__якорь = якорь
		клсРамка.__init__(сам, предок, border=3, relief="groove")
		сам.метка = клсМетка(сам, text=метка, border=3, relief='ridge', width=20, justify='right')
		сам.метка.pack(side='left', anchor='w')
		сам.ввод = клсВвод(сам, border=3)
		сам.ввод.insert(0, значение)
		сам.ввод.pack(fill='x')
		сам.pack(fill='x',side='top')
		
		# фрейм для выхода из формы
