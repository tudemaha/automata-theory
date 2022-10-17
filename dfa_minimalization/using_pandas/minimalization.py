from email import message
import pandas as pd

epsilon = '\u03B5'
empty = '\u2205'
sigma = '\u03a3'
delta = '\u03B4'

def minimal(start_state, final_states, alphabets, transitions):
    global filledTable
    state_count = int(len(transitions) / 2)

    table, states = [], []
    for i in range(state_count):
        table.append([])
        states.append('q' + str(i))
        for j in range(state_count):
            if j >= i:
                table[i].append(empty)
            else:
                table[i].append('')

    print('Before:')
    result_message(states, alphabets, start_state, final_states, transitions)

    table = pd.DataFrame(table, index = states, columns = states)
    table = fillingEpsilon(table, states, final_states)

    fillingTable(table, alphabets, transitions)
    
    new_transitions = minimalization(filledTable, states, transitions)
    
    new_states = set()
    for transition in new_transitions:
        new_states.add(transition[0])
    
    new_start = start_state
    for state in new_states:
        if start_state in state.split('/'):
            new_start = state
            break

    new_final = set()
    for final in final_states:
        for state in new_states:
            if final in state.split('/'):
                new_final.add(state)
                break
        
    print('After:')
    result_message(new_states, alphabets, new_start, new_final, new_transitions)




def fillingEpsilon(table, states, final_states):
    print(table)
    for final in final_states:
        for state in states:
            if state not in final_states:
                if table[state][final] == '':
                    table[state][final] = epsilon
                else:
                    table[final][state] = epsilon
    print(table)
    return table


def fillingTable(table, alphabets, transitions):
    global filledTable
    new_table = table.copy()
    change = False

    for row in table:
        for column in table:
            if table[column][row] == '':
                result = ['', '']
                for alphabet in alphabets:
                    result[0] = transitions[(row, alphabet)]
                    result[1] = transitions[(column, alphabet)]
                    if (table[result[0]][result[1]] != '' and table[result[0]][result[1]] != empty) or (table[result[1]][result[0]] != '' and table[result[1]][result[0]] != empty):
                        new_table[column][row] = alphabet
                        change = True
                        break
    
    print(new_table)

    if change: fillingTable(new_table, alphabets, transitions)
    else: filledTable = new_table


def minimalization(filledTable, states, transitions):
    new_transitions = {}

    useless = []
    for column in states:
        for row in states:
            if filledTable[column][row] == '':
                useless.append((column, row))
    
    if len(useless) == 0:
        print('DFA cannot be minimized')
        exit()

    useless = useless_combine(useless)
    
    for key, value in transitions.items():
        new_key, new_value = -1, -1
        for i, pair in enumerate(useless):
            if key[0] in pair: new_key = i
            if value in pair: new_value = i
        
        if new_key != -1: domain = ('/'.join(useless[new_key]), key[1])
        else: domain = key

        if new_value != -1: codomain = '/'.join(useless[new_value])
        else: codomain = value

        new_transitions[domain] = codomain

    return new_transitions

def useless_combine(useless):
    new_useless = []
    for key in useless:
        combine = set(key)
        for element in useless:
            if key == element: continue
            if key[0] in element or key[1] in element:
                combine.update(element)
                useless.pop(useless.index(element))
        new_useless.append(tuple(combine))
        useless.pop(useless.index(key))
    
    return new_useless

def result_message(states, alphabets, start_state, final_states, transitions):
    print('Detailed description:')
    print(f'- Q = {states},')
    print(f'- {sigma} = {alphabets},')
    print(f'- Start state: {start_state},')
    print(f'- Set of final state: {final_states},')
    print(f'- {delta} : Q x {sigma} --> where:')
    
    for key, value in transitions.items():
        print(f'\t{delta}{key} = {value}')

