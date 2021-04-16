# import random
# a = [random.randint(0, 10000) for i in range(1000)]
# mSort = True
# i = 0
# while mSort:
#     print(a)
#     if a[i] >  a[i+1]:
#         r = a[i]
#         a[i] = a[i + 1]
#         a[i + 1] = r
#         i = 0
#     else:
#         i+=1
#     if i == len(a)-1:
#         mSort = False
#         print(a)
import random
a = [random.randint(0, 100) for i in range(10)]
nums = []
for i in range(len(a)):
