# demo = []
# for i in range(0,4):
#     x = input("what is your name?\n")
#     y = x.lower()
#     # if x[0] == "H" or x[0] == "h":
#     #     x = x.lower()
#     if y.startswith("h"):
#         demo.append(y)
# print(demo)

# ================================
# demo = []
# plain = []
# count = 0
# for i in range(0,4):
#     x = input("what is your name?\n")
#     demo.append(x)

# for j in demo:
#     if j in plain:
#         print(f"my output is: {j}")
#     else:
#         plain.append(j)
# =================================
# arr = ["a", "b", "c", "d", "a"]
# demo ={}
# count = 1
# for i in arr:
#     if i in demo:
#         demo[i] = count +1
#     else:
#         demo[i] = 1
# print(demo)
# for i in demo:
#     if demo[i] > 1:
#         print(i)
# for key, val in demo.items():
#     if val > 1:
#         print(key)
#     demo[i] = count 
# print(demo)

# x = {"name":"ali", "age":32}
# print(x["age"])
# x["height"] = 180
# print(x)
# # ================================
# def foo():
#     return(1)
# a = foo()
# print(dir(a))
# ===============================
# def foo(x):
#     for i in x:
#         if i%2 == 0:
#             print(i)
# x = [2, 4, 5, 8, 10, 12]
# foo(x)
# ========================
def foo(name):
    return f"my name is {name}"
name = input("what is your name?")
print(foo(name))