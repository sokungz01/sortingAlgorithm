#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void printArr(int *arr , int size){
    for(int i = 0 ; i < size ; i++)
        printf("%d ",arr[i]);
}

void swap(int *a ,int *b)
{
    int temp = *a ;
    *a = *b;
    *b = temp;
}

int Partition(int *arr,int l,int r){
    int pivot = arr[l];
    int i = l;
    int j = r+1;

    do{
        do
            i++;
        while(arr[i] < pivot);

        do
            j--;
        while(arr[j] > pivot);

        swap(&arr[i],&arr[j]);

    }while(i<j);
    swap(&arr[i],&arr[j]);
    swap(&arr[l],&arr[j]);
    return j;
}

void QuickSort(int *arr, int l ,int r){
    if(l<r){
        int s = Partition(arr,l,r);
        QuickSort(arr,l,s-1);
        QuickSort(arr,s+1,r);
    }
}

int main(){
    int size;
    scanf("%d",&size);
    int *arr = (int *)malloc(size*sizeof(int));
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    QuickSort(arr,0,size-1);
    // printArr(arr,size);
    return 0;
}
