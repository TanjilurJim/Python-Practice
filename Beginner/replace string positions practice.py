#take input from user and replace the first and 2nd letter, 3rd and 4th, 5th and 6th

# input_str = input("Please enter a string: ")
# output_str = ""
#
# for i in range(0, len(input_str) - 1, 2):
#     output_str += input_str[i + 1]  # Add the next character
#     output_str += input_str[i]      # Add the current character
#
# if len(input_str) % 2:  # Check if the string length is odd
#     output_str += input_str[-1]  # Add the last character
#
# print(output_str)

#another way of doing it

input_str = input("please enter an input: ")

str_li = list(input_str)

for i in range(0, len(str_li)-1, 2):
    str_li[i], str_li[i+1] = str_li[i+1], str_li[i]  # Swap adjacent characters

output_str = ''.join(str_li)
print(output_str)
