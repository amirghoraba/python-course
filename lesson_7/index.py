# x = {15,16,17}
# # print(x)

# y = {"amir", "ali"}
# print(y)
# not ordered
# s = {1,6,7,8,2,1}
# a = {1,6,7,8,2,1}
# print(len(s))
# not duplicated
# print(type(s))
# print(isinstance(s, set))
# for i in s:
    # print(i)
#iterable

# a = {"amir"}
# print(s + a)
# print(s[0])
# s[0] = "amir"
# print(s)
# immutable unchangable
# print(s is a)
# unhashable 
# dic = {"name":"amir", {2}:"kolsoum"}
# print(dic)
# s = {1,2,{5,6,8},"amir"}
# print(s)
# f = frozenset({5,6,9,8})
# f2 = frozenset({5,6,9,8})
# print(type(f))
# print(f is f2)
# f[0] = "amir"
# immutable
# iterable
# s = {1,2,frozenset({5,6,8}),"amir"}
# print(s)
# print(dir(set))
# s = {4}
# a = frozenset({3,4})
# s.add(a)
# print(s)
# s = set({4,5,6, 7, 8, 9})
# a = {5,8,7}
# e = {"amir"}
# s.update(e)
# s.add(e)
# print(s)
# s.pop()
# s.discard(15)
# print(s.intersection(a))
# s.clear()
# s.intersection_update(a)
# s.remove(5)
# print(a.difference(s))
# print(dir(set))
# s.symmetric_difference_update(a)
# print(a.issubset(s))
# print(s.issuperset(a))
# s.union(a)
# print(s)


# arr = [5, 8, 9, 7, 44,11]
# target = 8
# index = 0
# for i in arr:
    # if i == target:
        # index=+1
        # print(index)
#  =======================================================       
# name = "amir ghoraba"
# target = "r"
# for i in name:
#     if i == target:
#         continue
#     print(i)
# ===========================================================
arr = [5, 8, 9, 55, 7, 44,11] 
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        if arr[j] < arr [i]:
            arr[j],arr[i]=arr[i],arr[j]
print(arr)
#  ===========================================================   
  






