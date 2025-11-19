nums =[2,7,11,15]
target=13
def twoSum(nums, target):
        i=0
        for i in range(len(nums)):
            if nums[i]+nums[i+1] == target:
                return i,i+1
print (twoSum(nums,target))
