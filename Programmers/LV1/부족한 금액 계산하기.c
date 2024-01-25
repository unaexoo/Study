#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int price, int money, int count) {
    long long answer = 0;
    int sum = 0;
 
    for (int i = 1; i < count+1; i++) {
        sum = price * i;
        answer += sum;
     
    }
   
    if (answer> money)
    {
        answer-=money;
    }
    else
    {
        answer = 0;
    }
    return answer;
}
