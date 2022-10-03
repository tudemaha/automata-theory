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
    
    if choice == '1':
        print('ini satu')
    elif choice == '2':
        print('ini 2')
    elif choice == '3':
        print('ini 3')

    exit_message()


def exit_message():
    print('\n===== PROGRAM SELESAI =====')
    exit()

    
__main__()