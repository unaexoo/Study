using System;

public class Solution
{
    public static int[] solution(int numer1, int denom1, int numer2, int denom2)
    {
        int[] answer = new int[2];
        int tmp = 0;
        if (denom1 % denom2 == 0 || denom2 % denom1 == 0)
        {
            tmp = denom1 % denom2 == 0 ? denom1 : denom2;
            numer1 *= tmp / denom1;
            numer2 *= tmp / denom2;

        }
        else
        {
            tmp = denom1 * denom2;
            numer1 *= denom2;
            numer2 *= denom1;
            denom1 = tmp;
            denom2 = tmp;
        }

        answer[0] = numer1 + numer2;
        answer[1] = tmp;

        return answer;
    }
    static void Main(string[] args)
    {
        int num1 = 1, de1 = 2, num2 = 3, de2 = 4;
        solution(num1, de1, num2, de2);
    }
}
