# GomoryCut
I implement two phase simplex method, dual simplex method, gomory-cut constraint to solve Integer Linear Programming <br />
Objective Function: cX -> Max <br />
Constraint: AX = b <br />
X >= 0 <br />
Input: <br />
number of constraint <br />
coefficient of objective function <br />
matrix coefficient of A <br />
vector coefficient of b <br />

Example:<br />
2 <br />
-2 3 0 0 <br />
1 0 1 0 <br />
2 -3 0 1 <br />
5 6 <br />

Meaning:
Max Z = -2x1 + 3x2 <br />
subject to <br />
 x1       +  x3       = 5 <br />
2x1 - 3x2       +  x4 = 6 <br />
and x1, x2, x3, x4 >= 0 <br />
