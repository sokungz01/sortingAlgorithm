#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void printArr(int *arr, int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void Merge(int *arr, int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;
    int i = 0, j = 0, k = 0;
    int *b = calloc(r - l + 1, sizeof(int));
    while (i < n1 && j < n2)
    {
        if (arr[l + i] < arr[m + j + 1])
        {
            b[k] = arr[l + i];
            i++;
        }
        else
        {
            b[k] = arr[m + j + 1];
            j++;
        }
        k++;
    }

    while(i < n1){
        b[k] = arr[l+i];
        i++;
        k++;
    }
    while(j<n2){
        b[k] = arr[m+j+1];
        j++;
        k++;
    }

    for(int m = 0 ; m < k ; m++){
        arr[l+m] = b[m];
    }
}

void MergeSort(int *arr, int l, int r)
{
    if (l != r)
    {
        int m = (l + r) / 2;
        MergeSort(arr, l, m);
        MergeSort(arr, m + 1, r);
        Merge(arr, l, m, r);
    }
}

int main()
{
    int size;
    scanf("%d",&size);
    int *arr = (int *)malloc(size*sizeof(int));
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    time_t start = clock();
    MergeSort(arr, 0, size - 1);
    time_t end = clock();
    printf("%.10f",(double)(end-start)/CLOCKS_PER_SEC);
    return 0;
}
