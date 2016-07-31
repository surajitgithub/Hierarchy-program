child = input()
gen_no = input()
list = []
e_d='e'
def right_left (child):
    if (child %2 ==0):
        list.append('r')
        child= child/2
    else:
        list.append('l')
        child = child+1
        child = child /2

    if child!=1:
        right_left(child)

right_left(child)
i = len(list) - 1
while(i>=0):
    if e_d == 'e':
        if list[i]=='r':
            e_d='d'
        else:
            e_d = 'e'
    else:
        if list[i]=='l':
            e_d='d'
        else:
            e_d = 'e'
    i = i-1


print e_d
