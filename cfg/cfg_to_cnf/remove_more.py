# import all required libraries
import re
from copy import deepcopy

# make capiral letter in regex form
capital = re.compile(r'[A-Z]')

# the real static
# remove more than 2 unit in production
def remove_more_two(cfg):
    # make a deepcopy of cfg
    temp_cfg = deepcopy(cfg)
    
    # empty set to store the new rule added
    used = []

    # iterate every rule in temp_cfg
    for i, row in enumerate(temp_cfg):
        # iterate every element in current rule's body
        for element in row[1]:
            # find all non terminal symbol in current element
            non_terminal = capital.findall(element)
            # if length of element more than 2 and number of non_terminal more than 2
            if len(element) > 2 and len(non_terminal) > 2:
                # transform the current element into list
                remove = list(element)
                # while number of index in list remove more than 2
                while(len(remove) > 2):
                    # remove the element from the current rule's body
                    cfg[i][1].remove(element)
                    # make new rule, the head is K and the body is first 2 char of current element
                    new = ['K', {''.join(remove[:2])}]
                    # if new rule not in used
                    if new not in used:
                        # append it to used list
                        used.append(new)
                    # replace first 2 index in remove list with K
                    remove[:2] = 'K'
                    # add the new element to the current rule's body
                    cfg[i][1].add(''.join(remove))
    
    # append all new rules in used list to cfg
    for use in used:
        cfg.append(use)