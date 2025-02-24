# x = "amir"
# print(type(x))
# print(isinstance(x, str))
# print(issubclass(x, type))
# print(dir(str))
# y = input("what is your familly?")
# print(f"my name is {x} and my familly is:{y}")
# for i in x:
#     print(i)
# x[1]="kolsum"
# print(x)
# unchagable or immutable hashable
# y = "amir"
# print(id(x) , id(y))
# ========================================
# arr = [4,8,7,9,64,"amir", {1,5,8},frozenset({88}), "maryam"]
# arr2 = [4,8,7,9,64,"amir", {1,5,8},frozenset({88})]
# print(type(arr))
# for i in arr:
#     print(i, end=" ")
# itarable
# arr[0]="maryam"
# print(arr is arr2)
# mutable ===> unhashable
# target = class str 
# for i in arr:
#     if isinstance(i, str):
#         print(i)
# for i in arr:
#     if type(i) == str:
#         print(i)
# count = 0
# while count < len(arr):
#     if isinstance(arr[count], str):
#         print(arr[count])
#     count += 1
# ============================================
# tuple
# x = (1,2,5,4,7)
# print(type(x))        
# print(isinstance(x, tuple))
# for i in x:
# x[0]= "amir"
# print(x)
# y = list(x)
# y[0] = "amir"
# print(tuple(y))
# print(dir(tuple))
# print(x.index(5))
# =====================================
# dic 
# d = {"name":"amir", "age":15, "name":"maryam"}
# print(d)
# print(d["name"])
# for key, val in d.items():
#     print(key , val)

# arr = [1,2,5,8,5,4,3,2,5]
# x = {}
# for i in arr:
#     if i in x:
#         x[i] +=1
#     else:
#         x[i] = 1
# print(x)
# =====================================
# arr = ["potato","tomato","benana","apple"]

# for i in range(len(arr)):
#     x = input("what do you want?\n")
#     if x in arr:
#         print("you buy it before you choose another fruit")
#     else:
#         arr.append(x)

# print(arr)
# ======================================
# chance = 5
# openion = 3
# arr = []
# import random 
# for i in range(5):
#     guess = random.randint(0,20)
#     # guess = int(input("what is the first guess?\n"))

#     if guess == openion:
#         print("you win")
#         break
#     elif guess != openion:
#         arr.append(guess)
#         chance -= 1
#         print(f"you lost and you have {chance} times")
#     else:
#         if chance == 0:
#             print("you lost")
#             break
# print(arr)

# ================================
# import random
# arr = ["apple", "banana", "melon", "lemon", "cucember", "potato", "tomato","orange", "struberry", "mango"]
# openion = "apple"
# chance = 3
# arr2 = []
# for i in range(3):
#     guess = random.choice(arr)
#     if guess == openion:
#         print("you win")
#         break
#     elif guess != openion:
#         chance -= 1
#         print(f"you have {chance} time ")
#         arr2.append(guess)
#     else:
#         print("you lost")
#         break
# print(arr2)
# =====================================
import random
arr = []
for i in range(3):
    number = random.randint(0,10)
    arr.append(number)
count = 0
for i in arr:
    count +=i
print(count)
print(count/len(arr))
    
    








    

    








# ========================================
# arr = [4,7,8,7,9,34,5,7,8,9]
# demo = {}
# for i in arr:
#     if i in demo:
#         demo[i] += 1
#     else:
#         demo[i] = 1
# print(demo)