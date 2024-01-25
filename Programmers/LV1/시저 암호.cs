public class Solution {
    public string solution(string s, int n) {
        string answer = "";
            char[] ch = s.ToCharArray();
            for (int i = 0; i < ch.Length; i++)
            {
                if (ch[i] >= 'a' && ch[i] <= 'z')
                {
                    ch[i] = (char)((ch[i] - 'a' + n) % 26 + 'a');
                }
                else if (ch[i] >= 'A' && ch[i] <= 'Z')
                {
                    ch[i] = (char)((ch[i] - 'A' + n) % 26 + 'A');
                }
                answer += ch[i].ToString();
            }
            return answer;
    }
}
