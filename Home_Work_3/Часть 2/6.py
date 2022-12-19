
d = {"name1": "id1", "name2": "id2", "name3": "id3"}
d_new = {}
for name, id in d.items():
	d_new[id] = name
print(d_new)