#include <iostream>
#include "PlayGround.h"

using namespace std;

int main()
{
    PlayGround playGround(5);

    cout << "\n請使用方向鍵上下增加、減少人數，按下 ESC 離開程式" << endl;
    cout << "目前空地人數為：" << playGround.getCurrentCount() << endl;

    char key;
    key = getchar();
    cout << key;

    do
    {
        key = (char)getchar();
        cout << (char)key;

        if (key == (char)72) // 上
        {
            if (playGround.AddCount() == false)
            {
                cout << "空地人數已滿！" << endl;
                continue;
            }
        }
        else if (key == 80) // 下
        {
            if (playGround.DecreaseCount() == false)
            {
                cout << "空地沒有人！" << endl;
                continue;
            }
        }
        cout << "目前空地人數：" << (char)playGround.getCurrentCount();
    } while (true);

    return 0;
}