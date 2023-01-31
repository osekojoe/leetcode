class Solution:
	def mySqrt(self, x: int) -> int:
		left = 0
		right = 10000000
		mid = (left + right) // 2