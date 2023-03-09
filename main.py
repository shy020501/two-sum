

def twoSum(self, nums: list[int], target: int) -> list[int]:
    answer = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                answer.append(i)
                answer.append(j)
                break
    return answer