# Project 3: Auto-check whether the input is an integer
num = input("Mời bạn nhập số NGUYÊN: ")
list_num = list(num)
len_num = len(num)
list_numIn = ["0","1","2","3","4","5","6","7","8","9"]

def checkInt ():
    count = 0
    for check in range (len_num):
        if list_num[check] in list_numIn:
            count = count + 1
        else:
            continue
    return count
checkInt()

while checkInt() != len_num:
    print ("Kí tự bạn vừa nhập không thuộc số NGUYÊN !!!!")
    num = input("Mời bạn nhập lại: ")
    list_num = list(num)
    len_num = len(num)
    checkInt()

print ("Số bạn vừa nhập {} thỏa số nguyên".format(num))
