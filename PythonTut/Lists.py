nums = [1,32,52,12,26,112,63]
names = ["naomi", "tchalla", "ross","robby"]

print(names)
print(nums)

print(nums[-3])
print(nums + names)

nums.insert(2,69)
print(nums)

nums.remove(69)
print(nums)

nums.pop(3)
print(nums)

nums.append(39)
print(nums)

nums.extend([26,76,5])
print(nums)

nums.sort()
names.sort()
print(nums+names)


