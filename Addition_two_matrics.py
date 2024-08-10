X=[[1,2,3],
   [4,5,6],
   [7,8,9]
   ]
Y=[[9,8,7],
   [6,5,4],
   [3,2,1]
   ]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]
        ]
i=j=0
for i in range(len(X)):#iteration through rows
    for j in range(len(X[0])):#iteration through columns
        result[i][j]=X[i][j]+Y[i][j]#addition of elements

for r in result:
    print(r)#printing the final result