#include <iostream>
#include "sort.h"
using namespace std;

int main()
{
    int a, b, c;

    cout << "input three number: " << endl;
    cin >> a >> b >> c;
    sort(a, b, c);

    return 0;
}
