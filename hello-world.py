#created by: Ben Chapman
#this code was developed using python version 2.7.6

print 'hello world!'

#for loops review
for i in range(0, 10):
	print i

print '\n'

#list review
homogenous_list = [2, 5, 1, 7]
for i in homogenous_list:
	print i

print '\n'

#lists can have different variable types as elements
mixed_list = [3, 'e', 4.5, [1, 2], "test", (2, 1, 3)]
for i in mixed_list:
	print i

print '\n'

#how to add values to the end of a list
homogenous_list.append(9)
for i in homogenous_list:
	print i

print '\n'

#how to set a value in a list
homogenous_list[2] = 10
for i in homogenous_list:
	print i

print '\n'

#we can set every value in a list
for i in range(len(homogenous_list)):
	homogenous_list[i] = 2 + i

for i in homogenous_list:
	print i

print '\n'

#lets review tuples
tup1 = (3, 5, 9)

#print the whole thing
print tup1

#print the third element
print tup1[2]

#print the second and third elements
print tup1[1:3]

tup2 = (1,2,4,6,3,2,7,2,3,5,9,7,9,4,2)

#print all elements from the fourth to the 9th
print tup2[3:9]

#we'll do more review later
