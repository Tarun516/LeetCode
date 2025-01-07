class Solution {
public:
    // Function to find the first occurrence of the key
    int firstOcc(vector<int>& nums, int key) {
        int n = nums.size();
        int start = 0, end = n - 1;
        int ans = -1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] == key) {
                ans = mid;       // Update answer
                end = mid - 1;   // Move left to find earlier occurrence
            } else if (nums[mid] < key) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return ans; // Return the first occurrence
    }

    // Function to find the last occurrence of the key
    int secondOcc(vector<int>& nums, int key) {
        int n = nums.size();
        int start = 0, end = n - 1;
        int ans = -1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] == key) {
                ans = mid;       // Update answer
                start = mid + 1; // Move right to find later occurrence
            } else if (nums[mid] < key) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return ans; // Return the last occurrence
    }

    vector<int> searchRange(vector<int>& nums, int key) {
        // Get the first and last occurrence of the key
        int first = firstOcc(nums, key);
        int last = secondOcc(nums, key);

        // Return as a vector
        return {first, last};
    }
};
