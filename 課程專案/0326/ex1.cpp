#include <iostream>
#include <string>
using namespace std;

class Company
{
public:
    Company(string name)
    {
        company_name = name;
    }
    string get_companyName()
    {
        return company_name;
    }

    void setCompanyName(string name)
    {
        company_name = name;
    }

private:
    string company_name;
};

int main()
{
    string newName;
    Company c1 = Company("NTUT Lab321"); // 需先建立成員才能呼叫函式
    cout << "Original company name is " << c1.get_companyName() << endl;
    cout << endl;
    cout << "Enter the new company name: ";
    getline(cin, newName);
    cout << endl;
    c1.setCompanyName(newName);
    cout << "New company name: " << c1.get_companyName() << endl;
    return 0;
}