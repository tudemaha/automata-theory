# function to join the same head in cfg into one rule
def join(cfg):
    # create a empty list to store the cfg
    new_cfg = []

    # check for every rules in cfg
    for row in cfg:
        # check for every rules in new_cfg
        for j, line in enumerate(new_cfg):
                # if row[0] (head) in cfg appear in head of new_cfg
                if row[0] in line[0]:
                    # union the body of the current new_cfg with the body of old cfg
                    new_cfg[j][1] = new_cfg[j][1].union(row[1])
                    break
        # if the head not appear (end of iteration)
        else:
            # just append the rule of old cfg to new_cfg
            new_cfg.append([row[0], row[1]])
    
    # return the new form of cfg
    return new_cfg
