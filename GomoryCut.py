from LP import simplex
from fractions import Fraction
import numpy as np

def main():
    ##Nhap du lieu
    A, b, c = readInput()

    ##Xay dung bai toan phu
    #them slack var
    A_sub = np.hstack((A, np.eye(len(A))))

    #Ham muc tieu cho bai toan phu
    c_sub = np.zeros((len(c)+len(A)))
    for i in range(len(c), len(c) + len(A)):
       c_sub[i] = -1

    c_gomory = np.hstack((c, [0]))

    #Phrase 1
    print("Phase 1:")
    sim = simplex(A, A_sub, b, c, c_sub, c_gomory)
    table = sim.createtable()
    table = sim.phrase1(table)

    for i in range(len(table)):
        table[i][1] = c[int(table[i][0])]

    print()
    ##Phrase 2
    print("Phase 2:")
    table = sim.phrase2(table)

    ##Ket qua sau 2 pha
    obj = np.sum(table[:, 1]*table[:, 2])
    print("Obj = ", Fraction(obj).limit_denominator(100))
    result = np.zeros((len(A[0])))
    for i in range (len(table)):
        result[i] = table[i][2]

    for i in range (len(result)):
        print("X"+str(i), "=", Fraction(result[i]).limit_denominator(100))


    for i in range(len(table)):
        for j in range (1, len(table[i])):
            table[i][j] = Fraction(table[i][j]).limit_denominator(100)

    ##Gomory-cut cho 1 bien 
    table, cut = gomory_cut(table)
    if cut == True:
        table = sim.dualSimplex(table)
        obj = np.sum(table[:, 1]*table[:, 2])
        print("Obj = ", Fraction(obj).limit_denominator(100))
        result = np.zeros((len(A[0])))
        for i in range (len(table)):
            if (i < len(A[0])):
                result[i] = table[i][2]

        for i in range (len(result)):
            print("X"+str(i), "=", Fraction(result[i]).limit_denominator(100))

def isInteger(fraction):
    if (fraction.denominator == 1):
        return True
    else:
        return False

def gomory_cut(table):
    X = []
    index = []
    for i in range(len(table)):
        if(not isInteger(Fraction(table[i][2]).limit_denominator(100))):
            X.append(convert(Fraction(table[i][2]).limit_denominator(100)))
            index.append(i)


    if len(index) == 0:
        print("Cac nghiem deu nguyen")
        cut = False
        return table, cut

    b = max(X)
    constraint = []
    constraint.append(len(table[0])-3)
    constraint.append(0)
    constraint.append(-b)
    for i in range (3, len(table[0])):
        constraint.append(-convert(Fraction(table[index[0]][i]).limit_denominator(100)))
    constraint.append(1)

    print("Ap dung Gomory-cut cho x"+ str(index[0]))

    table = np.hstack((table, np.zeros((len(table), 1))))
    table = np.vstack((table, constraint))
    cut = True

    return table, cut  
	    
def convert(fraction):
    numerator = fraction.numerator
    denominator = fraction.denominator
    return Fraction(numerator%denominator, denominator)

def readInput():
    print("Nhap ten file")
    fileName = input()
    f = open(fileName, 'r')
    constraint_num = int(f.readline())
    c = [float(ci) for ci in f.readline().split()]
    A = []
    for i in range (constraint_num):
    	A.append([float(Aij) for Aij in f.readline().split()])
    b = [float(bi) for bi in f.readline().split()]

    return np.asarray(A), np.asarray(b), np.asarray(c)


if __name__ == "__main__":
    main()
