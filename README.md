# GomoryCut
I implement two phase simplex method, dual simplex method, gomory-cut constraint to solve Integer Linear Programming
Objective Function: cX -> Max
Constraint: AX = b
X >= 0
Input:
number of constraint
coefficient of objective function
matrix coefficient of A
vector coefficient of b

Example:
2
-2 3 0 0
1 0 1 0
2 -3 0 1
5 6

Meaning:
Max Z = -2x1 + 3x2
subject to
 x1       +  x3       = 5
2x1 - 3x2       +  x4 = 6
and x1, x2, x3, x4 >= 0
