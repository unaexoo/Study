using System;

public class Solution {
    public bool solution(string s) {
        bool answer = true;
        int cnt1 = 0, cnt2 = 0;
        foreach(char ch in s)
        {
            if (ch == '(')
            {
                cnt1++;
            }
            else
            {
                cnt2++;
            }

            if (cnt2 > cnt1)
            {
                return answer = false;
            }
        }
        if (cnt1 != cnt2)
        {
            return answer = false;
        }
        return answer;
    }
}
