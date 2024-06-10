#pragma once
#include <iostream>
#include <string>
using namespace std;

class Car
{
public:
    enum CarBrand
    {
        HONDA,
        TOYOTA,
        BMW,
    };

    // 建構式初始化 current_speed 以及 brand
    Car();

    // 設定汽車廠牌，將 new_brand 參數放到 brand
    void SetBrand(CarBrand new_brand);
    // 取得汽車廠牌，依照 brand 的存放內容回傳廠牌名稱
    string GetBrandName();

    // 設定目前車速，將 new_speed 參數放到 current_speed
    void SetSpeed(float new_speed);
    // 取得目前車速，回傳 current_speed
    float GetSpeed();

    // 讓車子加速，一般汽車將目前速度累加 10
    virtual void Accelerate();
    // 讓車子煞車，一般汽車將目前速度遞減 10
    virtual void Brake();

protected:
    CarBrand brand;
    float current_speed;
};
