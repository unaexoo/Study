using System;
using System.Linq;

public class Solution {
    public string[] solution(string[] strings, int n) {
        string[] answer = new string[strings.Length];
        answer = strings.OrderBy(a=>a).OrderBy(a => a[n]).ToArray();
        return answer;
    }
}
