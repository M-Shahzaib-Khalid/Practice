##---------------global variable

# x="awesome"
# def myfunc():
#   global x ##if removed x will not be updated making it static
#   x="wow"

# myfunc()
# print(x)

##--------------type checking

# x=5
# print(type(x))
# y="Name"
# print(type(y))
# z=8.25
# print(type(z))
# a=[1,2,3]
# print(type(a))
# print(len(a))
# b={1,2,3}
# print(type(b))
# print(len(b))
# c=(1,2,3)
# print(type(c))
# print(len(c))

# x=y=z=5
# a,b,c=1,2,3
# print('x =',x,'\ny =',y,'\nz =',z,'\na =',a,'\nb =',b,'\nc =',c)

# #---------------unpacking 
# mylist=["apple","mango","orange"]
# x,y,z=mylist 
# print(x,y,z)

# myset={1,2,3}
# x,y,z=myset ##same for tuples
# print(x,y,z)

##----------------type casting

#x="55"
# print(float(x))
# print(str(x))
# print(complex(x))
# print(bool(x)) ##return True- False only to 0 and empty

# a=b"abc"
# print(type(a))
# b=b"12" ##only work for str
# print(type(b))
# print(a,b)

##-----------random generation

# import random
# print(random.randrange(10,20))

# a="Hello, World"
# print(a[0])

# print(len(a))

# for x in a: ##iterate letter by letter
#     print(x)

# for x in a:
#     if "W" == x:
#         print("found")
# print("Nill")

# b="My name is Shahzaib"
# if "shahzaib" in b.lower():
#     print("Found")
# elif "shahzaib" in b: ##if shahzaib after Shahzaib fail to execute
#     print("Found in elif")
# else:
#     print("not found")
    
# print(b[3:10])
# print(b[::-1])
# print(b[-5:-1])
# print(b[-5:])
# print(b[:-5])
# ba="  My name is Shahzaib  "
# print(ba.upper())
# print(ba.lower())
# print(ba.strip())
# print(ba.replace("S","$"))
# print(ba.split("is"))

# e="Hello"
# f="World"
# c=e+f
# d=e+" "+f
# g=e,f ##dealing as tuple
# print(c," | ",d," | ",g)


##----------------string format
# name="Shahzaib"
# age=21
# salary=20
# sen=f"My name is {name}. I am {age} years old."
# print(sen)
# sen=f"My name is {name}. I am {age} years old. My stipend is {salary:.2f}"
# print(sen)
# aa=name.capitalize()
# print("Capatilize 1st letter =",aa)
# bb=name.casefold()
# print("Lower case all =",bb)
# cc=name.center(10)
# print("Center in given space = ",cc)
# dd=name.count("h")
# print("Count of accurance of h =",dd)
# ee=name.encode()
# print("Encode = ",ee)
# ff=name.endswith("z")
# print("If endswith given argument =",ff)
# gg=name.find("a")
# print("Total found =",gg)

##----------operators
'''these operators perform calculation on binary level'''
# x=10
# x|=3 ##binary or of 10 and 3
# print(x)
# x=10 
# x&= 3 ##binary and of 10 and 3
# print(x)
# x=10
# x^=3 ##binary xor of 10 and 3
# print(x)
# x=10
# x>>=3 ##shift bits to right by 3 and discard 
# print(x)
# x=10
# x<<=3 ##shift bit to left by 3
# print(x)

##-------------list

# mylist=["mango","peach","apple","apple"]
# print(len(mylist))
# print(mylist[0:-1])

# if "apple" in mylist:
#     print("Yes, it is in list")
    
# mylist[0]="Cheery"
# print(mylist)

# mylist.append("pineapple") ##add at end
# print(mylist)

# mylist.insert(1,"Banana")
# print(mylist)

# mylist.insert(0,"Pomegrant")
# print(mylist)

# mylist[2:-3]=["Guava","Leachy"] ##replacing banana by two items
# print(mylist)

# yourlist=["Apricot","Berry"]
# mylist.extend(yourlist)
# print(mylist)

# print("-----------------Loop-------------------")
# for x in mylist:
#     print(x)
# print("-----------------In line Loop-------------------")
# [print(x) for x in mylist]
# print("-----------------By index Loop-------------------")
# for x in range(len(mylist)):
#     print(mylist[x])

# print("-----------------By while Loop-------------------")
# i=0
# while i in range(len(mylist)):
#     print(mylist[i])
#     i+=1

# print("-----------------List comprehension-------------------")
# fruits=[x for x in mylist if "g" in x.lower()]
# print(fruits)
# print("-----------------deletion-------------------")
# mylist.pop()
# print(mylist)

# mylist.pop(3)
# print(mylist)

# mylist.remove("apple") ##will remove first occurance only
# print(mylist)

# del mylist[3]
# print(mylist)

# mylist.clear()
# print(mylist)

##-------------------Sorting
# mylist=['Pomegrant', 'Cheery', 'Guava', 'Leachy', 'apple', 'apple', 'pineapple']
# print(mylist)
# print("-------------------Exact Reverse Sorting")
# mylist.reverse()
# print(mylist)
# print("-------------------default Sorting")
# mylist.sort()
# print(mylist)
# print("-------------------Descending Sorting")
# mylist.sort(reverse=True)
# print(mylist)
# print("-------------------Case Insensitive Sorting")
# mylist.sort(key=str.lower)
# print(mylist)
# print("-------------------Function based Sorting")
# def myfunc(st):
#     if type(st)== str:
#         return st
# mylist.sort(key=myfunc)
# print(mylist)

# def myfunct(st):
#     return st if "g" in st else "0" ##if g is found it will be lack back
# mylist.sort(key=myfunct)
# print(mylist)

##-------------Joining
# print("----------By operators")
# mylist=["apple","banana","mango","pineapple"]
# mlist=["cheery","peach"]
# mylist+=mlist
# print(mylist)
# mylist.clear()
# mlist.clear()
# print(mylist)

# print("----------By Build-in func")
# mylist=["apple","banana","mango","pineapple"]
# mlist=["cheery","peach"]
# mylist.extend(mlist)
# print(mylist)
# mylist.clear()
# mlist.clear()
# print(mylist)

# print("----------By loop")
# mylist=["apple","banana","mango","pineapple"]
# mlist=["cheery","peach"]
# for x in mlist:
#     mylist.append(x)
    
# print(mylist)
# mylist.clear()
# mlist.clear()
# print(mylist)


    