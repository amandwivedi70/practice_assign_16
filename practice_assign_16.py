# 1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using tuple

t = ("Java", "Python", "SQL", "C")

print(t)

# 2. Write a python program to store only one item using tuple.
t1 = ("b",)
t2 = tuple("b")

print(type(t1)) 
print(type(t2)) 

# 3. Write a python program to reverse the tuple.
t = ("Java", "Python", "SQL", "C")
print(t)
t = t[::-1]
print(t)

# 4. Write a python program to Swap two tuples in Python.
t1 = (10, 20, 30)
t2 = (100, 200, 300)

print("T1 :", t1)
print("T2 :", t2)

t1, t2 = t2, t1

print('After Swaping : ')
print("T1 :", t1)
print("T2 :", t2)

# 5. Write a python program to check if all items in the tuple are the same.
t2 = (100, 100, 100)

j = t2[-1]

for i in t2:
    if j != i:
        print('Not same values')
        break
else:
    print('Same')

# 6. Write a python program to divide the tuple into four variables.
# tuple1=(100, 200, 300, 400)
tuple1 = (100, 200, 300, 400)

a, b, c, d = tuple1

print(a, b, c, d,sep='\n')

# 7. Write a python program to copy elements 4 and 5 from the following tuple into a new
# tuple.
# tuple1=(1,2,3,4,5,6)
tuple1 = (1, 2, 3, 4, 5, 6)

tuple2 = tuple1[3:5]

print(tuple1, tuple2, sep='\n\nNew Tuple : ')

# 8. Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))

t2 = [i for i in tuple1]

t2 = sorted(t2, key=lambda x: x[1])
t2 = tuple(t2)

print(t2)

# 9. Write a python program to print the value 20 from given nested tuple
# tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

print(tuple1[1][1])

# 10. Write a python program to change the first item (22) of a list within the following tuple to 222.
# tuple1 = (11, [22, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0] = 122

print(tuple1)