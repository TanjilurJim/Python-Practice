#take a string as an input then lowercase it, uppercase it, swap cases capitalize it

def str_operations(s):
    capitalized = s.capitalize()
    lowercased = s.lower()
    uppercased = s.upper()
    swapped = s.swapcase()
    casefolded = s.casefold()

    return capitalized, lowercased, uppercased, swapped, casefolded


string_input = input('Please enter a string: ')

capitalized, lowercased, uppercased, swapped, casefolded = str_operations(string_input)

print(f"Capitalized: {capitalized}")
print(f"Lowercased: {lowercased}")
print(f"Uppercased: {uppercased}")
print(f"Swapped Cases: {swapped}")
print(f"Casefolded: {casefolded}")