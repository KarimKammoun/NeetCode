nums=[3, 4, 5, 6, 1, 2]
target=1
p=0
q=len(nums)-1

while p <= q:
    k = (p + q)//2

    if nums[k] == target:
        print(k)
        break

    if nums[p] <= nums[k]: 
        if nums[p] <= target < nums[k]: 
            q = k - 1
        else: 
            p = k + 1
    else: 
        if nums[k] < target <= nums[q]:  
            p = k + 1
        else:  
            q = k - 1
else:
    print(-1)

