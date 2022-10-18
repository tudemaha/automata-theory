# import pandas to make DataFrame
import pandas as pd

# variables to store Greek and math symbols
epsilon = '\u03B5'
empty = '\u2205'
sigma = '\u03a3'
delta = '\u03B4'

# minimalization logic
def minimal(start_state, final_states, alphabets, transitions):
    # global variabel for filling table
    global filledTable
    # number of state from transitions
    state_count = int(len(transitions) / 2)

    # create state elements from q0 to qn
    states = []
    for i in range(state_count):
        states.append('q' + str(i))

    # show detailed description from unminimized DFA
    print('\n--->> BEFORE <<---')
    result_message(states, alphabets, start_state, final_states, transitions)

    # make new state by removing inaccessable state(s)
    states = removeState(transitions, start_state)
    # sort the new states in ascending mode
    states.sort()

    # preparation to create a filling table by declare empty list
    table = []
    # create (states x states) table
    for i in range(len(states)):
        table.append([])
        for j in range(len(states)):
            # fill the upper triangular table by empty symbol
            if j >= i:
                table[i].append(empty)
            # fill the lower triangular by null string
            else:
                table[i].append('')

    # create a dataframe from table before and named its index and columns with state's name
    table = pd.DataFrame(table, index = states, columns = states)
    # fill the table by epsilon (0's iteration) by call fillingEpsilon function
    table = fillingEpsilon(table, states, final_states)

    # loop the table to add checking status
    fillingTable(table, alphabets, transitions)
    
    # make new transitions from the latest table (after minimized)
    new_transitions = minimalization(filledTable, states, transitions)
    
    # make new states to use in detailed description (after minimized)
    new_states = set()
    for transition in new_transitions:
        new_states.add(transition[0])
    
    # make new starting state name (for the minimized DFA)
    new_start = start_state # default use the old name if there's no change
    for state in new_states:
        if start_state in state.split('/'):
            new_start = state
            break

    # make new final state(s) name (for the minimized DFA)
    new_final = set()
    for final in final_states:
        for state in new_states:
            if final in state.split('/'):
                new_final.add(state)
                break
    
    # show detailed description from minimized DFA
    print('\n--->> AFTER <<---')
    result_message(new_states, alphabets, new_start, new_final, new_transitions)


# remove inaccessable state(s)
def removeState(transitions, start_state):
    # start with states's change status true
    change = True

    # iterate until no inaccessable state(s)
    while(change):
        # meake empty set to store accessable state(s)
        used_states = set()
        # always store start state, although no state(s) access it
        used_states.add(start_state)
        # change status to false to indicate no change occur
        change = False
        # add codomain of transition function to accessable set
        for key, value in transitions.items():
            used_states.add(value)

        # list of domain from deleted transition function
        delete = []
        # iterate all transition function
        for key in transitions:
            # if the state in domain is inaccessable, append it to delete list
            if key[0] not in used_states:
                delete.append(key)
        
        # iterate all key in delete list
        for key in delete:
            # delete transition function with the appropriate key in delete list
            del transitions[key]
            # change status to true cause there was some deletions
            change = True
    
    # if no change in state (change == false)
    if not change:
        # create new set of state
        new_states = set()
        # iterate and add all domain's state in transition function
        for key in transitions:
            new_states.add(key[0])
    # return new states
    return list(new_states)

# 0's iteration to fill epsilon in filling table
def fillingEpsilon(table, states, final_states):
    # print starting message and empty lower triangular filling table
    print('\n--->> FILLING TABLE <<---')
    print(table)

    # iterate final state
    for final in final_states:
        # iterate all state
        for state in states:
            # if one state in final state and the other isn't or vice versa
            if state not in final_states:
                # fill epsilon in the empty lower triangular filling table
                if table[state][final] == '':
                    table[state][final] = epsilon
                else:
                    table[final][state] = epsilon
    
    # show table after filling
    print(table)
    # return table
    return table

# filling table with appropriate alphabet
def fillingTable(table, alphabets, transitions):
    # global variable for filled table
    global filledTable
    # copy filling table to fill with alphabet
    new_table = table.copy()
    # first, make status of changed filling table is false
    change = False

    # iterate index of table as row
    for row in table:
        # iterate index of table as column
        for column in table:
            # check if the cell in table is empty
            if table[column][row] == '':
                # prepare list with two empty element to store destination state
                result = ['', '']
                # iterate alphabet
                for alphabet in alphabets:
                    # search of destinations of state in current cell
                    result[0] = transitions[(row, alphabet)]
                    result[1] = transitions[(column, alphabet)]
                    # if the cell of these destinations are empty and not located in upper triangular
                    if (table[result[0]][result[1]] != '' and table[result[0]][result[1]] != empty) or (table[result[1]][result[0]] != '' and table[result[1]][result[0]] != empty):
                        # fill appropriate alphabet in current cell
                        new_table[column][row] = alphabet
                        # because there's a change in table, turn status to true and break
                        change = True
                        break
    
    # print new table (after filled)
    print(new_table)

    # if tabled changed, run recursive
    if change: fillingTable(new_table, alphabets, transitions)
    # if no change, assign lates new table to filledTable
    else: filledTable = new_table

# minimization process of DFA
def minimalization(filledTable, states, transitions):
    # prepare empty dictionary for new transition function
    new_transitions = {}

    # prepare empty list to store states that can be merged
    useless = []
    # iterate states as column
    for column in states:
        # iterate states as row
        for row in states:
            # if there's an empty cell in filling table
            if filledTable[column][row] == '':
                # append the pair of states in empty cell to useless list as tuple
                useless.append((column, row))
    
    # if no pair in useless
    if len(useless) == 0:
        # show message that the DFA can't be minimized and exit program
        print('DFA cannot be minimized')
        exit()

    # update useless list with combination of state's pair to be a new name for a state
    useless = useless_combine(useless)
    
    # iterate old transition functions
    for key, value in transitions.items():
        # set -1 to mark no state(s) to merge
        new_key, new_value = -1, -1
        # iterate index and element in useless list
        for i, pair in enumerate(useless):
            # if state in domain is at pair (useless element), mark with index of pair
            if key[0] in pair: new_key = i
            # if state in codomain is at pair, mark with index of pair
            if value in pair: new_value = i
        
        # if state in domain merged, set the domain's state with state's combination as new name
        if new_key != -1: domain = ('/'.join(useless[new_key]), key[1])
        # else, just use the old domain
        else: domain = key

        # if state in codimain merged, set the codomain's state with state's combination as new name
        if new_value != -1: codomain = '/'.join(useless[new_value])
        #else, just use the old codomain
        else: codomain = value

        # insert new domain and codomain to new transition functions
        new_transitions[domain] = codomain

    # return new transition functions
    return new_transitions

# combine the state from empty cell in table
def useless_combine(useless):
    # prepare new empty list to store combined states
    new_useless = []

    # for every pair in useless list
    for key in useless:
        # combine set to store the combination
        combine = set(key)
        # iterate every element in useless list
        for element in useless:
            # if the key and element is the same, just continue, it's the same elememt
            if key == element: continue
            # if the key is in element of useless list
            if key[0] in element or key[1] in element:
                # update combine set with the element
                combine.update(element)
                # remove the merged element
                useless.pop(useless.index(element))
        # update new_useless with set of combine (converted to tuple)
        new_useless.append(tuple(combine))
    # return the new_useless (contain all the new states)
    return new_useless

# print the detailed description of DFA
def result_message(states, alphabets, start_state, final_states, transitions):
    print('Detailed description:')
    print(f'- Q = {states},')
    print(f'- {sigma} = {alphabets},')
    print(f'- Start state: {start_state},')
    print(f'- Set of final state: {final_states},')
    print(f'- {delta} : Q x {sigma} --> where:')
    
    # iterate transitions to print them in a vertical order
    for key, value in transitions.items():
        print(f'\t{delta}{key} = {value}')
        