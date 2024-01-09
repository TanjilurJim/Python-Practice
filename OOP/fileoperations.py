file = open("data.txt","r")

lines = file.readlines()
# print(line, end='')
# line2 = file.readlines()
# print(line2)

# for line in lines:
#     print(line, end='')

# Flush mode same as buffer

# Opening a file in write mode
file = open("example.txt", "w")

# Writing data to the file
file.write("Hello, World!\n")
file.write("This is an example of flush.\n")

# Flushing the internal buffer - this sends the data to the disk
file.flush()

# You can continue writing to the file after flushing
file.write("More data after flushing.\n")

# Always remember to close the file at the end
file.close()



# Now, open the file in read mode to read its contents
with open("example.txt", "r") as file:
    # Read the entire content of the file
    content = file.read()
    print(content)
