name_list=['david','xavier','alan','jim']
print(name_list)
#del:删除指定元素
del name_list[0]
print(name_list)
#pop():从list中弹出指定元素
name=name_list.pop(0)
print(name_list,name)
#remove():删除列表中指定元素（第一个匹配的）
name_list.remove('alan')
print(name_list)
#clear:清空list
name_list.clear()
print(name_list)
