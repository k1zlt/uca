package quick_sort;

import java.util.ArrayList;
import java.util.List;

public class quick_sort {
    public static void main(String[] args) {
        int[] arr = {3, 5, 2, 52, 4, 1, 5, 13, 51, 13, 1};
        for (int i: algo(arr)) {
            System.out.printf("%s ", i);
        }
        System.out.println();
    }

    public static int[] algo(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }
        int pivot = arr[0];
        int[][] split_result = split(split(arr, 1, arr.length), pivot);
        int[] left = algo(split_result[0]);
        int[] right = algo(split_result[1]);
        return concat(left, concat(new int[] {pivot}, right));
    }

    public static int[][] split(int[] arr, int pivot) {
        List<Integer> lower = new ArrayList<>();
        List<Integer> upper = new ArrayList<>();
        for (int i: arr) {
            if (i < pivot) {
                lower.add(i);
            } else {
                upper.add(i);
            }
        }
        int[] lowerArray = lower.stream().mapToInt(i -> i).toArray();
        int[] upperArray = upper.stream().mapToInt(i -> i).toArray();
        return new int[][] {lowerArray, upperArray};
    }

    public static int[] split(int[] arr, int start, int end) {
        int[] arr2 = new int[end - start];
        for (int i = start; i < end; i++) {
            arr2[i-start] = arr[i];
        }
        return arr2;
    }

    public static int[] concat(int[] a, int[] b) {
        int[] c = new int[a.length + b.length];
        for (int i = 0; i < c.length; i++) {
            if (i < a.length) {
                c[i] = a[i];
            } else {
                c[i] = b[i - a.length];
            }
        }
        return c;
    }
}
