public class Solution {
    public int[] solution(int[] arr, int divisor) {
       int[] answer;
            int tmp = 0;
            int cnt = 0;

            for(int i=0; i<arr.Length; i++)
            {
                if (arr[i] % divisor == 0)
                {
                    cnt++;
                }
            }
           
            if (cnt == 0)
            {
                answer = new int[1];
                answer[0] = -1;
                return answer;
            }

            answer = new int[cnt];


            for (int i = 0; i < answer.Length; i++)
            {
                for (int j = 0; j < arr.Length; j++)
                {
                    if (arr[j] % divisor == 0)
                    {
                        answer[i]= arr[j];
                        i++;
                    }
                }
            }

            for (int i = 0; i < answer.Length; i++)
            {
                for (int j = 0; j < answer.Length; j++)
                {
                    if (answer[j] > answer[i])
                    {
                        tmp = answer[j];
                        answer[j] = answer[i];
                        answer[i] = tmp;
                    }
                }
            }

                return answer;
    }
}
