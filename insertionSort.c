#include<stdio.h>
#include<stdlib.h>

void printArr(int *arr,int size){
    for(int i = 0 ; i < size ; i ++)
        printf("%d ",arr[i]);
}   

int main(){
    int size;
    scanf("%d",&size);
    int *arr = (int *)malloc(size*sizeof(int));
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    for(int i = 1 ; i < size ; i++){
        int v = arr[i];
        int j = i-1;

        while(j >= 0 && arr[j] > v){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = v;
    }
    return 0 ;
    
}