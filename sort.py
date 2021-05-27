arr = [1,2,5,3,7,8,6,4]

# def bubbleSort(arr):
# 	swapped = True
# 	while (swapped):
# 		swapped = False

# 		for i in range(len(arr)-1):
# 			if (arr[i] > arr[i+1]):
# 				swapped = True

# 				tmp = arr[i]
# 				arr[i] = arr[i+1]
# 				arr[i+1] =tmp
# 	return print(arr)
# print("bubbleSort")
# bubbleSort(arr)
# print("\n")

# def insertionSort(arr):
# 	for i in range(len(arr)):
# 		j = i

# 		while(j>0 and arr[j] < arr[j-1]):
# 			c += 1
# 			tmp = arr[j]
# 			arr[j] = arr[j-1]
# 			arr[j-1] = temp
# 			j -= 1
# 	return print(arr)
# print("insertionSort")
# insertionSort(arr)
# print("\n")

# def heapify(arr, n, i): 
#     largest = i  # Initialize largest as root 
#     l = 2 * i + 1     # left = 2*i + 1 
#     r = 2 * i + 2     # right = 2*i + 2 
  
#     # See if left child of root exists and is 
#     # greater than root 
#     if l < n and arr[i] < arr[l]: 
#         largest = l 
  
#     # See if right child of root exists and is 
#     # greater than root 
#     if r < n and arr[largest] < arr[r]: 
#         largest = r 
  
#     # Change root, if needed 
#     if largest != i: 
#         arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
#         # Heapify the root. 
#         heapify(arr, n, largest) 
  
# # The main function to sort an array of given size 
# def heapSort(arr): 
#     n = len(arr) 
  
#     # Build a maxheap. 
#     # Since last parent will be at ((n//2)-1) we can start at that location. 
#     for i in range(n // 2 - 1, -1, -1): 
#         heapify(arr, n, i) 
  
#     # One by one extract elements 
#     for i in range(n-1, 0, -1): 
#         arr[i], arr[0] = arr[0], arr[i]   # swap 
#         heapify(arr, i, 0) 
#     return print(arr)
# print("heapSort:")
# heapSort(arr) 
# print("\n")

# def quickSort(arr): 
#     if len(arr) <= 1:
#         return arr
#     else:
#         return quickSort([x for x in arr[1:] if x < arr[0]]) + \
#                [arr[0]] + \
#                quickSort([x for x in arr[1:] if x >= arr[0]])
# print("quickSort:")
# quickSort(arr)
# print("\n")


# def mergeSort(arr):
#     if len(arr) > 1:
 
#          # Finding the mid of the array
#         mid = len(arr)//2
 
#         # Dividing the array elements
#         L = arr[:mid]
 
#         # into 2 halves
#         R = arr[mid:]
 
#         # Sorting the first half
#         mergeSort(L)
 
#         # Sorting the second half
#         mergeSort(R)
 
#         i = j = k = 0
 
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
 
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
 
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

#     return print(arr)
 
# # Code to print the list
# print("mergeSort:")
# mergeSort(arr)
# print("\n")

# def binarySearch(arr, target):
# 	import math
# 	start = 0
# 	end = len(arr)-1

# 	while (start <= end):
# 		p =math.floor((start+end)/2)

# 		if (arr[p]==target):
# 			return print(p)
# 		else:
# 			if(target<arr[p]):
# 				end=p-1
# 			elif(target>arr[p]):
# 				start=p+1
# 	return -1

# print("binarySearch:")
# binarySearch(arr,1)
# print("\n")

# graph = {
#     "A":["B","C"],
#     "B":["A","C","D"], 
#     "C":["A","B","D","E"],
#     "D":["B","C","E","F"],
#     "E":["C","D"],
#     "F":["D"],      
# }
# def BFS(graph,s):
#     queue = []
#     queue.append(s)
#     seen = set()
#     seen.add(s)
#     while(len(queue)>0):
#         vertex = queue.pop(0)
#         nodes = graph[vertex]
#         for w in nodes:
#             if w not in seen:
#                 queue.append(w)
#                 seen.add(w)
#         print(vertex)
# print("BFS:")
# BFS(graph,'E')
# print("\n")

# graph = {
#     "A":["B","C"],
#     "B":["A","C","D"], 
#     "C":["A","B","D","E"],
#     "D":["B","C","E","F"],
#     "E":["C","D"],
#     "F":["D"],      
# }
# def DFS(graph,s):
#     stack = []
#     stack.append(s)
#     seen = set()
#     seen.add(s)
#     while(len(stack)>0):
#         vertex = stack.pop()
#         nodes = graph[vertex]
#         for w in nodes:
#             if w not in seen:
#                 stack.append(w)
#                 seen.add(w)
#         print(vertex)
# print("DFS:")
# DFS(graph,'E')

# def bubbleSort(arr):
# 	swapped = True
# 	while swapped:
# 		swapped =False
# 		for i in range(len(arr)-1):
# 			if arr[i]>arr[i+1]:
# 				swapped =True
# 				tmp = arr[i+1]
# 				arr[i+1] = arr[i]
# 				arr[i] =tmp
# 	return print(arr)

# bubbleSort(arr)