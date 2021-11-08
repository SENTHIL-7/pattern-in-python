row = int(input("Enter the row of the pattern : "))
for i in range(1,row+1):
    space =""
    for j in range(i,row):
        space+=" "
    
    pattern = ""
    for k in range(1,2*i):
       
        if((k==1) |( k==2*i-1) |(i==row)):
            pattern +="*"
        
        else:
            pattern+= " "
    print(space + pattern)
 
           
     

    