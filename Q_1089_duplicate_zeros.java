package leetcode;
import java.util.*;

public class Q_1089_duplicate_zeros {
    public void duplicateZeros(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int i : arr) {
            if (i == 0) {
                list.add(0);
                list.add(0);
            } else list.add(i);
        }

        for (int i = 0; i < arr.length; i++)
            arr[i] = list.get(i);
    }
}
