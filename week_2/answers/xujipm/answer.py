# codeing: utf-8
# authon: xujipm


import time


def twenty_four(nlist, strlist):
    global total
    global ans
    if len(nlist) == 1:
        strlist[0] = strlist[0][1:-1]
        if nlist[0] == 24 and strlist[0] not in total:
            total.add(strlist[0])
            outputfile.write(u'%s\n' % (strlist[0]))
    else:
        for i in range(len(nlist) - 1):
            twenty_four(nlist[:i]+[nlist[i]+nlist[i+1]]+nlist[i+2:],
                        strlist[:i]+['('+strlist[i]+'+'+strlist[i+1]+')'] +
                        strlist[i+2:])
            twenty_four(nlist[:i]+[nlist[i]-nlist[i+1]]+nlist[i+2:],
                        strlist[:i]+['('+strlist[i]+'-'+strlist[i+1]+')'] +
                        strlist[i+2:])
            twenty_four(nlist[:i]+[nlist[i]*nlist[i+1]]+nlist[i+2:],
                        strlist[:i]+['('+strlist[i]+'*'+strlist[i+1]+')'] +
                        strlist[i+2:])
            if nlist[i+1] != 0 and nlist[i] % nlist[i+1] == 0:
                twenty_four(nlist[:i]+[nlist[i]/nlist[i+1]]+nlist[i+2:],
                            strlist[:i]+['('+strlist[i]+'/'+strlist[i+1]+')'] +
                            strlist[i+2:])


def twenty_four_calc(filename="24_data.txt"):
    global outputfile
    global total
    global ans
    n = 0

    for line in open(filename):
        total = set()
        line = line.replace('\n', '')
        n = n + 1
        outputfile.write(u'===%s\n' % (line))
        line = line.replace('A', '1')
        line = line.replace('J', '11')
        line = line.replace('Q', '12')
        line = line.replace('K', '13')
        num = line.split(' ')
        twenty_four([int(x) for x in num], num)
        if len(total) == 0:
            outputfile.write(u'Impossible\n\n')
            pass
        else:
            outputfile.write(u'\n')
    pass


t1 = time.time()
print('start time:\t', time.ctime())


total = set()
ans = ''
outputfile = open('24_answer_xujipm.txt', mode='w', buffering=-1)

twenty_four_calc()
outputfile.close()

print('end   time:\t', time.ctime())
input('total used:\t%fs' % (time.time()-t1))
