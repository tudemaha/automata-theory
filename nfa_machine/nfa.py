delta = '\u03B4'
cap_delta = '\u03B4\u0302'
epsilon = '\u03B5'
union = '\u222a'
empty = '\u2205'

def print_first(start_state):
    print('\n' + cap_delta + '(' + start_state + ', ' + epsilon + ') = {' + start_state + '}', end = '\n\n')
    

def transition(string, start_state, finish_state, transitions):
    current_state = {start_state}
    start = cap_delta + '(' + start_state

    for i in range(len(string)):
        result = []
        current_string = string[:i + 1]
        start += ', ' + current_string + ') '

        for i, element in enumerate(current_state):
            if i == 0:
                start += '= ' + delta + '(' + element + ', ' + current_string[-1] + ') '
            else:
                start += union + ' ' + delta + '(' + element + ', ' + current_string[-1] + ') '
            
            if (element, current_string[-1]) in transitions:
                result.append(transitions[(element, current_string[-1])])
                if i == 0:
                    mid = '= ' + str(transitions[(element, current_string[-1])]) + ' '
                else:
                    mid += union + ' ' + str(transitions[(element, current_string[-1])]) + ' '
            else:
                if i == 0:
                    mid = '= ' + empty + ' '
                else:
                    mid += union + ' ' + empty + ' '
            
        current_state = set().union(*result)

        if len(current_state) != 0:
            finish = '= ' + str(current_state) + ' '
        else:
            finish = '= ' + empty + ' '

        if mid != finish:
            print(start + mid + finish, end = '\n\n')
        else:
            print(start + mid, end = '\n\n')
        
        start = cap_delta + '(' + start_state

    if len(current_state.intersection(finish_state)):
        return True
    else:
        return False