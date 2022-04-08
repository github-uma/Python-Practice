file = open("myfile.txt")
print("==========Read All content of file ==============")
# print(file.read())
print("============ Read first 8 characters of file irrespective of line============")
# print(file.read(8))
print("============= Read line by line =============")
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()
print("============= Read all lines and store in list =============")
for line in file.readlines():
    print(line)
file.close()
