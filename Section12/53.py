

# def pair_sum(arr, k):
#     paris = 0
#     used_number = []
#     for index, num in enumerate(arr):
#         print(arr)
#         if num < k:
#             reminder = k - num
#             if reminder in arr:
#                 print(num, reminder)
#                 paris += 1
#     return paris
# def pair_sum(arr, k):
#
#     if len(arr) < 2:
#         return
#
#     seen = set()
#     output = set()
#
#     for num in arr:
#
#         target = k - num
#         if target not in seen:
#             seen.add(num)
#         else:
#             output.add((num, target))
#
#     print(output)
#     print(seen)
#     return len(output)
#
#
# print(pair_sum([1, 3, 2, 2], 4))

# print([3, 2, 2].index(2))
print(sorted([3, 5, 1, 2]))