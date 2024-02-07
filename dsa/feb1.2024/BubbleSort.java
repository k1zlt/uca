import java.util.Arrays;

class BubbleSort {
    public static void main(String[] args) {
        int[] nums = {5, 3, 8, 6, 7, 2};
        for (int i = nums.length - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                if (nums[j] > nums[j+1]) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(nums));
    }
}