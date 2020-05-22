import numpy as np
from fractions import Fraction

class simplex:

    def __init__(self, A, A_sub, b, c, c_sub, c_gomory):
        self.A = A
        self.A_sub = A_sub
        self.b = b
        self.c = c
        self.c_sub = c_sub
        self.c_gomory = c_gomory  

    def createtable(self):
        size = list(self.A_sub.shape)
        cb = np.array(self.c_sub[size[1]-size[0]])
        B = np.array([size[1]-size[0]])

        for i in range(size[1]-size[0]+1,size[1]):
            cb = np.vstack((cb, self.c_sub[i]))
            B = np.vstack((B, i))
            xb = np.transpose([self.b])
        
        table = np.hstack((B, cb))
        table = np.hstack((table, xb))

        table = np.hstack((table, self.A_sub))

        table = np.array(table, dtype = 'float')

        return table

    def phrase1(self, table):

        size = list(self.A_sub.shape)
        print(len(self.A[0]))

        for row in table: 
            for el in row: 
                print(Fraction(str(el)).limit_denominator(100), end ='\t')  
            print() 
        reached = 0     
        itr = 1
        unbounded = 0
        alternate = 0
        
        while reached == 0: 
            # calculate Relative profits-> zj - cj for non-basics 
            i = 0
            rel_prof = [] 
            while i<(len(table[0])-3): 
                rel_prof.append(-self.c_sub[i] + np.sum(table[:, 1]*table[:, 3 + i])) 
                i = i + 1
        
            print("Zi-Ci: ", end =" ") 
            for profit in rel_prof: 
                print(Fraction(str(profit)).limit_denominator(100), end =", ") 
            print() 
            i = 0
            
            b_var = table[:, 0]
            # checking for alternate solution 
            while i<(len(table[0])-3): 
                j = 0
                present = 0
                while j<len(b_var): 
                    if int(b_var[j]) == i: 
                        present = 1
                        break; 
                    j+= 1
                if present == 0: 
                    if rel_prof[i] == 0: 
                        alternate = 1
                        # print(i, end =" ") 
                i+= 1
            print() 
            flag = 0
            for profit in rel_prof: 
                if profit < 0: 
                    flag = 1
                    break
                # if all relative profits > 0 
            if flag == 0: 
                print("All profits are >= 0, optimality reached") 
                reached = 1
                break
        
            # kth var will enter the basis 
            k = rel_prof.index(min(rel_prof)) 
            minValue = 99999
            i = 0; 
            r = -1
            # min ratio test (only positive values) 
            while i<len(table): 
                if (table[:, 2][i]>0 and table[:, 3 + k][i]>0):  
                    val = table[:, 2][i]/table[:, 3 + k][i] 
                    if val<minValue: 
                        minValue = val 
                        r = i     # leaving variable 
                i+= 1
        
                # if no min ratio test was performed 
            if r ==-1: 
                unbounded = 1
                print("Case of Unbounded") 
                break
        
            print("pivot element index:", end =' ') 
            print(np.array([r, 3 + k])) 
        
            pivot = table[r][3 + k] 
            print("pivot element: ", end =" ") 
            print(Fraction(pivot).limit_denominator(100)) 
                
                # perform row operations 
            # divide the pivot row with the pivot element 
            table[r, 2:len(table[0])] = table[ 
                    r, 2:len(table[0])] / pivot 
                    
            # do row operation on other rows 

            i = 0
            while i<len(table): 
                if i != r: 
                    table[i, 2:len(table[0])] = table[i, 
                        2:len(table[0])] - table[i][3 + k] * \
                        table[r, 2:len(table[0])] 
                i += 1
        
            
            # assign the new basic variable 
            table[r][0] = k 
            table[r][1] = self.c_sub[k] 
            
            for row in table: 
                for el in row: 
                    print(Fraction(str(el)).limit_denominator(100), end ='\t')  
                print()
            itr+= 1
        
        if unbounded == 1: 
            print("UNBOUNDED LPP") 
            exit()
        if alternate == 1: 
            print("ALTERNATE Solution") 
    
        i = 0
        while i < len(table):
            if (table[i][0] >= (len(self.A[0]))):
                if table[i][2] != 0:
                    print("khong co nghiem co so chap nhan duoc")
                    exit()
                else:
                    table = np.delete(table, (i), axis = 0)
                    i -= 1
            i += 1 
        
        F = np.array([table[0]])
        i = 1
        while i < len(table):
            F = np.vstack((F, table[i]))
            i += 1
    
        for i in range(size[0]):
            a = len(F[0]) - 1     
            F = np.delete(F, (a), axis = 1)
   
        return F
    
    def phrase2(self, table):


        reached = 0     
        itr = 1
        unbounded = 0
        alternate = 0
        
        while ((reached == 0) & (itr < 4)): 

            i = 0
            rel_prof = []
            print("Iteration: ", end =' ') 
            print(itr) 
     
            for row in table: 
                for el in row: 
                    print(Fraction(str(el)).limit_denominator(100), end ='\t') 
                print() 
    
        #calculate Relative profits-> Zj - cj for non-basics 
            while i<(len(table[0])-3): 
                rel_prof.append(-self.c[i] + np.sum(table[:, 1]*table[:, 3 + i])) 
                i = i + 1
            print("Zj - cj: ", end =" ") 
            for profit in rel_prof: 
                print(Fraction(str(profit)).limit_denominator(100), end =", ") 
            print() 
            i = 0
            
            b_var = table[:, 0] 
            # checking for alternate solution 
            while i<(len(table[0])-3): 
                j = 0
                present = 0
                while j<len(b_var): 
                    if int(b_var[j]) == i: 
                        present = 1
                        break; 
                    j+= 1
                if present == 0: 
                    if rel_prof[i] == 0: 
                        alternate = 1
                i+= 1
            print() 
            flag = 0
            for profit in rel_prof: 
                if profit < 0: 
                    flag = 1
                    break
                # if all relative profits > 0 
            if flag == 0: 
                print("All profits are >= 0, optimality reached") 
                reached = 1
                break
        
            # kth var will enter the basis 
            k = rel_prof.index(min(rel_prof)) 
            minValue = 99999
            i = 0; 
            r = -1
            # min ratio test (only positive values) 
            while i<len(table): 
                if (table[:, 2][i]>0 and table[:, 3 + k][i]>0):  
                    val = table[:, 2][i]/table[:, 3 + k][i] 
                    if val<minValue: 
                        minValue = val 
                        r = i     # leaving variable 
                i+= 1
        

            if r ==-1: 
                unbounded = 1
                print("Case of Unbounded") 
                break
        
        
            print("pivot element index:", end =' ') 
            print(np.array([r, 3 + k])) 
        
            pivot = table[r][3 + k] 
            print("pivot element: ", end =" ") 
            print(Fraction(pivot).limit_denominator(100)) 

            table[r, 2:len(table[0])] = table[ 
                    r, 2:len(table[0])] / pivot 
                    
            # do row operation on other rows 
            i = 0
            while i<len(table): 
                if i != r: 
                    table[i, 2:len(table[0])] = table[i, 
                        2:len(table[0])] - table[i][3 + k] * \
                        table[r, 2:len(table[0])] 
                i += 1
        
            
            # assign the new basic variable 
            table[r][0] = k 
            table[r][1] = self.c[k] 
            
            # print() 
            # print() 
            itr+= 1
        
        if unbounded == 1: 
            print("UNBOUNDED LPP") 
            exit()
        if alternate == 1: 
            print("ALTERNATE Solution") 
            print(table)
        # i = 0

        for row in table: 
            for el in row: 
                print(Fraction(str(el)).limit_denominator(100), end = '\t')  
            print() 
        
   
        return table

    def dualSimplex(self, table):
        reached = 0     
        itr = 1
        unbounded = 0
        alternate = 0
        
        while ((reached == 0) & (itr < 4)): 

            i = 0
            rel_prof = []
            ratio = []
            print("Iteration: ", end =' ') 
            print(itr) 
     
            for row in table: 
                for el in row: 
                    print(Fraction(str(el)).limit_denominator(100), end ='\t') 
                print() 
    

            min = 99999
            i = 0 
            r = -1
            ##TO_DO - check unbound
            # minimize negative Xb
            while i<len(table): 
                if (table[:, 2][i] < 0):  
                    val = table[:, 2][i] 
                    if val<min: 
                        min = val 
                        r = i     
                i+= 1

            i = 0
            #calculate Relative profits-> zj - cj for non-basics 
            while i<(len(table[0])-3): 
                rel_prof.append(-self.c_gomory[i] + np.sum(table[:, 1]*table[:, 3 + i]))
                if(table[r][3+i] != 0):
                    ratio.append(rel_prof[i]/table[r][3+i])
                else:
                    ratio.append(-999999)
                i = i + 1

            print("profit: ", end =" ")
            for profit in rel_prof: 
                print(Fraction(str(profit)).limit_denominator(100), end =", ")
            print()
            print("ratio: ", end =" ")  
            for rate in ratio:
                print(Fraction(str(rate)).limit_denominator(100), end =", ")
            print() 

            flag = 0
            for profit in rel_prof: 
                if profit < 0: 
                    flag = 1
                    break
                # if all relative profits > 0 
            if flag == 0 and r == -1:
                print("optimality reached") 
                reached = 1
                break
            elif r == -1: 
                unbounded = 1
                break

            i = 0
            
            b_var = table[:, 0] 
            # checking for alternate solution 
            while i<(len(table[0])-3): 
                j = 0
                present = 0
                while j<len(b_var): 
                    if int(b_var[j]) == i: 
                        present = 1
                        break; 
                    j+= 1
                if present == 0: 
                    if rel_prof[i] == 0: 
                        alternate = 1
                        # print(i, end =" ") 
                i+= 1
            print() 
        
            # kth var will enter the basis
            # k = ratio.index(max(ratio))
            # print(ratio[k])
            #print(ratio) 

            max = -999999999
            k = -1
            for i in range (len(ratio)):
                if(ratio[i] < 0 and ratio[i] > max):
                    max = ratio[i]
                    k = i
        
        
            print("pivot element index:", end =' ') 
            print(np.array([r, 3 + k])) 
        
            pivot = table[r][3 + k] 
            print("pivot element: ", end =" ") 
            print(Fraction(pivot).limit_denominator(100)) 

            table[r, 2:len(table[0])] = table[ 
                    r, 2:len(table[0])] / pivot 
                    
            # do row operation on other rows 
            i = 0
            while i<len(table): 
                if i != r: 
                    table[i, 2:len(table[0])] = table[i, 
                        2:len(table[0])] - table[i][3 + k] * \
                        table[r, 2:len(table[0])] 
                i += 1
        
            
            # assign the new basic variable 
            table[r][0] = k 
            table[r][1] = self.c_gomory[k] 
            
            print() 
            print() 
            itr+= 1

        if unbounded == 1 and reached == 0:
            print("UNBOUNDED LPP") 
            exit()
        if alternate == 1: 
            print("ALTERNATE Solution") 
        # i = 0
        
        return table
