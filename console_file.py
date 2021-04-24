import os
import shutil
import sys
import questions
import money
def func_console():
    a = 12
    sour_dir = os.getcwd()
    while a!=12:
        print(
           '1. Создать папку\n\
            2. Удалить (файл/папку)\n\
            3. Копировать (файл/папку)\n\
            4. Просмотр содержимого рабочей директории\n\
            5. Посмотреть только папки\n\
            6. Посмотреть только файлы\n\
            7. Просмотр информации об операционной системе\n\
            8. Создатель программы\n\
            9. Играть в викторину\n\
            10. Мой банковский счет\n\
            11. смена рабочей директории\n\
            12. Выход\n'
        )
        a = int(input('Ваш выбор: '))
        if a==1:
            folder = input('Ваша папка ')
            os.mkdir(folder)
        elif a==2:
            folder = input('Ваша папка ')
            if os.path.exists(os.path.join(os.getcwd(),folder)):
                os.rmdir(os.path.join(os.getcwd(),folder))
            else:
                print('Такой папки нет')
                input()
        elif a==3:
            folder_source = input('Папка, что копируем ')
            folder = input('Ваша папка ')
            if os.path.exists(os.path.join(os.getcwd(), folder_source)):
                shutil.copytree(os.path.join(os.getcwd(),folder_source), os.path.join(os.getcwd(),folder))
            else:
                print('Нет такой папки')
                input()
        elif a==4:
            print(os.listdir(os.path.join(os.getcwd())))
            input()
        elif a==5:
            dirs = os.listdir(os.path.join(os.getcwd()))
            dirss = []
            for i in dirs:
                if 'LICENSE' not in i:
                    if '.' not in i:
                        dirss.append(i)
                    else:
                        pass
                else:
                    pass
            print(dirss)
            input()
        elif a==6:
            dirs = os.listdir(os.path.join(os.getcwd()))
            dirss = []
            for i in dirs:
                if 'LICENSE' in i or '.' in i:
                    dirss.append(i)
                else:
                    pass
            print(dirss)
            input()
        elif a==7:
            print(sys.platform)
            input()
        elif a==8:
            print('Idel Nice')
            input()
        elif a==9:
            questions.question()
        elif a==10:
            money.func()
        elif a==11:
            new_dir = input('Введите вашу новую директорию ')
            if os.path.exists(new_dir):
                os.chdir(new_dir)
                input()
            else:
                print('Такого пути нет')
                input()
        elif a==12:
            pass
        else:
            print('Нужно выбрать от 1 до 12')
            input()