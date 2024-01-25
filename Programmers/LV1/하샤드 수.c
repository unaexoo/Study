#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = 0;
    int sum = 0;
    int num1 ,num2, num3,num4;

    int ten=1;
    while (x / ten != 0) {
        ten *= 10;
    }
    ten/=10;

    for (int i = 0; i < 10; i++) {
        num1 = x / ten;
        num2 = (x - num1 * ten) / 100;
        num3 = (x - num1 * ten - num2 * 100) / 10;
        num4 = (x - num1 * ten - num2 * 100 - num3 * 10) / 1;
        sum = num1 + num2 + num3 + num4;
        break;
    }

    if (x%sum== 0) {
        answer = true;
    }
    else
    {
        answer = false;
    }
    return answer;
}
