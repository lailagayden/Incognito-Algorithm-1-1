#Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements #of the list that are less than 5.

a.sort(reverse=True)

print(a.index(89))

for i in range(len(a)):
	print( str(i)+': '+str(a[i]))

max = 0;
for item in a:
  if item>max: 
    max = item
print('Max: ' + str(max))


min = float('inf');
for item in a:
  if item<min: 
    min = item
print('Min: '+str(min))