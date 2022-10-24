from checking import isMember

def insertString():
    string = ''
    while(string == ''):
        print('Masukkan string untuk dicek: ', end='')
        string = input()
    
    return string

def insertChoice():
    print('\nPilihan metode pengecekan:')
    print('1. Substring 101')
    print('2. Prefix 101')
    print('3. Suffix 101')

    while(True):
        print('Masukkan pilihan: ', end='')
        choice = input()
        accept_choice = ['1', '2', '3']

        if isMember(choice, ['1', '2', '3']):
            break
        else:
            print('Masukan tidak valid!\n')
    
    return choice