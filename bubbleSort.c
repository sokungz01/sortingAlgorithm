#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void printArr(int *arr,int size){
    for(int i = 0 ; i < size ; i ++)
        printf("%d ",arr[i]);
}   

void swap(int *a ,int *b){
    int temp = *a ;
    *a = *b;
    *b = temp;
}


int main(){

    int size;
    scanf("%d",&size);
    int *arr = (int *)malloc(size*sizeof(int));
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    time_t start = clock();
    for(int i = 0 ; i < size -1 ; i ++){
        for(int j = 0; j < size - i -1 ; j++){
            if(arr[j+1] < arr[j]){
                swap(&arr[j+1],&arr[j]);
            }
        }
    }
    time_t end = clock();
    printf("%.10f",(double)(end-start)/CLOCKS_PER_SEC);

    return 0 ;
    
}
