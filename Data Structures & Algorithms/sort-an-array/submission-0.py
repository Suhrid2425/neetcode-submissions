class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            i = 0
            j = 0
            arr = []

            while i < len(left) and j < len(right):

                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1

            while i < len(left):
                arr.append(left[i])
                i += 1

            while j < len(right):
                arr.append(right[j])
                j += 1

            return arr

        return merge_sort(nums)