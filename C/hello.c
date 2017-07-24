#include <stdio.h>
#include <string.h>
#include <pthread.h>


void *thread_fun(void *param)
{
    int *a = (int *)param;
    int i=0;
    while(1)
    {
        for(i=0;i<10;i++)
            {
                printf("%d ", a[i]++);
            }
    }
}

void main()
{
    pthread_t tid;
    int a[10]={1,2,3,4,5,6,7,8,9,0};
    thread_fun((void *)a);
    //pthread_create(&tid,NULL,thread_fun,(void *)a);
}
