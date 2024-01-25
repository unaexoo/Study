using System;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
       int[] answer = new int[commands.GetLength(0)];
            int first, last, size;
            int[] tmp;
            for(int i=0; i<commands.GetLength(0); i++)
            {
                first = commands[i, 0]-1;
                last = commands[i, 1]-1;
                size = commands[i, 2]-1;

                tmp = new int[last - first + 1];
                Array.Copy(array, first, tmp, 0, tmp.Length);
                Array.Sort(tmp);

                answer[i]=tmp[size];
            }
            return answer;
    }
}
