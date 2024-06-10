#include "PlayGround.h"

PlayGround::PlayGround(int max) : current_amount(0)
{
    PlayGround::max_count = max >= 1 ? max : 5;
}

bool PlayGround::AddCount()
{
    if (current_amount < max_count)
    {
        PlayGround::current_amount += 1;
        return true;
    }
    else
    {
        return false;
    }
}

bool PlayGround::DecreaseCount()
{
    if (current_amount > 0)
    {
        PlayGround::current_amount -= 1;
        return true;
    }
    else
    {
        return false;
    }
}

int PlayGround::getCurrentCount()
{
    return PlayGround::current_amount;
}