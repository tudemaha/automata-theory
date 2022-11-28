# import the required library
import re

# regex for all small letters
small = re.compile(r'[a-z]')
# regex for all capital letters
capital = re.compile(r'[A-Z]')

# remove the unit production
def remove_unit_production(cfg):
    # find all the body of rule contain just one non terminal symbol
    one_non_terminal = find_non_terminal(cfg)
    # remove the unit productino based on index of rule contain unit production
    remove_unit(one_non_terminal, cfg)
    # remove the unacessable rule
    remove_unaccessable(cfg)

    # return the cfg with no unit production
    return cfg

# find one non terminal in body
def find_non_terminal(cfg):
    # make empty list to store the information of rule contain unit production
    # form -> [index of rule, the unit production]
    one_non_terminal = []

    # iterate every rule in cfg
    for i, row, in enumerate(cfg):
        # iterate every element in body of current rule
        for element in row[1]:
            # count all non terminal (capital letter) appear in current element
            non_terminal = capital.findall(element)

            # if the length of element is equal to 1 and count of all capital letters is 1
            # (contain unit production)
            if len(element) == 1 and len(non_terminal) == 1:
                # if the index of rule contain unit production not listed yet
                if i not in one_non_terminal:
                    # append the index and element to one_non_terminal list
                    one_non_terminal.append([i, element])

    # return one_non_terminal
    return one_non_terminal

# remove the unit from cfg
def remove_unit(one_non_terminal, cfg):

    # iterate all information in one_non_terminal list
    for index in one_non_terminal:
        # make empty set to store the body of the unit terminal on the other rule
        temp_body = set()

        # remove the unit production in cfg
        cfg[index[0]][1].remove(index[1])
        # iterate every rules in cfg
        for row in cfg:
            # if the head of current rule is equal to unit production
            if row[0] == index[1]:
                # union the temp_body with the body of current rule
                temp_body = temp_body.union(row[1])
    
        # union the body of cfg contain unit production with temp_body
        cfg[index[0]][1] = cfg[index[0]][1].union(temp_body)

# remove the unaccessable rules
def remove_unaccessable(cfg):
    # empty set to store all non terminal symbol appear in body
    non_terminal_in_body = set()

    # iterate all rule in cfg
    for row in cfg:
        # iterate all element in current rule
        for element in row[1]:
            # find all non terminal symbol appear in current element
            non_terminal = capital.findall(element)
            
            # iterate all non terminal symbol in non_terminal
            for non in non_terminal:
                # add all the non terminal in non_terminal_in_body set
                non_terminal_in_body.add(non)
    
    # empty list to store the index of rule to be removed
    to_remove = []
    # iterate every rule in cfg
    for i, row in enumerate(cfg):
        # if the head not in non_terrmnal_in_body and no * symbol in head
        if row[0] not in non_terminal_in_body and '*' not in row[0]:
            # the rule is not accessable, so list the index
            to_remove.append(i)
    
    # iterate all index to remove
    for x in to_remove:
        # delete the index of unaccessable rule
        del cfg[x]