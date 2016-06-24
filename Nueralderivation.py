import math, random, sys
def check(x, expected, w, b, error):
    for i in range(len(x)): error += math.pow(1/(1+    math.pow(2.71828,(-1*w*x[i])+b)    )-expected[i],2)
    return error
def getDir(x,expected,w,b, error):
    for i in [0,.005,-.005]:
        for z in [0,.005,-.005]: error[check(x,expected,w+i,b+z,0)] = (w+i,b+z)
    if min(error.keys())<.001: return (0,0)
    return error[min(error.keys())]
def Solve(x,expected):
    w, b = (1,.01)
    dir = getDir(x,expected,w,b,{})
    while not dir == (0,0):
        w,b = dir
        dir = getDir(x,expected,dir[0],dir[1],{})
    return (w,b)
print("Not: "+str(Solve([1,0],[0,1]))+"\nAnd: "+str(Solve([2,1,0],[1,0,0]))+"\nOR: "+str(Solve([2,1,0],[1,1,0])))
