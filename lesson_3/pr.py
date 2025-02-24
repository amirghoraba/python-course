
# x = 10
# for i in range(10,0,-1):
    # x = x - i
    # print(x)
    # ======================
# i = 0
# while i < 10:
    # i=i + 1
    # if i % 2 == 0:
        # print(i)
# ====================================
# i = 0 
# while i < 10:
    # i=i + 1
    # if i ==  8:
        # break
    # print(i)
# ===================================
# name = "amir ghoraba"
# for i in range (0,len(name)):
    # if name[i] =="o":
        # print(i)
# =======================================
count = 0
name = "amir ghoraba"
target = "a"
# for i in name:
#     if i == target:
#         count = count + 1

for i in range(len(name)):
    if name[i] == target:
        count += 1
print(count)

# this is practice
# ===========================================
# for i in range (2):
    # for j in range (2):
        # print(j)
# =========================================
# for i in range(5,0,-1):
    # for j in range(i):
        # print("*", end = " ")
    # print("@")
    # this is practice
# ============================================
arr =[1,2,3,4,88,12,14]
for i in range (len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j] < arr[i]:
            arr[j] , arr [i] = arr[i] , arr[j]
print(arr)
# =================================================
# arr = [1,2,3,4,88,12,14]
# arr.sort()
# print(arr)
# ============================
# i= 0
# name = "amir ghoraba"
# target = "o"
# for i in range(len(name)):
#     while i< len(name)-1:
#      i = i + 1
#      if name[i]== target:
#         print(i)
#     break
# #  ====================================         
    