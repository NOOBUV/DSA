class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        for i in nums:
            self.prefix.append(self.prefix[-1] + i)
        self.n = len(self.prefix)

    def update(self, index: int, val: int) -> None:

        diff = val - self.nums[index]
        self.nums[index] = val
        for i in range(index+1, self.n):
            self.prefix[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
