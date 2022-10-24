delta = '\u03B4'
cap_delta = '\u03B4\u0302'
epsilon = '\u03B5'

def printFirstExtended(string):
    print('\n' + cap_delta + '(q0, ' + string + ')', end='\n\n')

def extended(start = '', finish = '', string = ''):
    parse = [string[:-1], string[-1]]

    if len(parse[0]) > 0:
        start += delta + '('
        finish = ', ' + parse[1] + ')' + finish
        print(start + cap_delta + '(q0, ' + parse[0] + ')' + finish, end='\n\n')
        extended(start, finish, parse[0])
    else:
        print(start + delta + '(' + cap_delta + '(q0, ' + epsilon + '), ' + parse[1] + ')' + finish, end='\n\n')

def printFirstResult(string):
    start = ''
    for char in string:
        start += delta + '('
    
    mid = 'q0, ' + string[0] + ')'

    finish = ''
    for char in string[1:]:
        finish += ', ' + char + ')'
    
    print(start + mid + finish, end = '\n\n')

def transition(string, start_state, finish_state, transitions):
    parse = [string[0], string[1:]]

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

        transition(parse[1], current_state, finish_state, transitions)

    else:

        current_state = transitions[(start_state, parse[0])]
        print(current_state, end ='\n\n')

        isAccepted(current_state, finish_state)
        

def isAccepted(lastState, finishState):
    if lastState in finishState:
        print('Status: STRING DITERIMA!')
    else:
        print('Status: STRING DITOLAK!')