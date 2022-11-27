def join(cfg):
    new_cfg = []

    for row in cfg:
        for j, line in enumerate(new_cfg):
                if row[0] in line[0]:
                    new_cfg[j][1] = new_cfg[j][1].union(row[1])
                    break
        else:
            new_cfg.append([row[0], row[1]])
    
    return new_cfg
