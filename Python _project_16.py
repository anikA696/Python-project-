file = open("test.txt","w")

file.write("Anika\n")
file.write("Anas")
file.close()
file = open("test.txt","r")
content= file.read()
print(content)
file.close()
