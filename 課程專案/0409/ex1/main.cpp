#include <iostream>
#include "Car.h"
#include "VanCar.h"
#include "SportCar.h"
using namespace std;

int main()
{
     // TODO: 建立一般汽車物件
     Car normalCar = Car();
     // TODO: 設定一般汽車品牌為 TOYOTA
     normalCar.SetBrand(Car::TOYOTA);
     cout << "Ordinary Car Brand: " << normalCar.GetBrandName() << endl;
     // TODO: 設定一般汽車目前車速為 20
     normalCar.SetSpeed(20);
     cout << "Ordinary Car Original Speed: " << normalCar.GetSpeed() << endl;
     // TODO: 呼叫一般汽車的加速方法
     normalCar.Accelerate();
     cout << "Speed after Accelerated: " << normalCar.GetSpeed() << endl;
     // TODO: 呼叫一般汽車的煞車方法
     normalCar.Brake();
     cout << "Speed after Brake: " << normalCar.GetSpeed() << endl
          << endl;

     // TODO: 建立箱型車物件
     VanCar vanCar = VanCar();
     // TODO: 設定箱型車品牌為 HONDA
     vanCar.SetBrand(Car::HONDA);
     cout << "Sports Car Brand: " << vanCar.GetBrandName() << endl;
     // TODO: 設定箱型車目前車速為 25
     vanCar.SetSpeed(25);
     cout << "Sports Car Original Speed: " << vanCar.GetSpeed() << endl;

     // TODO: 呼叫箱型車的加速方法
     vanCar.Accelerate();
     cout << "Speed after Accelerated: " << vanCar.GetSpeed() << endl;
     // TODO: 呼叫箱型車的煞車方法
     vanCar.Brake();
     cout << "Speed after Brake: " << vanCar.GetSpeed() << endl
          << endl;

     // TODO: 建立跑車物件
     SportCar sportCar = SportCar();
     // TODO: 設定跑車品牌為 BMW
     sportCar.SetBrand(Car::BMW);
     cout << "Sports Car Brand: " << sportCar.GetBrandName() << endl;
     // TODO: 設定跑車目前車速為 30
     sportCar.SetSpeed(30);
     cout << "Sports Car Original Speed: " << sportCar.GetSpeed() << endl;
     // TODO: 呼叫跑車的加速方法
     sportCar.Accelerate();
     cout << "Speed after Accelerated: " << sportCar.GetSpeed() << endl;
     // TODO: 呼叫跑車的煞車方法
     sportCar.Brake();
     cout << "Speed after Brake: " << sportCar.GetSpeed() << endl
          << endl;
     return 0;
}
