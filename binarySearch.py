
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
 
#     while low <= high:
 
#         mid = (high + low) // 2
 
#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1
 
#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1
 
#         # means x is present at mid
#         else:
#             return mid
 
#     # If we reach here, then the element was not present
#     return -1

# def binary_search(arr, x):
    
#     middleIndex = len(arr) // 2

#     if arr[middleIndex] > x :
#         new = arr[0:middleIndex+1]
#         for n in new:
#             if n == x:
#                 return True
#             else:
#                 return False
#     elif arr[middleIndex] == x :
#         return True

#     elif arr[middleIndex] < x:
#         new = arr[middleIndex:]
#         for n in new:
#             if n == x:
#                 return True
#             else:
#                 return False

# Test array
# arr = [ 2, 3, 10, 20, 40 ]
# x = 9

# def search(arr, x):
#     for i in arr:
#         if i == x:
#             return True
#         return False
 
# # # Function call
# # result = binary_search(arr, x)
# # print(result)

# result = search(arr, x)
# print(result)


# def swap_1(x,y):
#     x,y = y,x
#     return x,y

# def swap_2(x,y):
#     tmp = y
#     y = x
#     x = tmp
#     return x,y

# print(swap_1(5,6))
# print(swap_2(7,8))

# area = [[2,3],[4,5],[6,7]]
# c = []
# for k in area:
#     c.append(sum(k))
# print(sum(c))

# s = '123456'
# n = list(s)
# n.sort(reverse=True)
# final = ''.join(n)
# print(final)
# print(s[::-1])

# def removeElement_1(nums, val) -> int:
#     notDone = True
#     while(notDone):
#         if val in nums:
#             nums.remove(val)
#         if val not in nums:
#             notDone = False

#     return print(nums)

# def removeElement_2(nums, val) -> int:
#     while(True):
#         try:
#             nums.remove(val)
#         except:
#             return print(len(nums))
# removeElement_1(nums = [0,1,2,2,3,0,4,2], val = 2)
# removeElement_2(nums = [0,1,2,2,3,0,4,2], val = 2)


# def removeDuplicates(nums) -> int:
#     for i in nums:
#         if nums.count(i) >1:
#             nums.remove(i)
#         return print(len(nums))
# removeDuplicates([1,1,1,1])

# array1 = [1,None,2,3,None,None,5,None]

# def solution(array):
#   new = []
#   tmp = 0
#   for num in array:
#       if num is not None:
#           new.append(num)
#           tmp = num
#       else:
#           new.append(tmp)
#   return print(new)

# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# a = [8,1,2,2,3]
# def smallerNumbersThanCurrent(nums):
#     result = []
#     count = 0
#     for idx in range(len(nums)):
#         current_nums = nums[idx]
#         nums.remove(current_nums)
#         for n in nums:
#             if current_nums > n:
#                 count += 1
#                 result.append(count)
#             elif current_nums == n:
#                 result.append(0)
#     return print(result)

# smallerNumbersThanCurrent(a)