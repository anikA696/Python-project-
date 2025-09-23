num = int(input("Enter a number (1-100):"))

i = 1
while i <= num:
   if i % 5 == 0 or i % 7 == 0:
      print(i , "Devisible of 5 or 7")
   
   elif i % 2 == 0:
        print(i, "Even")
   else:
        print(i, "Odd")
   i += 1
