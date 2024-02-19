package bubble_sort;

public class bubble_sort {
    public static void main(String[] args) {
        int[] l = {3, 22, 213, 5, 3, 1, 2, 1, 2, 1, 2, 14, 12};
        for (int i = l.length - 1; i > 0 ; i--)
            for (int j = 0; j < i; j++)
                if (l[i] < l[j]) {
                    int temp = l[j];
                    l[j] = l[i];
                    l[i] = temp;
                }

        for (int i = 0; i < l.length; i++) {
            System.out.printf("%s ", l[i]);
        }
        System.out.println();
    }
}