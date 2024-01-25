using System;

public class Solution
{
    public static int[] solution(int[] num_list)
    {
        int[] answer=new int[num_list.Length];
        Array.Reverse(num_list);
        answer = num_list;
        return answer;
    }

    static void Main(string[] args)
    {
        int[] num = { 1, 2, 3, 4, 5 };
        
        Console.WriteLine(solution(num));
    }
}