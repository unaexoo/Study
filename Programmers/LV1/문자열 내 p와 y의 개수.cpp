#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = false;
    int cnt1 = 0, cnt2=0;
   
    int i = 0;
    while (s[i] != NULL) {
        if (s[i] == 'p' || s[i]=='P') {
            cnt1++;
        }
        if(s[i]=='y' || s[i]=='Y')
        {
            cnt2++;
        }

        i++;
    }
    
    
    if (cnt1 == 0 && cnt2==0) {
        answer = true;
    }
    else if (cnt1 == cnt2) {
        answer = true;
    }
    else{
        answer = false;
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer;
}
