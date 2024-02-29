package merge_sort;

public class merge_sort {
    public static void main(String[] args) {
        int[] arr = {2, 4, 2, 5, 3, 5, 2, 5, 7, 8, 2, 4, 66, 1};
        int[] result = algo(arr);
        for (int i : result) {
            System.out.printf("%s ", i);
        }
    }

    static int[] algo(int[] arr) {
        if (arr.length <= 1) return arr;
        int[] left_arr = slice(arr, 0, arr.length / 2);
        int[] right_arr = slice(arr, arr.length / 2, arr.length);
        left_arr = algo(left_arr);
        right_arr = algo(right_arr);
        int i = 0;
        int j = 0;
        int k = 0;
        int[] result = new int[left_arr.length + right_arr.length];
        while (i < left_arr.length && j < right_arr.length) {
            if (left_arr[i] > right_arr[j]) {
                result[k] = right_arr[j];
                j++;
            } else {
                result[k] = left_arr[i];
                i++;
            }
            k++;
        }

        while (i < left_arr.length) {
            result[k] = left_arr[i];
            i++;
            k++;
        }
        while (j < right_arr.length) {
            result[k] = right_arr[j];
            j++;
            k++;
        }
        return result;
    }

    static int[] slice(int[] arr, int start, int end) {
        int[] arr2 = new int[end - start];
        int j = 0;
        for (int i = start; i < end; i++) {
            arr2[j] = arr[i];
            j += 1;
        } 
        return arr2;
    }
}
