lst=[[0for x in range(9)]for y in range(9)]
#reading samples
for i in range(9):
    print("raw no.",i+1,end="")
    sample=input(" enter smaple ")
    for j in range(9):
        lst[i][j]=sample[j]
def check(lst):
#check row
    for i in lst:
      strng=""
      for j in i:
          strng+=j
      for ch in "123456789":
          if strng.find(ch)==-1:
              print("no")
              return
            
    #check column
    for i in range(9):
      strng=""
      for j in range(9):
          strng+=(lst[j][i])
      for ch in "123456789":
          if strng.find(ch)==-1:
              print("no")
              return
    #spliting sub squares
    x=0
    y=0
    while(x<9):
        for i in range(0+x,3+y):
            for k in range(3):
                strng=""
                for j in range(3*k,3*k+3):
                    strng+=(lst[i][j])
                for ch in "123456789":
                  if strng.find(ch)==-1:
                      print("no")
                      return
        x+=3
        y+=3
    if x==9:
        print("yes")
        return
check(lst)
            
        
 
    
         
