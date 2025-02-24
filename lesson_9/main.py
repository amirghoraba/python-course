# x :int = 1
# print(x)

# def foo():
#     return(1+4+5+9+7)
# y = foo()
# print(y)
# =============================\
# def foo(x):
#     return x
# print(foo(4))
# ================================
# def foo(name:str) -> str:
#     return f"my name is : {name}"
# print(foo("amir"))
# ===============================
# def foo(name, familly):
#     return f"my name is:{name} and my familly is : {familly}"
# x = input("what is your name?\n")
# z = input("what is your familly?\n")
# y = foo(x, z)
# print(y)
# ================================
# arr = [8,9,7,3,10,4,6,5,1]
# arr.sort()
# def foo(arr, target):
#     arr.sort()
#     first = 0
#     last = len(arr)-1
#     while first < last:
#         mid = (first+last) // 2
        
#         if arr[mid] == target:
#             return(mid)
#         elif arr[mid] < target:
#             first = mid+1
#         else:
#             last= mid -1
#     return -1
# target=4
# print(foo(arr, target))
# ==========================================
# def foo(a, b, c, *args, **kwargs):
#     # print(type(args))
#     print(args)
#     print(kwargs)
#     return a , b , c
# print(foo(2,8,7, {8,9,7,88}, name="amir"))
# ==================================
# arr = [5,6,9,8]
# {}
# arr = [False, 1,0,8,9,0,"amir"]
# output = False,1,8,9,"amir",0,0

# packing unpacking
# ====================================