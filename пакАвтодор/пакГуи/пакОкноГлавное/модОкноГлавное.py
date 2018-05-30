# coding: utf8
'''
Содержит описание главного окна.
'''

if True:
   from tkinter import Tk
   
class клсОкноГлавное(Tk):
   def __init__(сам, якорь):
      сам.__якорь = якорь
      Tk.__init__(сам)
   
   def Начать(сам):
      сам.mainloop()
