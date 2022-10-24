from menu.printing import *
from menu.insert import *
from checking import isMember
from dfa import *

def __main__():
    printTitle()

    alphabets = ['0', '1']

    string = insertString()

    if not isMember(string, alphabets):
        print('String yang dimasukkan bukan anggota alphabet')
        finish_message()
        exit()

    choice = insertChoice()

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

__main__()