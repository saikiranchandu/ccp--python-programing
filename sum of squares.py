def sumsquare(l):
    odd = []
    even = []
    for items in l:
        if items % 2 == 0:
            even.append(items)
        else:
            odd.append(items)
     squre1 = [ ]
     squre2 = [ ]
     total1 = 0
     total2 = 0
     for item in odd:
         squre1.append(item ** 2)
    for item1 in even:
        square2.append(item1 ** 2)
    for i in range(0, len(square1)):
        total1 = total1 + squre1[i]
    for i in range(0, len(square2)):
        total2=total2 + square2[i]
    final_answer = [ ]
    for j in total1, total2:
        final_answer.append(j)
    print(final _answer)
li = sumsquare([18,9,1,12,13,4,30])
    
