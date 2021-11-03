def linearSearch(ls,ele):
  for i in range (0,len(ls)):
   if ls[i] == ele:
      return i
      break
   return -1

ls = input("enter a list of numbers")
ls =ls.split()
result = linearSearch(ls,int(input("enter element to be found")))
if ( result == -1):
  print("Element not found")
else:
  print("Element is found at " ,result)

