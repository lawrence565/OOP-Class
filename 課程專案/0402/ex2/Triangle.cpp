#include "Triangle.h"
#include <iostream>

Triangle::Triangle(float length1, float length2, float length3)
{
    Triangle::sideLength[0] = length1;
    Triangle::sideLength[1] = length2;
    Triangle::sideLength[2] = length3;
};

Triangle::Type Triangle::GetType(){
    float long1;
    float short1;
    float short2;

    if (sideLength[0] > sideLength[1] && sideLength[0] > sideLength[2])
    {
        long1 = sideLength[0];
        short1 = sideLength[1];
        short2 = sideLength[2];
    }
    else if (sideLength[1] > sideLength[0] && sideLength[1] > sideLength[2])
    {
        long1 = sideLength[1];
        short1 = sideLength[0];
        short2 = sideLength[2];
    }
    else
    {
        long1 = sideLength[2];
        short1 = sideLength[0];
        short2 = sideLength[1];
    }

    if (sideLength[0] + sideLength[1] < sideLength[2])
    {
        std::cout << Invalid;
        return Invalid;
    }
    else if (long1 * long1 == short1 * short1 + short2 * short2)
    {
        std::cout << Right;
        return Right;
    }
    else if(sideLength[0] == sideLength[1] == sideLength[2]) {
        std::cout << Equilateral;
        return Equilateral;
    }
    else if (sideLength[0] == sideLength[1] || sideLength[1] == sideLength[2] || sideLength[0] == sideLength[2])
    {
        std::cout << Isosceles;
        return Isosceles;
    }else 
    {
        std::cout << Normal;
        return Normal;
    }
}

float* Triangle::GetSideLength()
{
    return sideLength;
}