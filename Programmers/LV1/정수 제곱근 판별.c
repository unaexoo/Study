#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include<math.h>
long long solution(long long n) {
    long long answer = 0;
    for (int i = 1; i <=n; i++) {
        if (pow(i,2) == n) {
            answer = pow((i+1),2);
            break;
        }
        else
        {
            answer = -1;
        }
    }
    return answer;
}
