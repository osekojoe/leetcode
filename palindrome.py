class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		tmp = x
		rev = 0
		while (tmp > 0):
			last_digit = tmp % 10
			rev = (rev * 10) + last_digit
			tmp = tmp // 10 #flatten or round off
		if x == rev:
			return True
		else:
			return False

	def isPalindromeString(self, x):
		x_str_rev = str(x)[::-1]
		reverse = int(x_str_rev)

		if x == reverse:
			return True
		else:
			return False

x = 1221
#sol = Solution.isPalindrome(object, x)
sol = Solution.isPalindromeString(object, x)
print(sol)