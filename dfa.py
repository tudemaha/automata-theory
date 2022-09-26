delta = '\u03B4'
cap_delta = '\u03B4\u0302'
epsilon = '\u03B5'

def printFirstExtended(string):
    print('\n' + cap_delta + '(q0, ' + string + ')', end='\n\n')

def printFirstResult(string):
    start = ''
    for char in string:
        start += delta + '('
    
    mid = 'q0, ' + string[0] + ')'

    finish = ''
    for char in string[1:]:
        finish += ', ' + char + ')'
    
    print(start + mid + finish, end = '\n\n')

def extended(start = '', finish = '', string = ''):
    parse = [string[:-1], string[-1]]

    if len(parse[0]) > 0:
        start += delta + '('
        finish = ', ' + parse[1] + ')' + finish
        print(start + cap_delta + '(q0, ' + parse[0] + ')' + finish, end='\n\n')
        extended(start, finish, parse[0])
    else:
        print(start + delta + '(' + cap_delta + '(q0, ' + epsilon + '), ' + parse[-1] + ')' + finish, end='\n\n')

def substring(string, start_state = 'q0'):
    parse = [string[0], string[1:]]
    finish_state = ['q3']
    transitions = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q1',
        ('q2', '0'): 'q0',
        ('q2', '1'): 'q3',
        ('q3', '0'): 'q3',
        ('q3', '1'): 'q3',
    }

    if parse[1] != '':

        current_state = transitions[start_state, parse[0]]

        start = ''
        for char in parse[1]:
            start += delta + '('
        
        mid = current_state + ', ' + parse[1][0] + ')'

        finish = ''
        for char in parse[1][1:]:
            finish += ', ' + char + ')'
        
        print(start + mid + finish, end = '\n\n')

        substring(parse[1], current_state)

    else:

        current_state = transitions[(start_state, parse[0])]
        print(current_state, end ='\n\n')

        if current_state in finish_state:
            print('STRING DITERIMA!')
        else:
            print('STRING DITOLAK!')