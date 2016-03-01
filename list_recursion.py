Converts a multilevel list in a single-level list

data = []
def list_recursion (data,lista):
	for item in data:
		if isinstance(item, list):
			return list_recursion(item, leveled_list)
		else:
			leveled_list.append(item)
			return data
