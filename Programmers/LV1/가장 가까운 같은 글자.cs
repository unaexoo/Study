using System;

public class Solution {
    public int[] solution(string s) {
       int[] answer = new int[s.Length];
        char[] strArr = s.ToCharArray();
        int idx = -1;
        for (int i = 0; i < strArr.Length; i++)
        {
            idx = -1;
            for (int j = i-1; j >=0; j--)
            {
                if (strArr[i] == strArr[j])
                {
                    idx = i - j;
                    break;
                }
            }
            answer[i] = idx;
        }
        return answer;
    }
}
