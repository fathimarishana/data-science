
def get_dict_input(prompt):
    user_input = input(prompt + " (format: key1:value1 key2:value2): ")
    items = user_input.split()
    result = {}
    for item in items:
        if ':' in item:
            key, value = item.split(':', 1)
            result[key] = value
        else:
            print(f"Skipping invalid item: {item}")
    return result


dict1 = get_dict_input("Enter first dictionary")
dict2 = get_dict_input("Enter second dictionary")
merged1 = dict1.copy()
merged1.update(dict2)
print("\nMerged using update():", merged1)


merged2 = {**dict1, **dict2}
print("Merged using ** operator:", merged2)

try:
    merged3 = dict1 | dict2
    print("Merged using | operator:", merged3)
except TypeError:
    print("Merged using | operator: Not supported in this Python version.")

