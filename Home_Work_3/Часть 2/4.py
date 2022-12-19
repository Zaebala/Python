
list1 = [1, 4, 1, 6, "Hello", "a", 5, "Hello"]
list2 = []

for i in list1:
	if i not in list2:
		list2.append(i)
for i in list2:
	if i in list1:
		list1.remove(i)
print(list1)