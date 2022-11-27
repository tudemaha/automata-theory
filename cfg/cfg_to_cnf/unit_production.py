import re

small = re.compile(r'[a-z]')
capital = re.compile(r'[A-Z]')

# remove the unit production
def remove_unit_production(cfg):
    one_non_terminal = find_non_terminal(cfg)
    remove_unit(one_non_terminal, cfg)
    remove_unaccessable(cfg)

    return cfg

# find one non terminal in body
def find_non_terminal(cfg):
    one_non_terminal = []

    for i, row, in enumerate(cfg):
        for element in row[1]:
            non_terminal = capital.findall(element)

            if len(element) == 1 and len(non_terminal) == 1:
                if i not in one_non_terminal:
                    one_non_terminal.append([i, element])

    return one_non_terminal

# remove the unit from cfg
def remove_unit(one_non_terminal, cfg):
    temp_body = []

    for i, index in enumerate(one_non_terminal):
        temp_body.append(set())

        cfg[index[0]][1].remove(index[1])
        for row in cfg:
            if row[0] == index[1]:
                temp_body[i] = temp_body[i].union(row[1])
        
    for i, index in enumerate(one_non_terminal):
        cfg[index[0]][1] = cfg[index[0]][1].union(temp_body[i])

# remove the unaccessable rules
def remove_unaccessable(cfg):
    terminal_in_body = set()

    for row in cfg:
        for element in row[1]:
            non_terminal = capital.findall(element)
            
            for non in non_terminal:
                terminal_in_body.add(non)
    
    to_remove = []
    for i, row in enumerate(cfg):
        for head in row[0]:
            if head not in terminal_in_body and '*' not in head:
                to_remove.append(i)
    
    for x in to_remove:
        del cfg[x]
