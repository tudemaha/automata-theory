# nfa module import
from nfa import *

# main function
def __main__():
    # print program title
    print('===== PROGRAM PENGECEKAN STRING (NFA) =====', end = '\n\n')

    # define alphabets
    alphabets = {'0', '1'}

    # input string will be checked
    string = ''
    # while input string null, keep ask user to input string
    while string == '':
        print('Masukkan string untuk dicek: ', end = '')
        string = input()
    
    # check input string, if it contains non-alphabet member, finish program
    for char in string:
        if char not in alphabets:
            print('String yang dimasukkan bukan anggota alphabet')
            exit_message()

    # print menu to show NFA machine options
    print('\nPilihan mesin pengecekan:')
    print('1. String diawali dan diakhiri string yang sama')
    print('2. String diawali 1 dan jumlah 0 adalah kelipatan 3')
    print('3. String diawali 0 dan jumlah 1 adalah ganjil')

    # define accepted user choice
    accept_input = ('1', '2', '3')
    # if user choice isn't accepted, re-enter to insert choice
    while True:
        print('Masukkan pilihan: ', end = '')
        choice = input()
        if choice in accept_input:
            break
        else:
            print('Masukan tidak valid!\n')
    
    # print the first step of extended transition function
    print_first('q0')

    # if user choose option 1
    if choice == '1':
        # call transition fungtion, with its argument (related to 1st NFA machine)
        result = transition(string, 'q0', {'q3'}, {
            ('q0', '0'): {'q2', 'q3'},
            ('q0', '1'): {'q1', 'q3'},
            ('q1', '0'): {'q1'},
            ('q1', '1'): {'q1', 'q3'},
            ('q2', '0'): {'q2', 'q3'},
            ('q2', '1'): {'q2'}
        })

    # if user choose option 2
    elif choice == '2':
        # call transition fungtion, with its argument (related to 2nd NFA machine)
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
    # if user choose option 3
    elif choice == '3':
        # call transition fungtion, with its argument (related to 3rd NFA machine)
        result = transition(string, 'q0', {'q2'}, {
            ('q0', '0'): {'q1'},
            ('q1', '0'): {'q1'},
            ('q1', '1'): {'q2'},
            ('q2', '0'): {'q2'},
            ('q2', '1'): {'q1'}
        })

    # print checking result based on transition function's return value
    if result: print('Status: STRING DITERIMA')
    else: print('Status: STRING DITOLAK')

    # show exit message
    exit_message()


# function to show exit message and exit program
def exit_message():
    print('\n===== PROGRAM SELESAI =====')
    exit()

# call __main__ function to start program
__main__()