# x = 3
# y = float(3)
# print(x,y)

# values = [1,2.23,5,7,2,30,15]
# print(values[7])
# for i in values:
#     print(i)

# x = "this is a thing"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)

""" F = input("type here      ")
y = F.split()
z= 0
for i in y:
    z += 1
    print (z) 
 """

# x = "test"
# print(f"hello {x}")


# temp = input("input ur temperuateurte   ")
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')      
# else:
#     print('cold')


bill = int(input("BILL:    "))
tip =input("Would you like to tip? Y/N      ")
if tip == "N":
   print(bill)
elif tip == "Y":
   service=input("How good was your service , bad okay good or great??         ")
   if service == "bad":
      print(bill*1)
   elif service == "okay":
      print(bill*1.15)
   elif service == "good":
      print(bill*1.20)
   elif service == "great":
      print(bill*1.25)










