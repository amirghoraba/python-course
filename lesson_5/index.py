# dictionary 
# x = {}
# print(type(x))
# print(isinstance(x, dict))
# demo = {"name":"amir", "familly":"ghoraba", "age":16}
# demo2 = {"name":"amir", "familly":"ghoraba", "age":16}
# not duplicated
# print(demo==demo2)
# demo["age"] = 22
# print(demo == demo2)
# print(id(demo), id(demo2))
# print(demo is demo2)
# changable mutable  ==> unhashable
# =====================================
# iterable orederd
# print(demo)
# for i in demo:
    # print(demo[i])
# ====================================

# arr = [2,4,6,1,3,8]
# target = 10
# demo = {}
# for i in range(len(arr)):
    # for j in range(i+1,len(arr)):
        # if arr[i] + arr[j]== target:
            # print(i, j)

# O(N**2)


# arr = [2,4,6,1,3,8]
# target = 10
# demo = {}
# for key , val in enumerate(arr):
#     print(key, val)
#     if val in demo:
#         print(demo[val], key)
#     demo[target-val] = key
# # print(demo)        
            

# arr = ["a", "b", "c", "d", "a", "t", "a"]
# demo = {}

# a 3 reapeat ======> a
# for i in arr:
    # if i in demo:
        # demo[i] += 1
    # else:
        # demo[i] = 1

# print(demo)













        
        