# def task1(num):
#     n=num
#     if not 1<=n<=100:
#         return "Input range error"
#     if n%2!=0:
#         return "Weird"
#     elif  2<=n<=5:
#         return "Not Weird"
#     elif 6<=n<=20:
#         return "Weird"
#     else:
#         return "Not Weird" 

# # number=int(input("Please Enter an integer: "))
# # print(task1(number))

# print(task1(int(input())))


# def task2(n1,n2):
#     if (1<=n1<=10**10 and 1<=n2<=10**10):
#         print(n1+n2)
#         print(n1-n2)
#         return n1*n2
#     else:
#         return "Range error"

# print(task2(int(input()),int(input())))

# def task3(n1,n2):
#     if n1==0:
#         print(0)
#         return "0"
#     if n2==0:
#         return "Division by zero is not possible"
#     else:
#         print(n1//n2)
#         return n1/n2
    
# print(task3(int(input()),int(input())))

# def task4(n):
#     if 1<=n<=20:
#         for x in range(0,n):
#             print(x**2)
        
#     else:
#         print("Range Error") 
    
# task4(int(input()))

# def task5(year):
#     if not 1900<=year<=10**5:
#         return "Range Constraint"
#     elif year%4 == 0:
#         if year%100==0:
#             if year%400==0:
#                 return True
#             return False
#         return True
#     return False
    
# print(task5(int(input())))

# def task6(num):
#     if not 1<=num<=150:
#         print("Constraint Error")
#     else:
#         for x in range(1,num+1):
#             print(x, sep=' ', end='', flush=True)

# task6(int(input()))

##--------------------by loops
# def task7(g1,g2):
#     for x in g2:
#        found=False
#        for y,val in enumerate(g1):
#           if x==val:
#             print(y+1, end=" ")
#             found=True
#        if not found:
#            print(-1,end="")
#        print()   
  

# a=["a","b","b","c"]
# b=["b","d","a"]
# task7(a,b)

##--------------by defaultdict

# from collections import defaultdict
# n,m=map(int,input().split())

# word_position=defaultdict(list)
# for i in range(1,n+1):
#     wrd=input().strip()
#     word_position[word].append(i)
# for _ in range(m):
#     query=input().strip()
#     if query in word_position:
#         print(' '.join(map(str,word_position[query])))
#     else:
#         print(-1)

from collections import namedtuple

# Car=namedtuple('Car','Price,Make,Milage,Color,Class')
# Car=Car(Price=120000,Make='Honda',Milage=55,Color='Silver',Class='A+')
# print(Car)
# print(Car.Make)

# Mobile=namedtuple("Mobile","Brand,RAM,Camera,Size")
# Mobile=Mobile(Brand='Apple',RAM=32,Size=6.0,Camera=3)
# print(Mobile)


# x,y=int(input()),input().split()    ###x= total stud, y=colums names
# sheet=namedtuple('sheet',y)
# m=0
# for _ in range(x):
#     d=input().split()
#     i=sheet(*d)
#     m+=int(i.MARKS)

# print(m/x)


# from collections import namedtuple
# x, y = int(input()), input().split()
# Student = namedtuple('Student', y)
# print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(x)) / x:.2f}")

##------------------------
# from collections import OrderedDict

# o_dict={}
# o_dict['a']=1
# o_dict['b']=2
# o_dict['c']=3
# o_dict['d']=4

# print(o_dict)

# o_odict=OrderedDict()
# o_odict['a']=1
# o_odict['b']=2
# o_odict['c']=3
# o_odict['d']=4
# print(o_odict)


# supermarket=OrderedDict()
# total=int(input())
# if 0<total<=100:
#     for _ in range(total):
#         *n,p=input().split()
#         x = ' '.join(n)
#         p = int(p)
#         supermarket[x] = supermarket.get(x, 0) + p
    
# for n,net_price in supermarket.items():
#     print(n,net_price)




# print(supermarket)
# print(supermarket.keys())
# print(supermarket.values())

##_---------------------
from collections import OrderedDict

n = int(input())
word_count = OrderedDict()

for _ in range(n):
    word = input().strip()
    word_count[word] = word_count.get(word, 0) + 1

print(len(word_count))
print(' '.join(str(count) for count in word_count.values()))