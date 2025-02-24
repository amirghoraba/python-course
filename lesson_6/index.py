# arr = ["a", "b","a", "c", "d", "c", "c"]
# demo = []
# for i in arr:
#     if i in demo:
#         print(i)
#     else:
#         demo.append(i)
# dic = {"name":"amir", "age":15}
# print(dic["name"])
# demo ={}
# for i in arr:
#     if i in demo:
#         demo[i] +=1
#     else:
#         demo[i]=1
# max_val = max(demo.values())
# for key, value in demo.items():
#     if value == max_val:
#         print(key)
# =============================
demo = { "familly":"ghoraba", 5:["python","php", "html",15], "name":"maryam"}
# for index, value in demo.items():
#     print(index, value)
# print(demo["course","age"][1, 3])

# x = "amir"
# x[0]="q"
# print(x)
# changable == mutable ===> unhashable/ ("list", "dict")
# unchangable == immutable ==> hasahble ("str", "int","tuple")
# not douplicated
# ================================================
# print(dir(demo))
# print(demo.get("name"))
# y = {"color":"red"}
# demo.update(y)
# print(demo)
# print(demo.pop("name"))
# demo.popitem()
# x = demo.copy()
# demo.clear()
# demo.setdefault("color", "green")
# demo.fromkeys("amir",5)
# print(demo)
# print(help(demo))
# =======================================================================
items = [
    {"name":"apple", "type":"fruite"},
    {"name":"carrot", "type":"vegetable"},
    {"name":"orange", "type":"fruite"},
    {"name":"brocoli", "type":"vegetable"},
]

demo = {}
for i in items:
    if i['type'] in demo:
        demo[i["type"]].append([i])
    else:
        demo[i['type']]=[i]
print(demo)
