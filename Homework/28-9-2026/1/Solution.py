class Solution:
	def removeDuplicates(self, s):
		# code here
		final = []

		for i in s:
			if i not in final:
				final.append(i)

		return "".join(final)
