using System;

namespace 문자열곱하기
{

    public class Solution
    {
        public string solution(string my_string, int k)
        {
            string answer = "";
            for(int i=0;i<k; i++)
            {
                answer += my_string;
            }
            return answer;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Solution sol = new Solution();

            Console.WriteLine(sol.solution("string",3));
        }
    }
}
