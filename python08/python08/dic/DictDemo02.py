# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# for key, value in dict1.items():
#     print(f'{key} = {value}')

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
def printItems(dict1):
        """
        this method is to print the items in a dictionary
        dict1:dictionary
        """
        for item in dict1.items():
                print(item)
print(printItems(dict1))