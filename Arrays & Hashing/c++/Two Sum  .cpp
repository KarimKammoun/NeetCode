class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            int n = target - nums[i];
            auto it = find(nums.begin() + i + 1, nums.end(), n);
            if (it != nums.end()) {
                return {i, static_cast<int>(distance(nums.begin(), it))};
            }
        }
        return {};
    }
};
