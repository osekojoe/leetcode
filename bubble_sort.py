#!usr/bin/env python3
class Solution(object):
	def bubbleSort(self, arr):
		"""sort array with bubble sort algorithm"""
		for i in range(len(arr)):
			for j in range(0, len(arr) - i - 1):
				if arr[j] > arr[j + 1]:
					arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
	arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]

	Solution.bubbleSort(object, arr)

	for i in range(len(arr)):
		print('{}'.format(arr[i]), end= " ")
		