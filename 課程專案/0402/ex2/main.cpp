#include <iostream>
#include "Triangle.h"
using namespace std;

void DisplayTriangleType(Triangle &tri)
{
    float *side_length = tri.GetSideLength();
    cout << "邊長為（" << side_length[0] << ", " << side_length[1] << ", " << side_length[2] << "）的三角形屬於:";
    switch (tri.GetType())
    {
    case Triangle::Equilateral:
        cout << "Equilateral" << endl;
        break;
    case Triangle::Isosceles:
        cout << "Isosceles" << endl;
        break;
    case Triangle::Right:
        cout << "Right" << endl;
        break;
    case Triangle::Normal:
        cout << "Normal" << endl;
        break;
    case Triangle::Invalid:
        cout << "Invalid" << endl;
        break;
    }
}

int main()
{
    Triangle triangle(3, 3, 3), triangle2(4, 4, 5), triangle3(3, 4, 5), triangle4(3, 4, 6), triangle5(2, 2, 4);
    DisplayTriangleType(triangle);
    DisplayTriangleType(triangle2);
    DisplayTriangleType(triangle3);
    DisplayTriangleType(triangle4);
    DisplayTriangleType(triangle5);

    float side1, side2, side3;
    cout << endl
         << "請輸入三角形 3 邊長: ";
    cin >> side1 >> side2 >> side3;
    Triangle userTriangle(side1, side2, side3);
    DisplayTriangleType(userTriangle);

    return 0;
}