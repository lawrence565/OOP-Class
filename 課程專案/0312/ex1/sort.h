#ifndef sort_h
#define sort_h
#include <iostream>
using namespace std;

template <class T>

void sort(T a, T b, T c)
{
    int arr[] = {a, b, c};
    int n = sizeof(arr) / sizeof(arr[0]);
    int mid;

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    cout << arr[0] << "=>" << arr[1] << "=>" << arr[2];
}

#endif
