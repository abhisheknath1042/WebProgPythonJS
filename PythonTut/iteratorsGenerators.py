# class TopTen(object):
#     """docstring for ClassName"""
#
#     def __init__(self):
#         self.num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <= 10:
#             val = self.num
#             self.num += 1
#
#             return val
#         else:
#             raise StopIteration
#
#
# values = TopTen()
#
# print(next(values))
#
# for i in values:
#     print(i)

def topten():
    n=1

    while n<=10:
        sq = n*n
        yield sq
        n+=1


values = topten()

for i in values:
    print(i)