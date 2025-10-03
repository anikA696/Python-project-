file = open("test.txt","w")

file.write("Anika\n")
file.write("Anas\n")
file.close()

file = open("test.txt","a")
file.write("Ali\n")
file.write("Sara")
file.close()

file = open("test.txt","r")
content= file.read()
print(content)
file.close()
