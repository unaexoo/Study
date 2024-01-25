using System;

public class Solution
{
    public int[] solution(int numer1, int denom1, int numer2, int denom2)
    {
        int[] answer = new int[] { };
        int numer = (numer1 * denom2) + (numer2 * denom1);
        int denom = numer1 * numer2;
 
        return answer;
    }
}