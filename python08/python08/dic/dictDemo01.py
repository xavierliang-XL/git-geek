#"name":"david" items
#Key     Value
def returnItems(dict):
    """
    this method is to return the items on the dictionary
    dict:dictionary
    """
    return dict.items()
dict={"name":"david","age":14,"gender":"M"}
# dict['name'] = 'Rose'
# print(dict["name"])

print(returnItems(dict))
