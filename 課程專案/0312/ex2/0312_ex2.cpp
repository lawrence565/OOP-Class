#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

void outputVector(const vector<int> &);
void inputVector(vector<int> &);
int boxVolume(int length, int width, int height);
int cube(int a);

int main()
{
    vector<int> integers1(4);
    vector<int> integers2(6);

    cout << "Size of intergers1 is: " << integers1.size() << "\nVector after initialization: " << endl;
    outputVector(integers1);

    cout << "Size of intergers2 is: " << integers2.size() << "\nVector after initialization: " << endl;
    outputVector(integers2);

    cout << "input 6 numbers:" << endl;
    for (int i = 0; i < integers1.size(); i++)
    {
        if (i == 3)
        {
            break;
        }
        else
        {
            cin >> integers1[i];
        }
    }
    for (int i = 0; i < integers2.size(); i++)
    {
        if (i % 2 == 1)
        {
            continue;
        }
        else
        {
            cin >> integers2[i];
        }
    }

    // cin >> integers1[0] >> integers1[1] >> integers1[2] >> integers2[0] >> integers2[2] >> integers2[4];

    integers1[3] = boxVolume(integers1[0], integers1[1], integers1[2]);
    integers2[1] = cube(integers2[0]);
    integers2[3] = cube(integers2[2]);
    integers2[5] = cube(integers2[4]);

    cout << "After input, the vectors contain" << endl;
    cout << "intergers1" << endl;
    outputVector(integers1);

    cout << "intergers2" << endl;
    outputVector(integers2);
}

void outputVector(const vector<int> &array)
{
    size_t i;
    for (i = 0; i < array.size(); i++)
    {
        cout << setw(12) << array[i];
        if ((i + 1) % 4 == 0)
        {
            cout << endl;
        }
    }
    if (i % 4 != 0)
    {
        cout << endl;
    }
}

void inputVector(vector<int> &array)
{
    for (size_t i = 0; i < array.size(); i++)
    {
        cin >> array[i];
    }
}

int boxVolume(int length, int width, int height)
{
    return length * width * height;
}

int cube(int a)
{
    return a * a * a;
}