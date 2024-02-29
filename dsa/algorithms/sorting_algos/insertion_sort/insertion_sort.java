package insertion_sort;

public class insertion_sort {
    public static void main(String[] args) {
        int[] list = {3, 2, 3, 1, 2, 4, 3, 4, 3, 2};
        algo(list);
        
    }

    static void algo(int[] list) {
        for (int i = 1; i < list.length; i++) {
            int j = i;
            while (j > 0 && list[j - 1] > list[j]) {
                int temp = list[j];
                list[j] = list[j-1];
                list[j-1] = temp;
                j--;
            }
        }
        for (int i = 0; i < list.length; i++) {
            System.out.printf("%s ", list[i]);
        }
        System.out.println();
    }
}