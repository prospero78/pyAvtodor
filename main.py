# coding: utf8
'''
Пробуем сделать программу учёта материалов для ООО "Черняховский Райавтодор".
'''
if True:
    from пакАвтодор.модАвтодор import клсАвтодор

def main():
    приложение = клсАвтодор()
    приложение.Начать()
    
if __name__=='__main__':
    main()
