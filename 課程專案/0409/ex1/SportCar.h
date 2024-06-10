#include "Car.h"

class SportCar : public Car
{
public:
    // To do覆寫原先在一般汽車的加速方法，箱型車讓目前速度遞增 5
    void Accelerate();

    // To do覆寫原先在一般汽車的煞車方法，箱型車讓目前速度遞減 5
    void Brake();
};
