using System;
using System.Linq;
public class Solution {
    public string solution(string s) {
        string answer = "";
            int[] numArray = s.Split(' ').Select(int.Parse).ToArray();
            int min = numArray.Min();
            int max = numArray.Max();
            answer = min + " " + max;
            return answer;
    }
}
