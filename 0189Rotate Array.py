def rotate(self, nums: list[int], k: int) -> None:
        if k >= len(nums):
            k = k % len(nums)
        ans = nums[-k:]
        nums[:] = ans[:] + nums[:-k]
        return None