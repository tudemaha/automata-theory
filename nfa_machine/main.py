from nfa import *

def __main__():
    print('===== PROGRAM PENGECEKAN STRING (NFA) =====', end = '\n\n')

    alphabets = {'0', '1'}

    string = ''
    while string == '':
        print('Masukkan string untuk dicek: ', end = '')
        string = input()
    
    for char in string:
        if char not in alphabets:
            print('String yang dimasukkan bukan anggota alphabet')
            exit_message()

    print('\nPilihan mesin pengecekan:')
    print('1. String diawali dan diakhiri string yang sama')
    print('2. String diawali 1 dan jumlah 0 adalah kelipatan 3')
    print('3. String diawali 0 dan jumlah 1 adalah ganjil')

    accept_input = ('1', '2', '3')
    while True:
        print('Masukkan pilihan: ', end = '')
        choice = input()
        if choice in accept_input:
            break
        else:
            print('Masukan tidak valid!\n')
    
    print_first('q0')

    if choice == '1':
        result = transition(string, 'q0', {'q3'}, {
            ('q0', '0'): {'q2', 'q3'},
            ('q0', '1'): {'q1', 'q3'},
            ('q1', '0'): {'q1'},
            ('q1', '1'): {'q1', 'q3'},
            ('q2', '0'): {'q2', 'q3'},
            ('q2', '1'): {'q2'}
        })

    elif choice == '2':
        result = transition(string, 'q0', {'q4'}, {
            ('q0', '1'): {'q1'},
            ('q1', '0'): {'q2'},
            ('q1', '1'): {'q1'},
            ('q2', '0'): {'q3'},
            ('q2', '1'): {'q2'},
            ('q3', '0'): {'q4'},
            ('q3', '1'): {'q3'},
            ('q4', '0'): {'q2'},
            ('q4', '1'): {'q4'}
        })
    elif choice == '3':
        result = transition(string, 'q0', {'q2'}, {
            ('q0', '0'): {'q1'},
            ('q1', '0'): {'q1'},
            ('q1', '1'): {'q2'},
            ('q2', '0'): {'q2'},
            ('q2', '1'): {'q1'}
        })

    if result: print('Status: STRING DITERIMA')
    else: print('Status: STRING DITOLAK')

    exit_message()


def exit_message():
    print('\n===== PROGRAM SELESAI =====')
    exit()

    
__main__()