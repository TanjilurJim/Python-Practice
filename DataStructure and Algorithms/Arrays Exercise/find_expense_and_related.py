# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses = {'january':2000, 'february':2350, 'march':2650,'april':2130,'May':2190}

exp_lst = [(k) for k in expenses.values()]

# print(exp_lst)

#1
print("In february you spent:",exp_lst[1]-exp_lst[0], "more than januray")
# 2
print("Total spent in the first quarter is: ",sum(exp_lst[:3]))
# 3
if 2000 in exp_lst:
  print("yes, 2000 is in the list", end=" ")
  print("it is in ",exp_lst.index(2000),"th index")

# 4
# expenses.update({'June':1980})
# print(expenses)
exp_lst.append(1980)
print(exp_lst)

#5
print("expenses after the return of 200 dollar of april: ", exp_lst[3]-200,"dollar")
