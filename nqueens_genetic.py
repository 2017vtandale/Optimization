import sys, re, math, random,time, itertools
def copy(array):
    newarr = []
    for i in range(len(array)):
        newarr.append(array[i])
    return newarr
def findIntersect(board):
    collisions = 0
    for a in range(len(board)):
      for b in range(a+1, len(board)):
         if (int(board[a])==int(board[b])) or (b-a == int(board[a])-int(board[b])) or (b-a == int(board[b])-int(board[a])):
            collisions += 1
    return collisions

def printboard(board):
    lenboard = len(board)
    tstr = ""
    for char in board:
        for i in range(int(char)-1):
            tstr+=("* | ")
        tstr+='q'
        for i in range(lenboard-(int(char))):
            tstr+=(" | *")
        print(tstr)
        xstr = ""
        for i in range(len(tstr)-1):
            xstr+="-"
        print(xstr)
        tstr = ""

def printarray(array):
    for i in ((array)):
        print(i)
    print()

def shuffle(size):
    board = list(range(1,size+1))
    random.shuffle(board)
    return board

def swap(board,r1, r2):
    trow = board[r2]
    board[r2] = board[r1]
    board[r1] = trow
    return board

def acceptp(improv,T):
    if improv/T > 150:
        return 1
    elif improv/T <150:
        return 0
    else:
        return math.pow(2.71828,improv/T)

def flip(dicti):
    newdict = {}
    for key in dicti.keys():
        if dicti[key] in newdict.keys():
            newdict[dicti[key]].append(key)
        else:
            newdict[dicti[key]] = [key]
    return newdict

def Solve(n):
    numrents = 50



    g0 = []
    multiplier = 1
    currgen = []

    for i in range(numrents):
        curr = shuffle(n)
        while len(g0)>0 and set(curr) in g0:
            curr = shuffle(n)
        g0.append(curr)

    currgen = g0
    newgen = g0
    check = True
    count = 1
    maxi = n

    while(check):

        #print(len(newgen))
        print(maxi)
        if multiplier>1.5:
            multiplier+=.05
        else:
            multiplier = 1.5

        currgen = newgen
        newgen = []
        count+=n

        interdict = {}

        for i in range(numrents):
            city1 = random.randint(0,numrents-1)

            while not (findIntersect([city1]))<multiplier*maxi:
                city1  = random.randint(0,numrents-1)

            city2 = random.randint(0,numrents-1)

            while not (city1 != city2 or findIntersect([city2])<multiplier*maxi):
                city2 = random.randint(0,numrents-1)

            pivot = random.randint(int(n/3),n-1)

            city1 = currgen[city1]
            city2 = currgen[city2]

            temp = city1[pivot:]
            baby1 = city1[0:pivot]+city2[pivot:]
            baby2 = city2[0:pivot]+temp




            if (random.randint(0,10)<3):

                rand1 = random.randint(0,len(city1)-1)
                rand2 = random.randint(0,len(city1)-1)
                while rand1 == rand2:
                    rand2 = random.randint(0,len(city1)-1)
                if random.randint(0,10)<5:
                    baby1 = swap(baby1,rand1,rand2)
                else:
                    baby2 = swap(baby2,rand1,rand2)

            newgen.append(baby1)
            newgen.append(baby2)

            intersect_1 = findIntersect(baby1)
            intersect_2 = findIntersect(baby2)

            bump = min(intersect_1,intersect_2)
            if intersect_1 in interdict:
                interdict[intersect_1].append((baby1))
            else:
                interdict[intersect_1] = [baby1]

            if intersect_2 in interdict:
                interdict[intersect_2].append([baby2])
            else:
                interdict[intersect_2] = [baby2]

            if bump<maxi:
                maxi = bump
            if bump == 0:
                check = False
                break
                
        low = list(interdict.keys())
        low = sorted(low)
        low = low[::-1]
        for i in range(len(low)):
            for k in interdict[low[i]]:
                if len(newgen)<numrents+1:
                    break
                if k in newgen:
                    newgen.remove(k)
            if len(newgen)<numrents+1:
                break


    print(bump)
    print(count)
    return best



if len(sys.argv)>1:
    size = int(sys.argv[1])
else:
    size = 55
start = time.clock()
test = Solve(size)
print(test)
printboard(test)
print("Time Taken: "+str(time.clock()-start))
