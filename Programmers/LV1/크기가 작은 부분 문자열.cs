using System;

public class Solution {
    public int solution(string t, string p) {
       int answer = 0;
        int len = t.Length - p.Length + 1;
        for (int i = 0; i < len; i++)
        {
            string substring = t.Substring(i, p.Length);

            if (substring.CompareTo(p) <= 0)
            {
                answer++;
            }
        }
        return answer;
    }
}
