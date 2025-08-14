var largestNumber = function(nums) {
    nums.sort((a, b) => {
        let ab = '' + a + b;
        let ba = '' + b + a;
        return ba.localeCompare(ab); // bigger combination first
    });

    // Handle case like [0,0] → "0"
    if (nums[0] === 0) return "0";

    return nums.join('');
};
