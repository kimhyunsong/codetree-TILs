#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
int main() {
    // 여기에 코드를 작성해주세요.

    int N, B;
    scanf("%d %d", &N, &B);

    int *p_arr = (int*)malloc(sizeof(int)* N);
    int *s_arr = (int*)malloc(sizeof(int)* N);

    for (int i = 0; i < N; i++)
    {
        int p, s;
        scanf("%d %d", &p, &s);
        p_arr[i] = p;
        s_arr[i] = s;
    }

    int max_student = INT_MIN;

    for (int i = 0; i < N; i++)
    {
        int price_sum = 0;
        int student_count = 0;
        for (int j = 0; j < N; j++)
        {
            if (price_sum > B)
            {
                student_count = j;
                if (j > max_student){
                    max_student = j;
                    break;
                }
            }
            else if (price_sum == B)
            {
                if ((j + 1) > max_student)
                {
                    max_student = j + 1;
                    break;
                }
            }


            price_sum += s_arr[j];
            if (i == j)
            {
                price_sum += p_arr[j] / 2;
            }
            else price_sum += p_arr[i];

        }

    }
    printf("%d", max_student);

    return 0;
}