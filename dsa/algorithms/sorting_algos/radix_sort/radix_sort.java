package radix_sort;

import java.util.Arrays;

public class radix_sort {
    public static void main(String[] args) {
        int[] arr = new int[]{423, 215, 123, 52, 234, 1, 31, 432, 11, 63, 743};
        algo(arr);
        for(int i: arr) {
            System.out.printf("%s ", i);
        }
        System.out.println();
    }

    public static int[] algo(int[] arr) {
        int max = Arrays.stream(arr).max().orElse(Integer.MAX_VALUE);
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countring_sort(arr, exp);
        }
        return arr;
    }

    public static void countring_sort(int[] arr, int exp) {
        int[] countArray = new int[10];
        for (int value: arr) {
            countArray[(value / exp) % 10]++;
        }

        for (int i = 1; i < 10; i++) {
            countArray[i] += countArray[i - 1];
        }

        int[] output = new int[arr.length];
        for (int i = arr.length - 1; i >= 0; i--) {
            int current = arr[i];
            int positionInArray = countArray[(current / exp) % 10] - 1;
            output[positionInArray] = current;
            countArray[(current / exp) % 10]--;
        }

        System.arraycopy(output, 0, arr, 0, arr.length);
    }
}
