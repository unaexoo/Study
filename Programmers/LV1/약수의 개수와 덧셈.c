#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int left, int right) {
    int answer = 0;
    int count = 0;
 
    for (int i=left; i < right+1; i++) {
        count = 0;
        for (int j = 1; j < right+1; j++) {
            if (i % j == 0)
            {
                count++;
            }
        }
        if (count % 2 != 0)
        {
            answer -= i;
        }
        if (count % 2 == 0)
        {
            answer += i;
        }
    }
    return answer;
}
