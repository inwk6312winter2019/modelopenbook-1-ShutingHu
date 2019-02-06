def create_list():
    fin = open('running-config.cfg')
    line = fin.readline()
    l = []
    for line in fin:
        word = line.split()
        if word[0] == 'access-list':
           if word[1] == 'global_access':
              l.append(line)
           elif word[1] == 'fw-management_access_in':
              l.append(line)
    print(l)
create_list()

