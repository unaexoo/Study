using System;
using System.Linq;
public class Solution
{
    public static int[] solution(int[] array)
    {
        int[] answer = new int[2];
        for (int i = 0; i < array.Length; i++)
        {
            for (int j = 0; j < array.Length; j++)
            {
                if (array[i] < array[j])
                {
                    answer[0] = array[j];
                    answer[1] = j;
                }
            }
        }
        return answer;
    }
    public int [] sol(int[] array)
    {
        int[] answer = new int[2] { array.Max(), Array.IndexOf(array, array.Max()) };
        return answer;
    }
    static void Main(string[] args)
    {
        int[] arr = { 1, 8, 3 };
        solution(arr);
    }
}