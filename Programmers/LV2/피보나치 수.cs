public class Solution {
    public int solution(int n) {
       int answer = 0;
            int num1=0;
            int num2 = 1;

            for(int i = 2; i <= n; i++)
            {
                answer = (num1 + num2) % 1234567;
                num1 = num2;
                num2 = answer;
            }
            return answer;
    }
}
