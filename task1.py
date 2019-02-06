from collections import defaultdict
def return_list():
    fin = open('running-config.cfg','r')
    lines = fin.readline()
    t = []
    for lines in fin:
        word = lines.split()
        if word[0] == 'interface':
           temp = ''
           temp = word[1]
        if word[0] == 'nameif':
           t.append((temp,word[1]))
        elif word[0] == 'no':
           t.append(temp)
    print(t)

return_list()

def list_ifname_ip():
    fin = open('running-config.cfg','r')
    lines = fin.readline()
    d = defaultdict(list)
    for lines in fin:
        word = lines.split()
        if word[0] == 'interface':
           key = ''
           key = word[1]
        if word[0] == 'vlan':
           d[key].append(word[1])
        if word[0] == 'nameif':
           d[key].append(word[1])
        if word[0] == 'ip':
           d[key].append(word[2])
           d[key].append(word[3])
    print(d)

list_ifname_ip()

