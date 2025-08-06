# Program 1 Write a program to find the index of an element in a tuple.
my_tuple = (10, 20, 30, 40, 50, 30)

element = int(input("Enter the element to find index: "))

if element in my_tuple:
    index = my_tuple.index(element)
    print(f"The index of {element} is {index}")
else:
    print(f"{element} is not in the tuple.")


# Program 2 Convert a tuple into list and sort them 
my_Tuple = (10,85,45,78,41,74,23)

new_list = list(my_Tuple)

new_list.sort()

print(f"Sorted List is: {new_list}")

# Program 3 Merge two dictionaries and print the result.
my_Dict = {"Cars": "BMW", "Year": 1986, "Color": "Black"}
my_Dict2 = {"Model": "M5cs", "Engine": "V8"}

my_Dict.update(my_Dict2)

print(f"The Merged Dictionary is {my_Dict}")

# Program 4 Given a list of numbers, remove all duplicates and print the result.
numbers = [10, 20, 30, 20, 40, 10, 50, 30]

unique_numbers = list(set(numbers))

unique_numbers.sort()

print("Updated List:", unique_numbers)
