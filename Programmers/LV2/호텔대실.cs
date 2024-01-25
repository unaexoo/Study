using System;
using System.Collections.Generic;

public class Solution
{
    public static int solution(string[,] book_time)
    {
        int answer = 0;
        List<string> time = new List<string>();
        
        for (int i = 0; i < book_time.GetLength(0); i++)
        {
            time.Add(book_time[i, 1]);    
        }

        string[] str = new string[time.Count];

        for (int i = 0; i < time.Count; i++)
        {
            str[i] = time[i];
        }

        string[] strleaveHour = new string[str.Length];
        string[] strleaveMinite = new string[str.Length];

        for (int i = 0; i < str.Length; i++)
        {
            strleaveHour[i] = str[i].Substring(0,2);
            strleaveMinite[i] = str[i].Substring(3);
            Console.WriteLine("first : {0}", strleaveMinite[i]);
        }

        int[] intleaveHour = new int[strleaveMinite.Length];
        int[] intlaeaveMinite = new int[strleaveMinite.Length];

        for (int i = 0; i < str.Length; i++)
        {
            intleaveHour[i] = int.Parse(strleaveHour[i]);
            intlaeaveMinite[i] = int.Parse(strleaveMinite[i]);
        }

        int minite = 0;

        for (int i = 0; i < str.Length; i++)
        {
            intlaeaveMinite[i] += 10;
            if (intlaeaveMinite[i] > 59)
            {
                intleaveHour[i] += 1;
                minite = intlaeaveMinite[i] % 60;
                intlaeaveMinite[i] = minite;
            }
        }

        return answer;
    }
    static void Main(string[] args)
    {
        string[,] time1 = { 
            { "09:10", "10:10" }, 
            { "10:20", "12:20" } };
       // string[,] time2 = { { "10:20", "12:30" }, { "10:20", "12:30" }, { "10:20", "12:30" } };
        solution(time1);
        //solution(time2);
    }
}
