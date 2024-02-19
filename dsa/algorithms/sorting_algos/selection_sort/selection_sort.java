package selection_sort;

public class selection_sort {
    public static void main(String[] args) {
        int[] l = {23, 123, 3123, 1, 123, 1, 3, 2, 5, 2, 5, 2, 6, 7};
        for (int i = 0; i < l.length; i++) {
            int temp = i;
            for (int j = i; j < l.length; j++) {
                if (l[temp] > l[j]) {
                    temp = j;
                }
            }
            int temp2 = l[i];
            l[i] = l[temp];
            l[temp] = temp2;
        }
        for (int i = 0; i < l.length; i++) {
            System.out.printf("%s ", l[i]);
        }
        System.out.println();
    }
}
