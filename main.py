from dfa import *

def __main__():
    print('===== PROGRAM PENGECEKAN STRING =====', end='\n\n')

    alphabets = ['0', '1']

    print('Masukkan string untuk dicek: ', end='')
    string = input()

    for char in string:
        if char not in alphabets:
            print('String yang dimasukkan bukan anggota alphabet')
            finish_message()
            exit()

    while(True):
        print('\nPilihan metode pengecekan:')
        print('1. Substring 101')
        print('2. Prefix 101')
        print('3. Suffix 101')
        print('Masukkan pilihan: ', end='')

        choice = input()
        accept_choice = ['1', '2', '3']
        if choice in accept_choice:
            break
        else:
            print('Masukan tidak valid!')

    match choice:
        case '1':
            printFirstExtended(string)
            extended(string = string)
            printFirstResult(string)
            substring(string)
        case '2':
            print('ini ')
        case '3':
            print('ini suffix')
    
    finish_message()

def finish_message():
    print('\n===== PROGRAM SELESAI =====')

__main__()