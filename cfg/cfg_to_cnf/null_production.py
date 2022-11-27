from itertools import combinations

new_cfg = []

# remove the null production
def remove_null_production(cfg):
    global new_cfg
    heads = []
    
    for row in cfg:
        if 'ε' in row[1]:
            heads.append(row[0])
    
    create_empty_new_cfg(cfg)
    create_new_cfg(heads, cfg)
    remove_empty_index(new_cfg)

    return new_cfg


# create new empty list based on cfg index
def create_empty_new_cfg(cfg):
    global new_cfg

    for _ in cfg:
        new_cfg.append(['', set()])

# create new cfg without null production (using combination)
def create_new_cfg(null_heads, cfg):
    global new_cfg

    for head in null_heads:
        for index, row in enumerate(cfg):
            new_body = set()
            for element in row[1]:
                if element == 'ε': continue

                new_body.add(element)

                if head in element:
                    index_contain_head = []
                    for i, char in enumerate(element):
                        if char == head:
                            index_contain_head.append(i)
                    
                    remove_combination = []
                    for i in range(1, len(index_contain_head) + 1):
                        for sub in combinations(index_contain_head, i):
                            remove_combination.append(sub)

                    for remove in remove_combination:
                        edit_element = list(element)
                        for x in remove:
                            edit_element[x] = ''
                        new_body.add(''.join(edit_element))

                new_cfg[index][0] = row[0]
                new_cfg[index][1] = new_cfg[index][1].union(new_body)
        


# rwmove the empty index in new cfg
def remove_empty_index(cfg):
    for row in cfg:
        if row == ['', set()]:
            del cfg[cfg.index(row)]