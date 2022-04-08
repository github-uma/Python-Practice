with open("myfile.txt", "r") as reader:  # file open in read mode and close in the end
    content = reader.readlines()
    with open("myfile.txt", "w") as writer:  # file open in write mode and close in the end
        for line in reversed(content):
            writer.write(line)

