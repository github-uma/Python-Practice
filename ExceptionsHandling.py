itemCounts = 0
if itemCounts == 0:
    pass
# if itemCounts != 2:
#   raise Exception("Product count is not matched")

assert (itemCounts == 0)

try:
    with open("myfiless.txt", "r") as reader:
        reader.read()
        print("File is opened")
except Exception as e:
    print(e)
finally:
    print("This block execute everytime irrespective of fail or pass")