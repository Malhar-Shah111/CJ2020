from sys import stdin
t = int(stdin.readline().strip())
solutions = []
for x in range(t):
    number = stdin.readline().strip()
    numlist = list(number)
    output = []
    for y in numlist:
        if y == '1':
            output.append('(')
            output.append(y)
            output.append(')')
            continue
        elif y == '2':
            for z in range(2):
                output.append('(')
            output.append(y)
            for z in range (2):
                output.append(')')
            continue
        elif y == '3':
            for z in range(3):
                output.append('(')
            output.append(y)
            for z in range (3):
                output.append(')')
            continue
        elif y == '4':
            for z in range(4):
                output.append('(')
            output.append(y)
            for z in range (4):
                output.append(')')
            continue
        elif y == '5':
            for z in range(5):
                output.append('(')
            output.append(y)
            for z in range (5):
                output.append(')')
            continue
        elif y == '6':
            for z in range(6):
                output.append('(')
            output.append(y)
            for z in range (6):
                output.append(')')
            continue
        elif y == '7':
            for z in range(7):
                output.append('(')
            output.append(y)
            for z in range (7):
                output.append(')')
            continue
        elif y == '8':
            for z in range(8):
                output.append('(')
            output.append(y)
            for z in range (8):
                output.append(')')
            continue
        elif y == '9':
            for z in range(9):
                output.append('(')
            output.append(y)
            for z in range (9):
                output.append(')')
            continue
        output.append(y)
    numlist2 = "".join(output)
    while ')(' in numlist2:
        numlist3 = numlist2.split(')(')
        numlist2 = "".join(numlist3)
    solutions.append(numlist2)
    
for m in range(len(solutions)):
    print("Case #"+str(m+1)+": "+solutions[m])
