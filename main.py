

def twoSum(self, nums: list[int], target: int) -> list[int]:
    answer: list = []
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                answer.append(i)
                answer.append(j)
                break
    return answer