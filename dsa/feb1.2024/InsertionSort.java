import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {
        int[] nums = {5, 4, 3, 4, 3, 2, 4, 1, 2, 3, 4, 3, 100};
        for (int i = 1; i < nums.length; i++) {
            int j = i;
            while (j > 0 && nums[j - 1] > nums[j]) {
                int temp = nums[j];
                nums[j] = nums[j - 1];
                nums[j - 1] = temp;
                j -= 1;
            }
        }
        System.out.println(Arrays.toString(nums));
    }
}
