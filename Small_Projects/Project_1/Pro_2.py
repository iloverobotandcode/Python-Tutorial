# Project 2: Finding the Amstrong number

num = int(input("Nhap so tu 3 toi 4 chu so: "))
saveKQ = 0
def factor(num):
    fa=0
    if num >= 100 and num <= 999: fa=3
    elif num > 999 and num <= 9999: fa=4
    return fa


while num < 100 or num > 9999:
    print ("Moi nhap lai: ", end="\t")
    num = int(input())

strNum = str(num)

factor(num)

for i in range (0,len(strNum),1):
    # print (strNum[i], end="\t") 
    check = strNum[i]
    intConv = int(check)
    luythua = 1
    for j in range (0,factor(num),1):
        luythua*=intConv
    saveKQ += luythua

print ("SO Amrstrong la: {}". format(saveKQ))
