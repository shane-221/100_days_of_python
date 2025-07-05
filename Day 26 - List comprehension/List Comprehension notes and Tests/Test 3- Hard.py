# Todo: Creating a  master list with all the numbers from both files
list_numbers = []

# Todo; pulling the numbers into the list from both files
with open("file1.txt") as file1:
    content = file1.read().splitlines()
    for i in content:
        i = int(i)
        list_numbers.append(i)

with open("file2.txt.") as file2:
    content = file2.read().splitlines()
    for i in content:
        i = int(i)
        list_numbers.append(i)
print(list_numbers)
# Todo: removing common numbers
# exclude_list =[]
# other_list =[n
#             for n in list_numbers
#             if n not in other_lis
#                 ]
# # result =

# print(result)
