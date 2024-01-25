using System;
public class Solution {
    public long solution(long n) {
        long answer = 0;
        char []num = n.ToString().ToCharArray();
        Array.Sort(num);
        Array.Reverse(num);
        answer = long.Parse(num);
        return answer;
    }
}
