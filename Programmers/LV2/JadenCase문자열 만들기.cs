using System;
using System.Text;
public class Solution {
    public string solution(string s) {
               string answer = "";
        s = s.ToLower();
        char[] ch = s.ToCharArray();

        for(int i=0; i<ch.Length; i++)
        {
            ch[0] = Char.ToUpper(ch[0]);
            if(ch[i] == ' '&& i+1 <ch.Length)
            {
                ch[i + 1] = char.ToUpper(ch[i + 1]);
            }

            answer+=ch[i].ToString();
        }
        return answer;
    }
}
