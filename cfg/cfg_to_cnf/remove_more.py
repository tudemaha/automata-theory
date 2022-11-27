import re
from copy import deepcopy

capital = re.compile(r'[A-Z]|α|β')

# the real static
# remove more than 2 unit in production
def remove_more_two(cfg):
    temp_cfg = deepcopy(cfg)
    
    used = []

    for i, row in enumerate(temp_cfg):
        for element in row[1]:
            non_terminal = capital.findall(element)
            if len(element) > 2 and len(non_terminal) > 2:
                remove = list(element)
                while(len(remove) > 2):
                    cfg[i][1].remove(element)
                    new = ['K', {''.join(remove[:2])}]
                    if new not in used:
                        used.append(new)
                    remove[:2] = 'K'
                    cfg[i][1].add(''.join(remove))
    
    for use in used:
        cfg.append(use)