using System;

public class Solution {
    public int[] solution(int brown, int yellow) {
     int[] answer = new int[2];
        int sum = brown + yellow;
        int tmp = 0;
        for (int i = 1; i <=sum; i++)
        {
            tmp = sum / i;
            if ((i - 2) * (tmp - 2) == yellow)
            {
                answer[0] = tmp;
                answer[1] = i;
                break;
            }
        }
        return answer;
    }
}
