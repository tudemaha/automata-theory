# import combintion function from itertools module
from itertools import combinations

# create empty list to store the remove null production from cfg
new_cfg = []

# remove the null production
def remove_null_production(cfg):
    # declare new_cfg as global variable
    global new_cfg
    # empty list to store the head contains null production
    heads = []
    
    # check every rules in cfg
    for row in cfg:
        # if the epsilon appear in the body of rule
        if 'ε' in row[1]:
            # append the head of the rule to heads list
            heads.append(row[0])
    
    # function to create empty list with the same number of index as the cfg
    create_empty_new_cfg(cfg)
    # function to create new cfg without null production
    create_new_cfg(heads, cfg)
    # function to remove the empty index of new_cfg (index of rule that only has epsilon in body)
    remove_empty_index(new_cfg)

    # return the cfg without null production
    return new_cfg


# create new empty list based on cfg index
def create_empty_new_cfg(cfg):
    # declare new_cfg from the global variable
    global new_cfg

    # append the empty rules to the new_cfg based on number of index from cfg
    for _ in cfg:
        new_cfg.append(['', set()])

# create new cfg without null production (using combination)
def create_new_cfg(null_heads, cfg):
    # declare new_cfg from the global variable
    global new_cfg

    # iterate all the heads in null_heads list (head that contain epsilon)
    for head in null_heads:
        # iterate every rule in cfg
        for index, row in enumerate(cfg):
            # create empty set to store the body of the current rule
            new_body = set()
            # iterate all elements in body of the current rule
            for element in row[1]:
                # skip the iteration if the current element is epsilon (so the epsilon not stored in new_body)
                if element == 'ε': continue

                # add current element (not epsilon) to new_body
                new_body.add(element)

                # if the head contains epsilon appear in current element
                if head in element:
                    # make empty list to store the index of every char in element that contains the head
                    index_contain_head = []
                    # iterate every char in element
                    for i, char in enumerate(element):
                        # if the current char is the head
                        if char == head:
                            # append the index into index_contain_head list
                            index_contain_head.append(i)
                    
                    # empty list to store the index of eleemnt contains head
                    remove_combination = []
                    # do iteration from 1 to n (number of element in list index_contain_head)
                    for i in range(1, len(index_contain_head) + 1):
                        # iteration to get all the possible combinatin of number of index
                        for sub in combinations(index_contain_head, i):
                            # append the combination to list remove_combination
                            remove_combination.append(sub)

                    # remove the char of current element based on the combination
                    for remove in remove_combination:
                        # transform the current element from string to list
                        edit_element = list(element)
                        # iterate all the current combination
                        for x in remove:
                            # remove the char based on combination
                            edit_element[x] = ''
                        # add new element from combination to new_body (transform it into string back)
                        new_body.add(''.join(edit_element))

                # append the current head in iteration to new_cfg
                new_cfg[index][0] = row[0]
                # append the union of old body in cfg with the new body (after combination)
                new_cfg[index][1] = new_cfg[index][1].union(new_body)
        


# remove the empty index in new cfg
def remove_empty_index(cfg):
    # iterate every rule in cfg
    for row in cfg:
        # if the rule is empty (in ['', set()] form)
        if row == ['', set()]:
            # delete the empty rule
            del cfg[cfg.index(row)]