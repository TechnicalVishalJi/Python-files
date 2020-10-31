items = [1,2,3,4,5,6,7,8,9]
items2 = [1,2,3,4,5,6,7,8,9]
items3 = [1,2,3,4,5,6,7,8,9]

def list_sorter1(list):
	list.sort(reverse=True)
	print(list)
def list_sorter2(list):
	a = list[::-1]
	print(a)
def list_sorter3(list):
	lem = len(list)
	list[0],list[lem-1] = list[lem-1],list[0]
	list[1],list[lem-2] = list[lem-2],list[1]
	list[2],list[lem-3] = list[lem-3],list[2]
	list[3],list[lem-4] = list[lem-4],list[3]
	print(list)
	
list_sorter1(items)
list_sorter2(items2)	
list_sorter3(items3)