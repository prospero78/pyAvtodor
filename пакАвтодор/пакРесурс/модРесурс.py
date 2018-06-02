# coding: utf8
'''
Содержит все используемые ресурсы в программе.
Позволяет производить интернационализацию и настройку приложения.
'''

class клсРесурс:
   def __init__(сам, якорь):
      сам.__якорь = якорь
      сам.Конфигурировать()
      сам.Язык_Уст()

   def Конфигурировать(сам):
      сам.сборка = "0011"
      сам.сборка_дата = "2018-06-02"
      сам.сборка_время = "09:12"
      сам.язык = "ру"

   def Язык_Уст(сам):
      if сам.язык == "ру":
         сам.Ру_Уст()

   def Ру_Уст(сам):
      сам.окноГлавное_Название = "Склад (сборка "+сам.сборка+")"
      сам.окноГлавное_РазмерМинХ = 400
      сам.окноГлавное_РазмерМинУ = 600
      сам.окноГлавное_кнпФайл = "Файл"
      сам.окноГлавное_мнуНовый = "Новый..."
      сам.окноГлавное_мнуВыход = "Выход"
      сам.окноГлавное_кнпАсфальт = "Асфальт"
      сам.окноГлавное_мнуРецепты = "Рецепты"
      сам.окноГлавное_мнуПаспорта = "Паспорта"
      сам.окноГлавное_мнуОтгрузка = "Отгрузка"
      сам.окноГлавное_кнпСправка = "Справка"
      сам.окноГлавное_мнуСправка = "Справка по программе"
      сам.окноГлавное_мнуО_Программе = "О программе..."
      сам.окноГлавное_кнпНастройка = "Настройка"
      сам.окноГлавное_мнуПользователи = "Пользователи"
      сам.окноГлавное_мнуОтображениеДаты = "Отобржение даты"
      сам.окноГлавное_мнуОтображениеВремени = "Отображение времени"
      сам.окноГлавное_мнуСмт_Уст = "СМТ..."

      сам.окноО_Программе_текст = """Программа учёта материальных средств автодора.
   Лицензия: BSD-2.
   Автор: prospero.78.su@gmail.com

   Программа предназначена для учёта поступления материалов
   на склад автодора, пересчёта в изготавливаемый асфальт,
   составления различного рода отчётов по видам контрагентов
   и материалам, учёта транспортных документов"""
