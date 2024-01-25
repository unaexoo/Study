using System;
public class Solution {
    public int[] solution(int n, int m) {
       int[] answer = new int[2];
        int max = Math.Max(n, m);
        int min = Math.Min(n, m);

        int rem = 0;
        while (min != 0)
        {
            rem = max % min;
            max = min;
            min = rem;
        }

        answer[0] = max;
        answer[1] = n * m / max;
        return answer;
    }
}
