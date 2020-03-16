numbers = tuple(range(1,10))

count_even = 0
count_odd = 0

#for i in numbers:
#   if i % 2 == 0:
 #       print(i,"is even")
  #  else:
  #      print(i,'is odd')

for x in numbers:
    if x % 2 == 0:
        count_even +=1
    else:
        count_odd +=1

print("Even numbers =",count_even)
print("Odd numbers =",count_odd)

                      