#pragma once

class Triangle
{
public:
    enum Type
    {
        Equilateral,
        Isosceles,
        Right,
        Normal,
        Invalid
    };

    Triangle(float length1, float length2, float length3);

    Type GetType();

    float *GetSideLength();

private:
    float sideLength[3];
};
