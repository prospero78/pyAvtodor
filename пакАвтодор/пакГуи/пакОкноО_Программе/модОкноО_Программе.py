# coding: utf8
'''
Инициализация пакета окна "О программе".
'''

if True:
   from tkinter import Toplevel as клсОкно, Button as клсКнопка, Text as клсТекст
   
class клсОкноО_Программе(клсОкно):
   def __init__(сам, якорь):
      сам.__якорь = якорь
      клсОкно.__init__(сам)
      сам.Скрыть()
      сам.кнпОк = клсКнопка(сам, text='Ok', command = сам.Скрыть)
      сам.кнпОк.pack(side='bottom', fill='x')
      сам.тСодержание = клсТекст(сам)
      сам.тСодержание.insert('1.0', 'Проверка текста')
      сам.тСодержание.pack(side='top', fill='both', expand=1)
   
   def Скрыть(сам):
      сам.state('withdraw')
      сам.grab_release()
   
   def Показать(сам):
      сам.state('normal')
      сам.lift()
      сам.focus_set()
      сам.grab_set()
      
