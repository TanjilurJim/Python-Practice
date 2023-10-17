email = input("please enter your mail id: ")

if " " in email:
    print("Remove the space")

elif "@" in email:
    atrate = email.find("@")

    print("user id: ", email[:atrate])
    print("domain : ", email[atrate+1:])



else:
    print("please use a valid mail")


# Solution 2

# email = input("Please enter your email address: ")
#
# if "@" in email:
#     # Find the index of the "@" symbol
#     at_index = email.index("@")
#
#     # Extract the user ID and domain name
#     user_id = email[:at_index]
#     domain_name = email[at_index + 1:]
#
#     print("User ID:", user_id)
#     print("Domain Name:", domain_name)
# else:
#     print("Invalid email address. Make sure it contains the @ symbol.")
