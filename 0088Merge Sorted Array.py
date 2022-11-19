def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = nums2[:] + nums1[:m]
        nums1.sort()