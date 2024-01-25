#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int sum = 0;
    int count = 0;
    for (int i = 0; i < nums_len; i++) {
        for (int j = i+1; j < nums_len ; j++) {
            for (int k = j + 1; k < nums_len; k++) {
                count = 0;
                sum = nums[i] + nums[j] + nums[k];
                for (int x = 1; x <= sum; x++) {
                    if (sum % x == 0) {
                        count++;
                    }
                }
                if (count == 2) {
                    answer++;
                }
                sum = 0;
            }
        }
    }
    return answer;
}
