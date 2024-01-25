#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include<string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
  
    char* answer = (char*)malloc(1*strlen(s)+1);

    int cnt = 0;
    strcpy(answer, s);
    for (int i = 0; i < strlen(s); i++) {
        cnt++;
        if (cnt % 2 == 1 && ('a' <= s[i] && 'z' >= s[i])) {
            answer[i] -= 32;
        }
        else if(cnt%2==0 && ('A' <= s[i] && 'Z' >= s[i])) {
            answer[i] += 32;
        }
        else if (s[i] == ' ') {
            cnt = 0;
        }
    }


    /*for (int i = 0; i < cnt; i++) {
        if ('a' <= s[i] && 'z' >= s[i]) {
            if (cnt % 2 == 1) {
                answer[i] -= 32;
            }
        }
        if ('A' <= s[i] && 'Z' >= s[i]) {
            if (cnt % 2 == 1) {
                answer[i] += 32;
            }
        }
    }*/
    return answer;
}
