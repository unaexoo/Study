#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include<math.h>
int solution(int n) {
    int answer = 0;
    int num = 0;
    while (n != 0) {
        num=n % 3;
        n /= 3;
        answer*=3;
        answer +=num;
    }
    return answer;
}
