#include <iostream>
#include <stdio.h>
#include <unordered_set>
using namespace std;

void findSumPair(int arr[], int size, int sum)
{
    std::unordered_set<int> seen;
    for (int i = 0; i < size; ++i)
    {
        int diff = sum - arr[i];
        if (seen.find(diff) != seen.end())
        {
            std::cout << "Match Found: (" << arr[i] << ", " << diff << ")\n";
        }
        seen.insert(arr[i]);
    }
}

// Driver program to test above functions
int main()
{
    int arr[] = {5, 8, 9, 4, 3, 6};
    int N = sizeof(arr) / sizeof(arr[0]);
    int givenSum = 14;
    findSumPair(arr, N, givenSum);
    return 0;
}