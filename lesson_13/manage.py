# import random
# arr = ["amir", "baba", "soheyl", "geeks", "geeg", "fadak"]

# # for i in arr:
# #     if i == i[-1:-len(arr)-1:-1]:
# #         print(i)
# # # =======================================
# target = "geeg"
# demo = []
# count = 3
# for i in range (1,4):
#     x = random.choice(arr)
#     if x == target:
#         print("python you win")
#         break
#     if x != target:
#         count -= 1
#         demo.append(x)
#         with open("fail.txt","a") as f:
#             f.write(f"you made a mistack: {x}\n")
#         print(f"python you have {count} chance")
#     if count == 0:
#         print("python you lose")
#         break
# print(demo)
# =========================================
# with open("demo.txt", mode="a") as file:
    # file.write("hallet chetore\n")


# with open("demo.txt", "r") as file:
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.read(20))
    # print(file.readlines())
import csv

# with open("teacher.csv", 'a') as f:
#     demo = ["firstname", "lastname", "course"]
#     x = csv.DictWriter(f, fieldnames=demo)
#     dictheader = x.writeheader()
#     dictrow = x.writerows([{
#         "firstname":"kolsoum",
#         "lastname":"akbari",
#         "course":"php"
#     },
#     {
#         "firstname":"saed",
#         "lastname":"akbari",
#         "course":"php"
#     }]

#     )



# with open("teacher.csv") as m:
#     x = csv.reader(m)
#     for i in x:
#         print("".join(i))


# with open("demo1.txt", "x") as r:
#     r.write("hello")

# ========================================
# def foo(name, x, y):
    
#     print(x + y)
# foo("amir", 5, 9)

# ================================
# def foo(name):
#     print(f"my name is: {name}")

# x = input("what is your name?\n")

# def foo(x, y ,z, *args, **kwargs):
#     print(x)
#     print(kwargs)
# foo(5, 8 ,9, 88,65,32, name="amir")
# ===========================
