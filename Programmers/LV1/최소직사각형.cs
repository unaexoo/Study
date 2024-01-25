using System;

public class Solution {
    public int solution(int[,] sizes) {
      int answer = 0;
        int tmp = 0;
        for(int i=0; i<sizes.GetLength(0); i++)
        {
            if (sizes[i, 1] > sizes[i, 0])
            {
                tmp = sizes[i, 1];
                sizes[i, 1] = sizes[i, 0];
                sizes[i, 0] = tmp;
;            }
        }

        int max = 0;
        for(int i=0; i < sizes.GetLength(0); i++)
        {

            if (sizes[i, 0] > answer)
            {
                answer = sizes[i, 0];
            }

            if (sizes[i, 1]>max)
            {
                max = sizes[i, 1];
            }
   
        }

        answer *= max;
        return answer;
    }
}
