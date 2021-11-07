row =int(input("ENter the number of row :"))

for i in range(1,row+1):
   pat =""
   space =""
   for j in range(row,i,-1):
       space+=" "
   for k in range(0,2*i-1):
       pat+="*"
   print(space+pat)

