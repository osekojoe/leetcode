#!usr/bin/env python3
class Solution(object):
	"""return indices of the two numbers such that they 
	add up to target
	eg: 
	Input: nums = [2,7,11,15], target = 9
	Output: [0,1]
	Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
	"""
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in range(len(nums)):
			for j in range((i + 1), len(nums)):
				if nums[j] == target - nums[i]:
					return [i, j]

	def hash_twoSum(self, nums, target):
		"""more efficient solution with hash table"""
		hashmap = {}
		for i in range(len(nums)):
			hashmap[nums[i]] = i
		for i in range(len(nums)):
			j = target - nums[i]
			if (j in hashmap) and hashmap[j] != i:
				return [i, hashmap[j]]

nums = [2,7,11,15]
target = 9

sol = Solution.twoSum(object, nums, target)
print(sol)