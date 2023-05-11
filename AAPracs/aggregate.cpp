#include <bits/stdc++.h>

using namespace std;

void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    int size = 1;
    int count = 0;
    int arr[size];
    int *p = arr;
    int cost = 0;

    while (1)
    {
        int n;
        cout << "Enter the number you wish to insert in the dynamic table: ";
        cin >> n;
        if (count < size)
        {
            *(p + count) = n;
            count += 1;
            cout << p << endl;
            print(p, count);
            cost += 1;
        }
        else
        {
            // double array
            cout << "Double" << endl;
            int *new_arr = new int[size * 2];
            for (int i = 0; i < count; i++)
            {
                // cout<<*(p+i)<<endl;
                new_arr[i] = *(p + i);
            }
            cost += count + 1;
            size *= 2;
            new_arr[count] = n;
            count += 1;
            p = new_arr;
            cout << p << endl;
            print(p, count);
        }
        cout << "Ammortized Cost: " << cost << endl;
        cout << endl;
    }
    return 0;
}