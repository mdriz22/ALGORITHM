def binary_search(my_list, low, high, elem):

  if high >= low:
       mid = (high + low) // 2

       if my_list[mid] == elem:
          return mid

       elif my_list[mid] > elem:
          return binary_search(my_list, low, mid - 1, elem)

       else:
          return binary_search(my_list, mid + 1, high, elem)
  else:

       return -1

import matplotlib.pyplot as plt
import time
ot=[]
yvalue=[]
T=int(input("Enter no of Excution"))
for j in range(0,T):
  start=time.time()
  n=int(input("Enter n"))
  yvalue.append(n)
  my_list=[]
  for i in range(0,n):
    ele=int(input("Enter Element"))
    my_list.append(ele)
  elem_to_search = int(input("Enter key"))
  print("The list is")

  for i in range(0,n):
    print(my_list[i])

  my_result = binary_search(my_list,0,len(my_list)-1,elem_to_search)
  if my_result != -1:
    print("Element found at index ", str(my_result))
  else:
    print("Element not found!")
  end=time.time()
  tn=end-start
  ot.append(tn)

print("Execution time",ot)

# Plot a graph
x=ot
y=yvalue
plt.plot(x,y)
plt.show()
