people = [
	{"name":"Ron", "club":"MUFC"},
	{"name":"Roon", "club":"DC United"},
	{"name":"Ruud", "club":"PSV"}
]

# def func(person):
# 	return person["name"]

# people.sort(key=func)

people.sort(key=lambda person: person["name"])

print(people)