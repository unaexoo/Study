using System;

public class Solution {
public int[] solution(string s)
        {
            int[] answer = new int[2];
            int cnt = 0; 
            int zero = 0;

            while (s != "1")
            {
                int sub_cnt = 0;
                for (int i = 0; i < s.Length; i++)
                {
                    if (s[i] == '1') sub_cnt++;
                    else zero++;
                }
                
                s = Convert.ToString(sub_cnt, 2);
                cnt++;
            }
            
            answer[0] = cnt;
            answer[1] = zero;

            return answer;
        }
}
