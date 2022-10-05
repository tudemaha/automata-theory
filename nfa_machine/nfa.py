# variables to store Greek and math symbols
delta = '\u03B4'
cap_delta = '\u03B4\u0302'
epsilon = '\u03B5'
union = '\u222a'
empty = '\u2205'

# print first NFA extended transition function
def print_first(start_state):
    print('\n' + cap_delta + '(' + start_state + ', ' + epsilon + ') = {' + start_state + '}', end = '\n\n')
    
# NFA computation and print step by step to terminal
def transition(string, start_state, finish_state, transitions):
    # store current state(s) will be checked, starting from start state
    current_state = {start_state}
    # make start pattern to print in terminal
    start = cap_delta + '(' + start_state

    # for loop to check each alphabet in string
    for i in range(len(string)):
        # list of result from current checking result
        result = []
        # current string to process (for print and for extended transition function)
        current_string = string[:i + 1]
        # add start pattern with current string
        start += ', ' + current_string + ') '

        # iterate current state(s) with current alphabet
        for i, element in enumerate(current_state):
            # add to start pattern by order of iteration (if first, use '=' else use union symbol)
            if i == 0:
                start += '= ' + delta + '(' + element + ', ' + current_string[-1] + ') '
            else:
                start += union + ' ' + delta + '(' + element + ', ' + current_string[-1] + ') '
            
            # [core process of NFA]
            # if combination of current alphabet and current state(s) available in transition function
            # append the result to 'result' variable
            if (element, current_string[-1]) in transitions:
                result.append(transitions[(element, current_string[-1])])
                # make mid pattern to print (if first, use '=' else use union symbol)
                if i == 0:
                    mid = '= ' + str(transitions[(element, current_string[-1])]) + ' '
                else:
                    mid += union + ' ' + str(transitions[(element, current_string[-1])]) + ' '
            # if the combination not found in transition function
            else:
                # do nothing to 'result' variable, just add mid pattern
                if i == 0:
                    mid = '= ' + empty + ' '
                else:
                    mid += union + ' ' + empty + ' '
        
        # update current_state with union of the result of current checking
        # used for next checking
        current_state = set().union(*result)

        # finish pattern based on number of element of current_state
        if len(current_state) != 0:
            finish = '= ' + str(current_state) + ' '
        else:
            finish = '= ' + empty + ' '

        # if mid pattern and finish pattern isn't the same
        if mid != finish:
            # print start, mid, and finish pattern
            print(start + mid + finish, end = '\n\n')
        else:
            # just print start and mid pattern
            print(start + mid, end = '\n\n')
        
        # if number of element(s) in curent_state equal to 0 (death state)
        # break from alphabet looping (string not accepted)
        if len(current_state) == 0: break

        # reset start pattern
        start = cap_delta + '(' + start_state

    # after iteration, if intersection of current_state and finish_state
    # not null, return true (string accepted) else return false
    if len(current_state.intersection(finish_state)):
        return True
    else:
        return False