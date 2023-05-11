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
  int account = 0;

  cout << "Initial account balance = " << account << endl
       << endl;

  while (1)
  {
    int n;
    cout << "Enter the number you wish to insert in the dynamic table: ";
    cin >> n;
    account += 3; // adding 3 in account

    if (count < size)
    {
      *(p + count) = n;
      count += 1;
      print(p, count);
      account -= 1;
    }
    else
    {
      cout << "Double" << endl;
      int *new_arr = new int[size * 2];
      for (int i = 0; i < count; i++)
      {
        new_arr[i] = *(p + i);
      }
      account -= count;
      p = new_arr;
      *(p + count) = n;
      size *= 2;
      count += 1;
      account -= 1;
      print(p, count);
    }
    cout << "Account balance: " << account << endl;
    cout << endl;
  }

  return 0;
}

// fot STACK in py
// def multipop(S, k):
//     for i in range(k):
//         S.pop(-1)
// def mstack():
//     S = []
//     A = [5,7,9,2,8,6,3,1,7,3,10,8,4,9]
//     total_cost = 0
//     print(" Cost of operation\t\tStack")
//     for i in range(len(A)):
//         cost = 0
//         if A[i] < len(S) or A[i] == len(S):
//             multipop(S, A[i])
//             cost += A[i]
//         S.append(A[i])
//         cost += 1
//         print("\t", cost , "\t\t\t", S)
//         total_cost += cost
//     print("Asymptotic cost for each operation : ", len(A))
//     print("Amortized cost for each operation : ", round(total_cost/len(A)))
// print("AGGREGATE METHOD USING STACK")
// mstack()