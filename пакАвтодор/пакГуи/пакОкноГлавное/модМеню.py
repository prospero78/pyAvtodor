# coding: utf8
'''
Описывает меню для операций в главном окне.
Меню упаковано в отдельный фрейм для лёгкого перемещения по окну,
в случае необходимости.
'''

if True:
   from tkinter import Frame as Фрейм, Menubutton as МенюКнопка, Menu as Меню

class клсМеню(Фрейм):
   def __init__(сам, предок, якорь):
      сам.__якорь = якорь
      сам.__предок = предок
      рес = якорь.рес
      обр = якорь.обр
      Фрейм.__init__(сам, предок)
      сам.pack(side='top',fill='x')

      сам.кнпФайл = МенюКнопка(сам, text = рес.окноГлавное_кнпФайл)
      сам.кнпФайл.pack(side='left',fill='x')

      мнуФайл  =  Меню(сам.кнпФайл, tearoff = 0 )
      мнуФайл.add_cascade(label=рес.окноГлавное_мнуНовый)
      мнуФайл.add_separator()
      мнуФайл.add_cascade(label=рес.окноГлавное_мнуВыход, command = обр.соб.Выход)

      сам.кнпФайл["menu"]  =  мнуФайл
      сам.мнуФайл = мнуФайл

      сам.кнпАсфальт = МенюКнопка(сам, text = рес.окноГлавное_кнпАсфальт)
      сам.кнпАсфальт.pack(side='left',fill='x')

      мнуАсфальт  =  Меню(сам.кнпАсфальт, tearoff = 0 )
      мнуАсфальт.add_cascade(label=рес.окноГлавное_мнуРецепты)
      мнуАсфальт.add_cascade(label=рес.окноГлавное_мнуПаспорта)
      мнуАсфальт.add_cascade(label=рес.окноГлавное_мнуОтгрузка)

      сам.кнпНастройка = МенюКнопка(сам, text = рес.окноГлавное_кнпНастройка)
      сам.кнпНастройка.pack(side='left',fill='x')

      мнуНастройка  =  Меню(сам.кнпНастройка, tearoff = 0 )
      мнуНастройка.add_cascade(label=рес.окноГлавное_мнуПользователи)
      мнуНастройка.add_separator()
      мнуНастройка.add_cascade (label=рес.окноГлавное_мнуСмт_Уст, command=обр.соб.СМТ_Уст)
      мнуНастройка.add_separator()
      мнуНастройка.add_cascade (label=рес.окноГлавное_мнуАвто_Уст, command=обр.соб.Авто_Уст)
      мнуНастройка.add_separator()
      мнуНастройка.add_cascade(label=рес.окноГлавное_мнуОтображениеДаты)
      мнуНастройка.add_cascade(label=рес.окноГлавное_мнуОтображениеВремени)

      сам.кнпНастройка["menu"]  =  мнуНастройка
      сам.кнпНастройка = мнуНастройка


      сам.кнпСправка = МенюКнопка(сам, text = рес.окноГлавное_кнпСправка)
      сам.кнпСправка.pack(side='left',fill='x')

      мнуСправка  =  Меню(сам.кнпСправка, tearoff = 0 )
      мнуСправка.add_cascade(label=рес.окноГлавное_мнуСправка)
      мнуСправка.add_separator()
      мнуСправка.add_cascade(label=рес.окноГлавное_мнуО_Программе, command = обр.соб.О_Программе_Показать)

      сам.кнпСправка["menu"]  =  мнуСправка
      сам.мнуСправка = мнуСправка
