using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr) {
         int[] answer;
            if (arr.Length == 1)
            {
                answer = new int[1];
                answer[0] = -1;
                return answer;
            }
            answer = new int[arr.Length - 1];
            
            List<int> list = new List<int>(arr);
            list.Remove(arr.Min());
            
            for (int i = 0; i < answer.Length; i++)
            {
                answer[i] = list[i];
            }

            return answer;
    }
}
