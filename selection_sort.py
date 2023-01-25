#!usr/bin/env python3
class Solution(object):
	def selection_sort(self, arr):
		for i in range(len(arr)):
			min_idx = i #initialize minimum element
			for j in range(i + 1, len(arr)):
				if arr[min_idx] > arr[j]:
					min_idx = j
			arr[i], arr[min_idx] = arr[min_idx], arr[i]

	def printArr(self, arr):
		for i in range(len(arr)):
			print("%d" %arr[i], end=" ")

if __name__ == "__main__":
	arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
	Solution.selection_sort(object, arr)
	Solution.printArr(object, arr)