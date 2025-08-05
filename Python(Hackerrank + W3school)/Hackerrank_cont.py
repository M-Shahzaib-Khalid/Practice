##----------------------Ration of +,-,0 in List
# def ration_cal(array):
#     pos=neg=zero=0
#     for x in array:
#         if x>0:
#             pos+=1
#         elif x<0:
#             neg+=1
#         else:
#             zero+=1
#     l=len(array)
#     print(f"{pos/l:.6f}")
#     print(f"{neg/l:.6f}")
#     print(f"{zero/l:.6f}")

#-------------Max and Min sum of list neglecting last

# def min_max(arr):
#     maximum=minimum=0
#     array=arr.copy()
#     for x in range(len(arr)-1):
#         m=max(arr)
#         maximum+=m
#         arr.remove(m)
#     for x in range(len(array)-1):
#         n=min(array)
#         minimum+=n
#         array.remove(n)

#     print(minimum,sep=" ",end=" ",flush=True)
#     print(maximum)
#arr = list(map(int, input().rstrip().split()))

#-------------Time Format conversion

# from datetime import datetime        
# def timeconversion(s):
#     dt=datetime.strptime(s,"%I:%M:%S%p")
#     convert=dt.strftime("%H:%M:%S")
#     return convert



# s=input()
# print(timeconversion(s))

##---------------median
# def median(arr):
#     l=len(arr)
#     arr=sorted(arr)
#     if l%2==0:
#         print(arr[l//2])
#     else:
#         print(arr[l//2])

# a=[1,5,4,2,3]       #3
# b=[1,2,3,4,5,6]       #4
# c=[1,9,0,7,6,3,5]       #5
# median(c)

##-------------find unique
# def lonelyinteger(a):
#     for x in a:
#         if a.count(x)==1:
#             return x

# a=[1,2,3,4,3,2,1]
# print(lonelyinteger(a))

##-----------Diagonal absolute difference

# import numpy as np

# def diagonal_difference(arr):
#     l=len(arr)
#     left_diag=right_diag=0
#     for x in range(l):
#         left_diag+=arr[x][x]
#         right_diag+=arr[x][n-1-x]
#     return abs(left_diag-right_diag)


# n=3
# arr=[]
# for _ in range(n):
#     arr.append(list(map(int,input().rstrip().split())))
# print(arr)
# print(diagonal_difference(arr))

##----------------Frequency

# def freq(arr):
#     array=sorted(arr)
#     l=len(array)
#     count_freq=[0]*(l)
#     for x in array:
#         count_freq[x]+=1

#     return count_freq



#     array=sorted(arr)
#     frequency=[]
#     for x in range(100):
#         c=array.count(x)
#         frequency.append(c)
#     return frequency
# arr=[1,2,1,1,3,2]
# print(freq(arr))

# a="63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33"
# c=list(map(int,a.split()))

# print(freq(c))

##----------------Flip Matrix

# def flippingMatrix(matrix):
#     n = len(matrix) // 2
#     total = 0
#     for i in range(n):
#         for j in range(n):
#             total += max(
#                 matrix[i][j],
#                 matrix[i][2*n - 1 - j],
#                 matrix[2*n - 1 - i][j],
#                 matrix[2*n - 1 - i][2*n - 1 - j]
#             )
#     return total

##--------------Nearly similar rectangles

# from collections import defaultdict
# from math import gcd

# def nearlySimilarRectangles(sides):
#     ratio_count = defaultdict(int)
#     result = 0
    
#     for a, b in sides:
#         g = gcd(a, b)
#         reduced = (a // g, b // g)
#         result += ratio_count[reduced]
#         ratio_count[reduced] += 1
        
#     return result

##------------Road Repair

# def getMinCost(crew_id, job_id):
#     crew_id.sort()
#     job_id.sort()
#     total_distance = sum(abs(c - j) for c, j in zip(crew_id, job_id))
#     return total_distance

##-----------------List compression

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) 
#           for k in range(z + 1) 
#           if i + j + k != n]

# print(result)

##--------------------Runner Up
# n = int(input())
# arr = map(int, input().split())
    
# arr=sorted(arr)
# if not arr[-1]==arr[-2]:
#     print(arr[-2])
# else:
#     array=set(arr.copy())
#     m=max(array)
#     array.remove(m)
#     result=max(array)
#     print(result)

##---------Nested list
# record=[]
# for _ in range(int(input())):
#     name=input()
#     grade=input()
#     record.append([name,grade])

# unique_scores = sorted(set(score for name, score in record))
# second_lowest = unique_scores[1]


# students_with_second_lowest = [name for name, score in record if score == second_lowest]

# for name in sorted(students_with_second_lowest):
#     print(name)

##----------Avg of marks from dict
# n= int(input())
# student_marks={}
# for _ in range(n):
#     name,*line=input().split()
#     scores=list(map(int,line))
#     student_marks[name]=scores
# query_name=input()

# marks=student_marks[query_name]
# sum=0
# for x in marks:
#     sum+=x

# print(f"{sum/len(marks):.2f}")

##----------------Color Code

# import re

# css_line=[]
# n=int(input())

# for _ in range(n):
#     css_line.append(input())

# pattern=re.compile(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3}?)')
# inside=False
# for line in css_line:
#     if '{' in line:
#         inside=True
#         continue
#     if '}' in line:
#         inside=False
#         continue
#     if inside:
#         matches=pattern.findall(line)
#         for match in matches:
#             print(match)
            
##-----------------HTml Parser

# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.skip_data = False

#     def handle_starttag(self, tag, attrs):
#         print(f"Start : {tag}")
#         for attr in attrs:
#             print(f"-> {attr[0]} > {attr[1] if attr[1] is not None else 'None'}")
#         if tag in ["title", "h1", "h2", "h3", "h4", "h5", "h6", "script", "style"]:
#             self.skip_data = True

#     def handle_endtag(self, tag):
#         print(f"End   : {tag}")
#         if tag in ["title", "h1", "h2", "h3", "h4", "h5", "h6", "script", "style"]:
#             self.skip_data = False

#     def handle_startendtag(self, tag, attrs):
#         print(f"Empty : {tag}")
#         for attr in attrs:
#             print(f"-> {attr[0]} > {attr[1] if attr[1] is not None else 'None'}")

#     def handle_data(self, data):
#         if data.strip() and not self.skip_data:
#             print(data.strip())

#     def handle_comment(self, data):
#         pass  # Ignore comments

# n = int(input())
# lines = [input() for _ in range(n)]
# html = '\n'.join(lines)

# parser = MyHTMLParser()
# parser.feed(html)

##-------------List 
# mylist=[]
# n=int(input())
# command=[]
# for _ in range(n):
#     command.append(input().split())

# for x in command:
#     if x[0]=="append":
#         mylist.append(int(x[1]))
#     elif x[0]=="insert":
#         mylist.insert(int(x[1]), int(x[2]))
#     elif x[0]=="remove":
#         mylist.remove(int(x[1]))
#     elif x[0]=="pop":
#         mylist.pop()
#     elif x[0]=="sort":
#         mylist.sort()
#     elif x[0]=="reverse":
#         mylist.reverse()
#     elif x[0]=="print":
#         print(mylist)
#     else:
#         print("Invalid Command")

##------------Hash Calculator

# n=int(input())

# mytuple=tuple(map(int, input().split()))
# print(hash(mytuple))

##----------------Zigzag correction
# def findZigZagSequence(a, n):
#     a.sort()
#     mid = int(n//2)
#     a[mid], a[-1] = a[-1], a[mid]

#     st = mid + 1
#     ed = n - 2
#     while(st <= ed):
#         a[st], a[ed] = a[ed], a[st]
#         st = st + 1
#         ed = ed - 1

#     for i in range (n):
#         if i == n-1:
#             print(a[i])
#         else:
#             print(a[i], end = ' ')
#     return a

# test_cases = int(input())
# for cs in range (test_cases):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(findZigZagSequence(a, n))

##-------------Tower breaker

# def breaker(n,m):
#     if m==1 or n%2==0:
#         return 2
#     else:
#         return 1

##---------Cipher

# def cipher(s,t):
#     encrypt=''
#     for x in s:
#         if x.isalpha():
#             if ord(x) in range(65,90):
#                 a=ord(x)+t
#                 if(a>90):
#                     b=(64+(a-90))
#                     encrypt+=chr(b)
#                 else:
#                     encrypt+=chr(a)
#             else:
#                 a=ord(x)+t
#                 if(a>122):
#                     b=(96+(a-122))
#                     encrypt+=chr(b)
#                 else:
#                     encrypt+=chr(a)
#         else:
#             encrypt+=x
#     return encrypt

##--------------More Clean

# def cipher(s,t):
#     encrypt=''
#     for x in s:
#         if (65<=ord(x)<=90) or (97<=ord(x)<=122):
#                 if ord(x)<=90:
#                     encrypt+=chr((ord(x)-65+t) % 26 + 65)
#                 else:
#                   encrypt+=chr((ord(x)-97+t)% 26 + 97)   
#         # elif (97<=ord(x)<=122):
#         #         encrypt+=chr((ord(x)-97+t)% 26 + 97)
#         else:
#             encrypt+=x

#     return encrypt

# print(cipher("middle-Outz1 z",2))

##--------------------Palindrome Index

# r='aabcaa'
# s=r

# def is_palindrome(s):
#     return s==s[::-1]
 
# def palindrome_index(s):
#     if is_palindrome(s):
#         return -1
#     left,right=0,len(s)-1
#     while left<right:
#         if s[left]!=s[right]:
#             if is_palindrome(s[left+1:right+1]):
#                 return left
#             elif is_palindrome(s[left:right]):
#                 return right
#             else:
#                 return -1
#         left+=1
#         right-=1
#     return -1


# print(palindrome_index(s))
    
##--------------Grid Challenge
# # l=int(input())
# # mylist=[input() for _ in range(l)]
# mylist=['azb','fde']


# print(mylist)
# def grid(s):
#     a=[sorted(x) for x in s ]
#     for x in range(len(a[0])):
#         for y in range(1,len(a)):
#             if a[y][x]<a[y-1][x]:
#                 return 'NO'
#     return 'YES'

# print(grid(mylist))

##-------------superdigit

num='12345'

# def superdigit(s):
#     a=0
#     for x in s:
#         a+=int(x)

#     if a>=10:
#         b=str(a)
#         return superdigit(b)
#     else:
#         b=a
#         return b

# print(superdigit(num))
# s=input()
# i=int(input())
# def concat(s,k):
#     a=''
#     t=0
#     for x in range(k):
#         a+=s
#     for x in a:
#         t+=int(x)

#     if t>=10:
#         t=str(t)
#         return concat(t,1)
#     return t

# print(concat(s,i))

# s = input()
# i = int(input())

# def digit_sum(n,k):
#     initial=sum(int(x) for x in n)*k
#     while initial>=10:
#         initial=sum(int(y) for y in str(initial) )
#     return initial

# print(digit_sum(s, i))

##----------------New Year Chaos

# def minimumBribes(positions):
#     bribes = 0
#     for i in range(len(positions)):
#         if positions[i] - (i + 1) > 2:
#             print("Too chaotic")
#             return

#         for j in range(max(0, positions[i] - 2), i):
#             if positions[j] > positions[i]:
#                 bribes += 1
#     print(bribes)

# test_cases=int(input())

# for _ in range(test_cases):
#     people=int(input())
#     positions=list(map(int,input().split()))
#     minimumBribes(positions)

##------------------------
# total_petrol = 0
# total_distance = 0
# tank = 0
# start_index = 0

# def truck(petrolpumps):
#     for i, (petrol, distance) in enumerate(petrolpumps):
#         total_petrol += petrol
#         total_distance += distance
#         tank += petrol - distance
#         if tank < 0:
#             start_index = i + 1
#             tank = 0

#     return start_index if total_petrol >= total_distance else -1

##-------------Hash Value

# i=input()
# mytuple=tuple(map(int,input().split()))
# print(hash(tuple(mytuple)))

# n=int(input())
# mylist=map(int,input().split())
# t=tuple(mylist)
# print(hash(t))

##----------------substring
# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string) - len(sub_string) + 1):
#         if string[i:i+len(sub_string)] == sub_string:
#             count += 1
#     return count

##-----------string validation
# def string_validation(s):
#     alnum=alpha=num=lo=up=False
#     for x in s:
#         if x.isalnum():
#             alnum=True
#         if x.isalpha():
#             alpha=True
#         if x.isdigit():
#             num=True
#         if x.islower():
#             lo=True
#         if x.isupper():
#             up=True

#     if alnum==True:
#         print("True")
#     else:
#         print("False")
#     if alpha==True:
#         print("True")
#     else:
#         print("False")
#     if num==True:
#         print("True")
#     else:
#         print("False")
#     if lo==True:
#         print("True")
#     else:
#         print("False")
#     if up==True:
#         print("True")
#     else:
#         print("False")
            
# string_validation('qA2')

##-----------Logo
# #thickness = int(input()) #This must be an odd number
# thickness=5
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

##------------Text wrap

# import textwrap
# from textwrap import wrap
# def text_wrap(s,w):
#     a=wrap(s,w)
#     a='\n'.join(a)
#     print(a)

##--------------Split and join string

# def sl_join(s):
#     line=s
#     line=line.split()
#     line='-'.join(line)
#     return line

# print(sl_join('My Name Is Shahzaib'))

##------------------MAt design

# def pattern(h,w):
#     pattern=[]
#     for i in range(1,h,2):
#         line=('.|.'*i).center(w,'-')
#         pattern.append(line)
#     pattern.append("WELCOME".center(w,'-'))

#     for i in range(h-2,0,-2):
#         line=(".|."*i).center(w,"-")
#         pattern.append(line)

#     for x in pattern:
#         print(x)

# h,w=input().rsplit() #w must be h*3
# pattern(int(h),int(w))

##----------------------Dec, Oct< Hexa

# def i_n(n):
    
#     width=len(bin(n))-2
    
#     for x in range(1,n+1):
#         dec=str(x).rjust(width)
#         octal=oct(x)[2:].rjust(width)
#         hexa=hex(x)[2:].upper().rjust(width)
#         binary=bin(x)[2:].rjust(width)
#         print(dec,octal,hexa,binary)
# i_n(12)

##--------------Rangoli pattern Creation
# import string

# def print_rangoli(size):
#     alpha = string.ascii_lowercase
#     lines = []

#     for i in range(size):
#         left = alpha[size-1:i:-1] 
#         right = alpha[i:size]
#         row = '-'.join(left + right)
#         lines.append(row.center(4*size - 3, '-'))

    
#     full_rangoli = lines[::-1] + lines[1:]
#     print('\n'.join(full_rangoli))

# n = int(input("Enter size: "))
# print_rangoli(n)

##--------------------Capitalization
##-----1
s='muhammad shahzaib Khalid'
# first,second=s.split()
# first=[x for x in first ]
# first[0]=first[0].upper()
# first=''.join(first)
# second=[x for x in second ]
# second[0]=second[0].upper()
# second=''.join(second)
# s=first+' '+second
##------2
# sp=s.split()
# print(sp)
# j=''
# for x in sp:
#     a=x[0]
#     a=a.upper()
#     j+=" "+a+x[1:]
# j=j.strip()
# print(j)
##---------3
# print(' '.join(word.capitalize() for word in s.split()))
##-------4

# result=''
# cap=True
# for x in s:
#     if x==' ':
#         cap=True
#         result+=x
#     elif cap:
#         result+=x.upper()
#         cap=False
#     else:
#         result+=x
# return result

##------Minion Game

# s=input('Enter String: ')
# def minion_game(s):
#     vowels='AEIOU'
#     Kevin=Stuart=0
#     for i in range(len(s)):
#         if s[i] in vowels:
#             Kevin+=len(s)-i
#         else:
#             Stuart+=len(s)-i
#     if Kevin > Stuart:
#         print(f"Kevin {Kevin}")
#     elif Stuart > Kevin:
#         print(f"Stuart {Stuart}")
#     else:
#         print("Draw")

# minion_game(s.upper())

##----------Merge the tools

# s='AABCAAADA'
# r=3
# s=input()
# r=int(input())
# mylist=[]
# for x in range(0,len(s),r):
#     mylist.append(s[x:x+r])

# for x in mylist:
#     unique=''
#     for y in x:
#         if y not in unique:
#             unique+=y
#     print(unique)

##---------Eval
# x=5
# s='x+1'
# print(eval(s))     #printing


##---------Athelete sort

# N,M=input('Enter Total Atheletes and Colu count: ').split()
# sheet=[]
# for _ in range(int(N)):
#     sheet.append(input().split())
# k=int(input())
# def Athelete_sort(k,sheet):
#     sheet=sorted(sheet,key=lambda x: int(x[k]))
    
#     for x in sheet:
#         result=''
#         for y in x:
#             result+=' '+y
#         print(result.strip())

# Athelete_sort(k,sheet)

##----------Any or All

# int_list=['1','2','4','1','5']    
# # total=int(input())
# # int_list=input().split()

# if all(int(i)>=1 for i in int_list) and  any(i==i[::-1] for i in int_list):
#     print('True')
# else:print('False')

##-------ginortS
##-----------1
# s='Sorting1234'
# final=''
# result=[]
# even=sorted([x for x in s if x.isdigit() and int(x)%2==0])
# odd=sorted([x for x in s if x.isdigit() and int(x)%2!=0])
# upper=sorted([x for x in s if x.isupper()])
# lower=sorted([x for x in s if x.islower()])
# result=lower+upper+odd+even
# for x in result:
#     final+=x
# print(final)

##----------2
# even=odd=lower=upper=result=final=''
# for x in s:
#     if x.isupper():
#         upper+=x
#     elif x.islower():
#         lower+=x
#     elif x.isdigit():
#         if int(x)%2==0:
#             even+=x
#         else: odd+=x
# result=sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)
# for x in result:
#     final+=x
# print(final)


