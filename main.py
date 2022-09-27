from dfa import *

def __main__():
    print('===== PROGRAM PENGECEKAN STRING =====', end='\n\n')

    alphabets = ['0', '1']

    string = ''
    while(string == ''):
        print('Masukkan string untuk dicek: ', end='')
        string = input()


    for char in string:
        if char not in alphabets:
            print('String yang dimasukkan bukan anggota alphabet')
            finish_message()
            exit()

    print('\nPilihan metode pengecekan:')
    print('1. Substring 101')
    print('2. Prefix 101')
    print('3. Suffix 101')

    while(True):
        print('Masukkan pilihan: ', end='')
        choice = input()
        accept_choice = ['1', '2', '3']
        if choice in accept_choice:
            break
        else:
            print('Masukan tidak valid!\n')

    printFirstExtended(string)
    extended(string = string)
    printFirstResult(string)

    if choice == '1':
        transition(string, 'q0', ['q3'], {
            ('q0', '0'): 'q0',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q2',
            ('q1', '1'): 'q1',
            ('q2', '0'): 'q0',
            ('q2', '1'): 'q3',
            ('q3', '0'): 'q3',
            ('q3', '1'): 'q3'
        })

    elif choice == '2':
        transition(string, 'q0', ['q3'], {
            ('q0', '0'): 'q4',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q2',
            ('q1', '1'): 'q4',
            ('q2', '0'): 'q4',
            ('q2', '1'): 'q3',
            ('q3', '0'): 'q3',
            ('q3', '1'): 'q3',
            ('q4', '0'): 'q4',
            ('q4', '1'): 'q4'
        })

    elif choice == '3':
        transition(string, 'q0', ['q3'], {
            ('q0', '0'): 'q0',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q2',
            ('q1', '1'): 'q1',
            ('q2', '0'): 'q0',
            ('q2', '1'): 'q3',
            ('q3', '0'): 'q2',
            ('q3', '1'): 'q1'
        })
    
    finish_message()

def finish_message():
    print('\n===== PROGRAM SELESAI =====')

__main__()