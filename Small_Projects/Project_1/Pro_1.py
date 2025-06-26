# Project 1: Making an auto-generate set of multiplication table 
print ("\nMULTIPLICATION TABLE")

for i in range (2,10):
    for j in range (1,11):
        product = i*j
        print ("| {}*{} = {}|".format(i,j, product))
    print("\n")
