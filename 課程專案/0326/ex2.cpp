#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef struct carType
{
    string brand;
    unsigned int price;
} CarType_t;

class CarRepository
{
public:
    CarRepository()
    {
        cout << "Cars in the repository" << endl;
    }

    // 增加廠牌為 carBrand、價格為 carPrice 的汽車到車庫 cars 中
    void AddCar(string carBrand, unsigned int carPrice)
    {
        CarType_t new_car;
        new_car.brand = carBrand;
        new_car.price = carPrice;
        cars.insert(cars.end(), new_car);
    };
    // 刪除在車庫中第 carNumber 台汽車，若 carNumber
    // 在 cars 數量範圍內回傳 true，若超出範圍，回傳 false
    bool DeleteCar(int carNumber)
    {
        if (carNumber < cars.size())
        {
            cars.erase(cars.begin() + carNumber);
        }
        else
        {
            return false;
        }

        return true;
    };

    // 顯示在車庫中的所有汽車廠牌與價格
    void ShowCars()
    {
        for (int i = 0; i < cars.size(); i++)
        {
            cout << "Car N0." << i << endl;
            cout << "Car Brand: " << cars[i].brand << endl;
            cout << "Car Price: " << cars[i].price << endl;
            cout << endl;
        }
    };

private:
    // 停在車庫的汽車
    vector<CarType_t> cars;
};

int main()
{
    CarRepository repo;
    string newCar;
    int newCarPrice;

    repo.AddCar("Maserati", 350000);
    repo.AddCar("BMW", 85000);
    repo.AddCar("Toyota", 17000);
    cout << "請輸入新車品牌：";
    cin >> newCar;
    cout << "請輸入新車價格：";
    cin >> newCarPrice;
    repo.AddCar(newCar, newCarPrice);
    repo.ShowCars();

    int deleteCarNo;
    cout << "Enter Car No. you want to delete: ";
    cin >> deleteCarNo;

    if (repo.DeleteCar(deleteCarNo) == false)
        cout << "Car No." << deleteCarNo + 1 << " is invalid!" << endl;
    else
        repo.ShowCars();

    return 0;
}
