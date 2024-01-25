#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;
    int small;
    int big;

    if (a>b)
    {
        small = b;
        big = a;
    }
    else
    {
        small = a;
        big = b;
    }
  
    for (int i = small; i < big + 1; i++) {
        answer += i;
    }
    return answer;
}
