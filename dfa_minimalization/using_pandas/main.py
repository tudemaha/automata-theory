# import minimization module
from minimalization import minimal

# main function
def __main__():
    # program title
    print('===== DFA MINIMALIZATION =====')

    # list of DFA machine
    print("Pilihan mesin:")
    print('1. Mesin DFA I')
    print('2. Mesin DFA II')
    print('3. Mesin DFA III')

    # accpted user input
    accept = ('1', '2', '3')
    # user input, repeat if empty
    while(True):
        print('Masukkan pilihan: ', end = '')
        choice = input()
        if choice in accept: break
        else: print('Masukan tidak valid\n')

    # if user selects 1, minimize the first DFA machine
    if choice == '1':
        minimal('q0', {'q4'}, {'a', 'b'}, {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q2',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q3',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q2',
            ('q3', 'a'): 'q1',
            ('q3', 'b'): 'q4',
            ('q4', 'a'): 'q1',
            ('q4', 'b'): 'q2'
        })
    # if user selects 2, minimize the second DFA machine
    elif choice == '2':
        minimal('q0', {'q1', 'q2', 'q4'}, {'0', '1'}, {
            ('q0', '0'): 'q3',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q2',
            ('q1', '1'): 'q5',
            ('q2', '0'): 'q2',
            ('q2', '1'): 'q5',
            ('q3', '0'): 'q0',
            ('q3', '1'): 'q4',
            ('q4', '0'): 'q2',
            ('q4', '1'): 'q5',
            ('q5', '0'): 'q5',
            ('q5', '1'): 'q5',
        })
    # if user selects 3, minimize the third DFA machine
    elif choice == '3':
         minimal('q0', {'q3', 'q5'}, {'0', '1'}, {
            ('q0', '0'): 'q1',
            ('q0', '1'): 'q3',
            ('q1', '0'): 'q0',
            ('q1', '1'): 'q3',
            ('q2', '0'): 'q1',
            ('q2', '1'): 'q4',
            ('q3', '0'): 'q5',
            ('q3', '1'): 'q5',
            ('q4', '0'): 'q3',
            ('q4', '1'): 'q3',
            ('q5', '0'): 'q5',
            ('q5', '1'): 'q5',
        })

    # message to display program completed
    print('\n===== END OF PROGRAM =====')

# run __main__ function
__main__()