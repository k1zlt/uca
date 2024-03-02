package countring_sort;

import java.util.Arrays;

public class countring_sort {
    public static void main(String[] args) {
        int[] arr = new int[]{423, 432, 432, 423, 215, 123, 52, 234, 1, 31, 432, 11, 63, 743};
        sort(arr);
        for(int i: arr) {
            System.out.printf("%s ", i);
        }
        System.out.println();
    }

    public static int[] sort(int[] arr) {
        int max = Arrays.stream(arr).max().orElse(Integer.MAX_VALUE);
        int min = Arrays.stream(arr).min().orElse(0);

        int[] countArray = new int[max - min + 1];
        for (int value: arr) {
            countArray[value - min]++;
        }
        int k = 0;
        for (int i = 0; i < max - min + 1; i++) {
            while (countArray[i] > 0) {
                countArray[i]--;
                arr[k] = i + min;
                k++;
            }
        }
        return arr;
    }
}
