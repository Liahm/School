#pragma once
#ifndef MONSTER_
#define MONSTER_

#include <string>

using namespace std;

class enemy
{
public:
	enemy();
	virtual string getName() const = 0;
	virtual string getDescription() const = 0;

	virtual void attackOne(enemy * target) = 0;
	virtual void attackTwo(enemy * target) = 0;
	virtual void attackThree(enemy * target) = 0;
	virtual void attackFour(enemy * target) = 0;
	virtual void usePotion(enemy * target) = 0;

	virtual string attackOneName() const = 0;
	virtual string attackTwoName() const = 0;
	virtual string attackThreeName() const = 0;
	virtual string attackFourName() const = 0;
	virtual string usePotionName() const = 0;

	virtual int getHealth() const = 0;
	virtual void doDamage(int damage) = 0;
	virtual void resetHealth() = 0;

};

enemy::enemy()
{
}

#endif