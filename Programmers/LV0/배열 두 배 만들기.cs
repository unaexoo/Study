using System;
using System.Linq;
public class Solution
{
    public static int[] solution(int[] numbers)
    {
        int[] answer = new int[numbers.Length];

        for (int i = 0; i < numbers.Length; i++)
        {
            answer[i] = numbers[i] * 2;
        }
        return answer;
    }
    public static int[] sol(int[] numbers) 
    {

        int[] answer = numbers.Select(x => x * 2).ToArray();
        return answer;
    }

    static void Main(string[] args)
    {
        int[] num = { 1, 2, 3, 4, 5 };
        solution(num);
    }
}
