using System;

public class Solution
{
    public static int solution(string[] s1, string[] s2)
    {
        int answer = 0;
        for (int i = 0; i < s1.Length; i++)
        {
            for (int j = 0; j < s2.Length; j++)
            {
                if (s1[i] == s2[j]) 
                {
                    answer++;
                }
            }
        }
        Console.WriteLine(answer);
        return answer;
    }
    static void Main(string[] args)
    {
        string[] str1 = { "a", "b", "c" };
        string[] str2 = { "com", "b", "d", "p", "C" };
        solution(str1, str2);
    }
}