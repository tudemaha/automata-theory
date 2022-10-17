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

    print('After:')
    result_message(states, alphabets, start_state, final_states, new_transitions)


def fillingEpsilon(table, states, final_states):
    for final in final_states:
        for state in states:
            if state not in final:
                table[state][final] = epsilon
    
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


    for key, value in transitions.items():
        for pair in useless:
            new_state = '/'.join(pair)
            if key[0] in pair:
                domain = (new_state, key[1])
                if value in useless:
                    codomain = new_state
                else:
                    codomain = value
                new_transitions[domain] = codomain
            elif value in pair:
                new_transitions[key] = new_state
            else:
                new_transitions[key] = value
    
    return new_transitions


def result_message(states, alphabets, start_state, final_states, transitions):
    print('Detailed description:')
    print(f'- Q = {states},')
    print(f'- {sigma} = {alphabets},')
    print(f'- Start state: {start_state},')
    print(f'- Set of final state: {final_states},')
    print(f'- {delta} : Q x {sigma} --> where:')
    
    for key, value in transitions.items():
        print(f'\t{delta}{key} = {value}')

