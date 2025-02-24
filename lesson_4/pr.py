print("choose your choice")
print("1.plus")
print("2.minus")
print("3.times")
print("4.divided")

demo = True
while True:
    choice = input("choose your choice 1/2/3/4\n")
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("enter first num\n"))
        num2 = int(input("enter second num\n"))
        if choice== '1' :
            print(num1 + num2)
        elif choice== '2':
            print(num1 - num2)
        elif choice== '3':
            print(num1*num2)
        elif choice== '4':
            print(num1 / num2)
        x = input("do you want to continue?\n")
        if x == "yes" or x == "yes".upper() or x == "y":
            print()
        else :
            print("good luck")
            demo = False
            break
    else:
        demo = False
        break
#   =============================================================
# total = 0
# arr = [95, 76, 85, 43, 25, 15, 30, 38]
# for i in arr:
#     total = total + i
# print(total)  
# this is practice
# =======================================================

