##------------------Tuple

#mytuple=("apple","banana","mango","pineapple")
# print(mytuple)
# print(mytuple[2])

# print("--------------Unpacking tuple")
# mytuple=("apple","banana","mango","pineapple")
# x,y,z,a=mytuple
# print(x,y,z,a)

# mytuple=("apple","banana","mango","pineapple")
# b,*c,d=mytuple         ##will assign mutiple values to 'c' as list
# print(b,c,d)

# ##------------------Access
#mytuple=("apple","banana","mango","pineapple")
#mytuple[0]="peach"      ##will throw error, no assignment allowed
#print(mytuple[0:3])

##-------------------modification

#mytuple.add("peach")    ##error

# x=list(mytuple)
# x.append("peach")
# x.insert(0,"orange")
# mytuple=tuple(x)
# print(mytuple)


##-------------------remove
# #mytuple.pop() ##error
#mytuple.remove("mango")

# x=list(mytuple)
# x.remove("mango")
# x.pop()
# mytuple=tuple(x)
# print(mytuple)

##-----------------join

# ytuple=("guava","pomegrant")
# mytuple+=ytuple
# print(mytuple)


##----------join by loop

# ytuple=("guava","pomegrant")
# for x in ytuple:
#     mytuple.append(x)  ## error
# print(mytuple)


##----------------Copy

# ytuple=mytuple.copy()       ##error
# print(ytuple)

# mylist=["apple","banana","mango","pineapple"]
# ylist=mylist.copy()
# print(ylist)


##-----------------sets

#myset={"Mango","Banana","Melon","Peach"}
# for x in myset:
#     print(x)

##----------------access

# for x in range(len(myset)):
#     print(myset[x])     ##error

# myset.add("Apple")
# print(myset)

# mylist=["Pomegrant","Cheery","Banana"]      
# myset.update(mylist)        ##no duplication, adding list in set
# print(myset)

##---------------add

# nwset={0,True,"True","0"}
# nwset.add(False)        ##no change
# print(nwset)
# nwset.add(1)            #no change
# print(nwset)
# nwset.add("False")
# print(nwset)
# nwset.add("True")       #no change
# print(nwset)

##------------methods

# set1={1,2,3,4,5}
# set2={2,5,6,7,8}
# set3={2,3}
# #set1|=set2
# #print(set1)
# print(set1>=set3)       ##True set1 is superset 
# print(set1<=set3)       ##False set1 is subset of set3
# print(set3<=set1)       ##True set3 is subset of set1
# print(set1^set2)        ##symentric_differ (all except dupli)
# print(set1-set2)        ##unique of set1
# print(set1&set2)        ##only dupli

# set1=set1-set2
# print(set1)


##-------------------remove

myset={1,2,3,4,6,(1,2,3,4),5,(2,3,4,5,6,7)}

# def func(anyset):

#     intuple=[x for x in anyset if isinstance(x,tuple)]

#     for y in intuple:
#         anyset.remove(y)
#         newtuple=tuple(z for z in y if z not in (2,4))
#         anyset.add(newtuple)
    
    # for x in anyset:
    #     if isinstance(x,tuple):
    #         original=x
    #         break
    
    # anyset.remove(original)

    # newtuple=tuple(x for x in original if x not in (2,4))
    # anyset.add(newtuple)

# func(myset)
# print(myset)


# myset[0]="Mango"                 ##error
# print(myset)
#fruits={"mango","banana","peach",("lemon","orange"),"apple",("leachy","apricot","orange","banana")}
# print(myset)

# aset={1,2,3,4,{1,2,3,4}}        ##error caz set is not hashable
# print(aset)

# bset={1,2,3,4,[1,2,3,4]}        ##error caz list is not hashable
# print(bset)

# myset.remove((1,2,3,4))
# print(myset)

# myset.pop()
# print(myset)
# print(fruits)
# fruits.pop()
# print(fruits)

##---------------------------------
# print(myset)
# x=list(myset)
# x[0]="Change"
# myset=set(x)
# print(myset)


# print(fruits)
# x=list(fruits)
# x[0]="Change"
# fruits=set(x)
# print(fruits)


###-----------------------Dict

# thisdict={
#     "Brand":"Lexus",
#     "Model":"LC300",
#     "Year":2025

# }

# print(thisdict)
# print(thisdict["Brand"])
# print(len(thisdict))
# print(thisdict.keys())
# print(thisdict.get("Brand"))
# print(thisdict.values())
# print(thisdict.items())


##---------------update

# thisdict["Color"]="White"
# print(thisdict)

# thisdict["Year"]=2026
# print(thisdict)

# if 2025 in thisdict:        ##retunrs nothing because it check keys
#     print("yes")

''' in this case both are true but only if will be executed
if 2025 in thisdict.values():
    print("Found in values")
elif "Year" in thisdict:
    print("elif")
'''

# if 2025 in thisdict.values():
#     print("Found in values")
# if "Year" in thisdict:
#     print("elif")


#thisdict.update({"Color":"white","Brand":"Lamborghini"})
# print(thisdict)

##thisdict.update({["name","age"]:("Shahzaib",50)})       ##error mutable used
##print(thisdict)

# thisdict.update({("type","wheel"):{"coupe",4}})
# print(thisdict)

# thisdict.update({("name","age"):["Shahzaib",50]})
# print(thisdict)

# thisdict.update({("second_name","height"):("Shahzaib",5.9)})
# print(thisdict)

##----------------remove

# thisdict.pop("white")       ##error not key value
# print(thisdict)

## thisdict.pop("Color")    
## print(thisdict)

# thisdict.popitem()
# print(thisdict)

##----------------Loop
# print("----------------------------------------")
# for x in thisdict:
#     print(x)
# print("----------------------------------------")
# for x in thisdict:
#     print(thisdict[x])
# print("----------------------------------------")
# for x in thisdict.keys():
#     print(x)
# print("----------------------------------------")
# for x in thisdict.values():     ##return key and its value as tuple
#     print(x)
# print("----------------------------------------")
# for x in thisdict.items():
#     print(x)
# print("----------------------------------------")
# for x,y in thisdict.items():
#     print(x,y)

## for x in thisdict.items():
##     print(thisdict[x])

## for x in thisdict.keys():
##     print(thisdict[x])

##-------------Nested Dict

Toyota={
    "Sedan":{"Name":"Crown","Model":2025},
    "SUV":{"Name":"Fortuiner","Model":2025},
    "Pickup":{"Name":"Tundra","Model":2025}
}

Hatchback={"Name":"Aqua","Model":2025}
Coupe={"Name":"Eq","Model":2020}

# print(Toyota.keys())
# print("-----------------------------")
# print(Toyota.values())
# print("-----------------------------")
# print(Toyota.items())


Toyota["Hatchback"]=Hatchback
Toyota["Coupe"]=Coupe


# print(Toyota.keys())
# print("-----------------------------")
# print(Toyota.values())
# print("-----------------------------")
# print(Toyota.items())

checkdict={"Toyota":Toyota}
# print(checkdict)



##--------------------Iteration

# print(Toyota["Hatchback"].items())
# print(Toyota["Hatchback"]["Name"])
# print(Toyota["Hatchback"])

# for x,obj in Toyota.items():
#     print(x)
#     for y in obj:
#         print(y,":",obj[y])

# print("---------------------")

# for inner_dic_name, inner_info in Toyota.items():
#     print(inner_dic_name)
#     for kys in inner_info:
#         print(kys,":",inner_info[kys])

