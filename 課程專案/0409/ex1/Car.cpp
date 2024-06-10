#include "Car.h"
#include "VanCar.h"
#include "SportCar.h"

Car::Car() : current_speed(0), brand(TOYOTA){};

void Car::SetSpeed(float new_speed)
{
    current_speed = new_speed;
}

float Car::GetSpeed()
{
    return current_speed;
}

void Car::Accelerate()
{
    current_speed += 10.0f;
}

void VanCar::Accelerate()
{
    current_speed += 5.0f;
}

void SportCar::Accelerate()
{
    current_speed += 50.0f;
}

void Car::Brake()
{
    if (current_speed < 10.0f)
        current_speed = 0;
    else
        current_speed -= 10.0f;
}

void VanCar::Brake()
{
    if (current_speed < 5.0f)
        current_speed = 0;
    else
        current_speed -= 5.0f;
}

void SportCar::Brake()
{
    if (current_speed < 50.0f)
        current_speed = 0;
    else
        current_speed -= 50.0f;
}

void Car::SetBrand(CarBrand new_brand)
{
    brand = new_brand;
}

string Car::GetBrandName()
{
    switch (brand)
    {
    case HONDA:
        return "HONDA";
        break;
    case TOYOTA:
        return "TOYOTA";
        break;
    case BMW:
        return "BMW";
        break;
    }
}
