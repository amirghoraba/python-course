# tuple 
# arr = [1,2,3,4,5]
# x = tuple(arr)
# print(type(x))
# t = (1,5,6,9,8)
# for i in t:
#     print(i)
# iterable
# ordered
# unchangable immutable ===> hashable
# x = "siyamak"
# x[1]="q"
# print(x)
# a = list(t)
# a[0]="amir"
# r = tuple(a)
# # t[0]="amir"
# print(r)
# ===================================
# t = ("amir",)
# print(type(t))
# ================================
# a = (5,4)
# b = (6,8)
# print(a+b)
# print(dir(tuple))
# t = ("amir",5, "arash", 5,8,9)
# print(t.count(5))
# print(t.index(5,2))
# ===================================
# SEt 
# s = {1,5,"amir", {"age":15}}
# print(type(s))
# not ordrede
# print(len(s))
# del s
# print(s[0])
# not duplicated
# immutable unchangable ==> unhashable
# frozenset == >hashable
# print(s is d)
# d = d+s
# print(d)
# w = {"name":"amir", "age":[15,20,18]}
# print(w)
# print(dir(d))
# print(d.union(s))
# print(d.difference(s))
# print(d.symmetric_difference(s))
# d.symmetric_difference_update(s)
# d.update({99999})
# d.pop()
# d.remove(1)
# d.intersection_update(s)
# print(d.issuperset(s))
# print(s.issubset(d))
d = {1,5,"amir",5, frozenset({55})}
s = {"amir", 5,8888}
# for i in d:
#     for j in s:
#         if j is i:
#                  print("true")
#              break
#         else:
#              print(False)
demo = {}
for i in d:
    if i in demo:
        demo[i] += 1
    else:
        demo[i] = 1
print(demo)
for j in s:
    try:
        if  demo[j] and demo[j] ==1:
             print(True)
    except:    
        raise KeyError("s are not in demo")
        
    
         