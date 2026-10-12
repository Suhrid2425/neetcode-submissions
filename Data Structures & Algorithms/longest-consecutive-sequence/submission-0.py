class Solution:
    def longestConsecutive(self, nums):

        nums_set = set(nums)
        longest = 0

        for num in nums_set:

            # Check if num is the START of a sequence
            if num - 1 not in nums_set:

                length = 1

                # Check next numbers
                while num + length in nums_set:
                    length += 1

                longest = max(longest, length)

        return longest