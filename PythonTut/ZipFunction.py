names = ("Navin", "Kiran", "Asha")
comps = ("Google", "Telusko", "YouTube")

zipped = list(zip(names,comps))
zipped2 = dict(zip(names,comps))

print(zipped)
print(zipped2)

for (a,b) in zipped:
	print(a,b)