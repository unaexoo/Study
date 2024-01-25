using System;

public class Solution
{
    public int solution(int n, int t)
    {
        int answer = n;
        for (int i = 1; i <=t; i++)
        {
            answer *= 2;
        }
        return answer;
    }
    static void Main(string[] args)
    {
        int num = 2;
        int t = 10;
        Solution sol = new Solution();
        Console.WriteLine(sol.solution(num, t));
    }
}