irs = 0
results = []
search_query = input("Search\n").lower()
lis = ["python is best language for beginners","python is a good language","python is not python snake"]

for options in lis:
	if search_query in options:
		results.append(options)
		irs += 1
							
print(f"{irs} results found")
n = 1
for items in results:
	print(f"{n}. {items}\n")
	n += 1
	


