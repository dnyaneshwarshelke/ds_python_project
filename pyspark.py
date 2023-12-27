ls=[1,2,2,3,4,5,5,5,6,7,8,9]
for i in range(1,len(ls)):
   if(ls[i]==ls[i-1]):
      print(i)