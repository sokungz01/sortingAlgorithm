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
	int s  = l;
	int i = 0;
	int pivot = arr[l];
	for(i = l+1; i <= r;i++){
		if(arr[i] < pivot){
			s++;
			swap(&arr[i],&arr[s]);
		}
	}
	
	swap(&arr[l],&arr[s]);
	return s;
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

    time_t start = clock();
    QuickSort(arr,0,size-1);
    time_t end = clock();
    printArr(arr,size);
    printf("%.10f",(double)(end-start)/CLOCKS_PER_SEC);

    return 0;
}
