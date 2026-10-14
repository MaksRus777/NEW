import random as rm
import time
import string

english_words = []
def traning_one_symvol():
    spesial_symvols =str(""",'"[]{}./""")
    list_of_litters = string.ascii_lowercase
    # len_list_of_litters = len(list_of_litters)
    # print(len_list_of_litters)
    try:
        print('\n\n\n\n\nТренировка ввода одного символа.\n\n\n\n\n')
        count = int(input('Введите количество тренировочных символов:\n'))
        if count == 0:
            print('Число символов не должны быть равным 0, попробуйте еще раз.')
        else:   
            print(f'Нажмите "Enter", чтобы начать.')

        start = input('')
        a=0
        mistake = 0
        starttime=time.time()
        list_of_mist=[]


        while a != count:
            if count == 0:
                break
            display_litter = list_of_litters[rm.randint(0,len(list_of_litters)-1)]
            print(f'--> {display_litter}\n')
            print(' ')
            traning_print_value = input(str(''))
        
            if traning_print_value == display_litter:
                a+=1
            
            else:
                mistake += 1
                list_of_mist.append(display_litter)
                a+=1 
            print(' ')
            
        else:
            endtime=time.time()
            time_of_exirsize = endtime-starttime
            unic_list = list(set(list_of_mist))
            if count !=0:
                print(f'Кол-во тренировочных символов - {count}')
                print(f'Кол-во ошибок - {mistake} ({(mistake/count)*100}%)')
                print(f"Ваше время - {time_of_exirsize} сек.")
                if mistake > 0:
                    print('Ошибки:')
            for i in unic_list:
                if list_of_mist.count(i) == 1:
                    print(f"{i} - {list_of_mist.count(i)} раз")
                else:
                    print(f"{i} - {list_of_mist.count(i)} раза")
            time.sleep(10)
    except ValueError:
        print("Здесь нужно ввести число, попробуйте еще раз.")
        time.sleep(10)


def traning_3_symvols():
    spesial_symvols =str(""",'"[]{}./""")
    list_of_litters = string.ascii_lowercase
    # len_list_of_litters = len(list_of_litters)
    # print(len_list_of_litters)
    try:
        print('\n\n\n\n\nТройные символы.\n\n\n\n\n')
        count = int(input('Введите количество тренировочных тройных символов:\n'))
        if count == 0:
            print('Число символов не должны быть равным 0, попробуйте еще раз.')
        else:   
            print(f'Нажмите "Enter", чтобы начать.')

        start = input('')
        a=0
        mistake = 0
        starttime=time.time()
        list_of_mist=[]


        while a != count:
            if count == 0:
                break
            display_litter = list_of_litters[rm.randint(0,len(list_of_litters)-1)] + list_of_litters[rm.randint(0,len(list_of_litters)-1)] + list_of_litters[rm.randint(0,len(list_of_litters)-1)]
            print(f'--> {display_litter}')
            print(' ')
            traning_print_value = input(str('Введите символ: '))
        
            if traning_print_value == display_litter:
                a+=1
            
            else:
                mistake += 1
                list_of_mist.append(display_litter)
                a+=1 
            print(' ')
            
        else:
            endtime=time.time()
            time_of_exirsize = endtime-starttime
            unic_list = list(set(list_of_mist))
            if count !=0:
                print(f'Кол-во тренировочных символов - {count}')
                print(f'Кол-во ошибок - {mistake} ({(mistake/count)*100}%)')
                print(f"Ваше время - {time_of_exirsize} сек.")
                if mistake > 0:
                    print('Ошибки:')
            for i in unic_list:
                if list_of_mist.count(i) == 1:
                    print(f"{i} - {list_of_mist.count(i)} раз")
                else:
                    print(f"{i} - {list_of_mist.count(i)} раза")
            time.sleep(10)
    except ValueError:
        print("Здесь нужно ввести число, попробуйте еще раз.")
        time.sleep(10)


def traning_upper_registr():
    spesial_symvols =str(""",'"[]{}./""")
    list_of_litters = string.ascii_uppercase
    # len_list_of_litters = len(list_of_litters)
    # print(len_list_of_litters)
    try:
        print('\n\n\n\n\nТренировка ввода одного символа вверхнего регистра.\n\n\n\n\n')
        count = int(input('Введите количество тренировочных символов:\n'))
        if count == 0:
            print('Число символов не должны быть равным 0, попробуйте еще раз.')
        else:   
            print(f'Нажмите "Enter", чтобы начать.')

        start = input('')
        a=0
        mistake = 0
        starttime=time.time()
        list_of_mist=[]


        while a != count:
            if count == 0:
                break
            display_litter = list_of_litters[rm.randint(0,len(list_of_litters)-1)]
            print(f'--> {display_litter}')
            print(' ')
            traning_print_value = input(str('Введите символ: '))
        
            if traning_print_value == display_litter:
                a+=1
            
            else:
                mistake += 1
                list_of_mist.append(display_litter)
                a+=1 
            print(' ')
            
        else:
            endtime=time.time()
            time_of_exirsize = endtime-starttime
            unic_list = list(set(list_of_mist))
            if count !=0:
                print(f'Кол-во тренировочных символов - {count}')
                print(f'Кол-во ошибок - {mistake} ({(mistake/count)*100}%)')
                print(f"Ваше время - {time_of_exirsize} сек.")
                if mistake > 0:
                    print('Ошибки:')
            for i in unic_list:
                if list_of_mist.count(i) == 1:
                    print(f"{i} - {list_of_mist.count(i)} раз")
                else:
                    print(f"{i} - {list_of_mist.count(i)} раза")
            time.sleep(10)
    except ValueError:
        print("Здесь нужно ввести число, попробуйте еще раз.")
        time.sleep(10)


def traning_special_symvol():
    spesial_symvols =str(""",'"[]{}./?!<>;:#%*&@-=+""")
    list_of_litters = string.ascii_lowercase
    # len_list_of_litters = len(list_of_litters)
    # print(len_list_of_litters)
    try:
        print('\n\n\n\n\nТренировка ввода одного специального символа.\n\n\n\n\n')
        count = int(input('Введите количество тренировочных символов:\n'))
        if count == 0:
            print('Число символов не должны быть равным 0, попробуйте еще раз.')
        else:   
            print(f'Нажмите "Enter", чтобы начать.')

        start = input('')
        a=0
        mistake = 0
        starttime=time.time()
        list_of_mist=[]


        while a != count:
            if count == 0:
                break
            display_litter = spesial_symvols[rm.randint(0,len(spesial_symvols)-1)]
            print(f'--> {display_litter}')
            print(' ')
            traning_print_value = input(str('Введите символ: '))
        
            if traning_print_value == display_litter:
                a+=1
            
            else:
                mistake += 1
                list_of_mist.append(display_litter)
                a+=1 
            print(' ')
            
        else:
            endtime=time.time()
            time_of_exirsize = endtime-starttime
            unic_list = list(set(list_of_mist))
            if count !=0:
                print(f'Кол-во тренировочных символов - {count}')
                print(f'Кол-во ошибок - {mistake} ({(mistake/count)*100}%)')
                print(f"Ваше время - {time_of_exirsize} сек.")
                if mistake > 0:
                    print('Ошибки:')
            for i in unic_list:
                if list_of_mist.count(i) == 1:
                    print(f"{i} - {list_of_mist.count(i)} раз")
                else:
                    print(f"{i} - {list_of_mist.count(i)} раза")
            time.sleep(10)
    except ValueError:
        print("Здесь нужно ввести число, попробуйте еще раз.")
        time.sleep(10)

def traning_english_words():
    english_list = []
    txtpass = input(str('Введите путь к файлу формата .txt со словами.\nПример для Ubuntu: /home/maks/Desktop/python/traning/word.txt \n')).strip()
    try:
        
        with open(txtpass, "r") as data:
            for row in data.readlines():
                english_list.append(row)



        try:
            print('\n\n\n\n\nТренировка ввода английских слов.\n\n\n\n\n')
            print(f'Количество слов в txt-файле = {len(english_list)},\nпри необходимости отредоктируйте.\n')
            count = int(input('Введите количество тренировочных символов:\n'))
            if count == 0:
                print('Число символов не должны быть равным 0, попробуйте еще раз.')
            else:   
                print(f'Нажмите "Enter", чтобы начать.')

            start = input('')
            a=0
            mistake = 0
            starttime=time.time()
            list_of_mist=[]

            
            while a != count:
                if count == 0:
                    break
                display_litter = english_list[rm.randint(0,len(english_list)-1)]
                print(f'--> {display_litter}')
                print(' ')
                traning_print_value = input(str('Введите символ: '))
            
                if traning_print_value == display_litter:
                    a+=1
                
                else:
                    mistake += 1
                    list_of_mist.append(display_litter)
                    a+=1 
                print(' ')
                
            else:
                endtime=time.time()
                time_of_exirsize = endtime-starttime
                unic_list = list(set(list_of_mist))
                if count !=0:
                    print(f'Кол-во тренировочных символов - {count}')
                    print(f'Кол-во ошибок - {mistake} ({(mistake/count)*100}%)')
                    print(f"Ваше время - {time_of_exirsize} сек.")
                    if mistake > 0:
                        print('Ошибки:')
                for i in unic_list:
                    if list_of_mist.count(i) == 1:
                        print(f"{i} - {list_of_mist.count(i)} раз")
                    else:
                        print(f"{i} - {list_of_mist.count(i)} раза")
                time.sleep(10)
        except ValueError:
            print("Здесь нужно ввести число, попробуйте еще раз.")
            time.sleep(10)
    except  FileNotFoundError:
        print('Тренировка слов недоступна, так как не подключен txt-файл. Проверьте путь к файлу и название файла.')
        time.sleep(10)

print('Введите "1" для начала тренировки ввода символов.\nВведите "2" для начала тренировки пар и троек символов.\nВведите "3" для начала тренировки букв верхнего регистра.\nВведите "4" для начала тренировки спецсимволов.\nВведите "5" для начала тренировки ввода английских слов.\n')
try:    
    level_choice = int(input(''))
    if level_choice == 1 :
        traning_one_symvol()
    if level_choice == 2 :
        traning_3_symvols()
    if level_choice == 3 :
        traning_upper_registr()
    if level_choice == 4 :
        traning_special_symvol() 
    if level_choice == 5 :
        traning_english_words()       

    if level_choice != 1 and level_choice != 2 and level_choice != 3 and level_choice != 4 and level_choice != 5:
        print("Вы не выбрали ни один из предложеных вариантов, попробуйте еще раз.")
        time.sleep(10)
except ValueError:
    print("Вы не выбрали ни один из предложеных вариантов, попробуйте еще раз.")
    time.sleep(10)

