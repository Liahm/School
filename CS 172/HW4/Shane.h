
#ifndef SHANE_
#define SHANE_

#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Enemy.h"

using namespace std;
//Second Boss
class Shane : public enemy
{
private:
	string my_name;
	int my_health;
	bool heal;
public:
	Shane(string n = "Shane");

	string getName() const; //Not sure if I actually need this
	string getDescription() const;
	virtual void attackOne(enemy * target);
	virtual void attackTwo(enemy * target);
	virtual void attackThree(enemy * target);
	virtual void attackFour(enemy * target);
	virtual void usePotion(enemy * target);

	virtual string attackOneName()const;
	virtual string attackTwoName()const;
	virtual string attackThreeName()const;
	virtual string attackFourName()const;
	virtual string usePotionName()const;

	int getHealth() const;
	void doDamage(int damage);
	void resetHealth();

};

Shane::Shane(string n)
{
	my_name = n;
	my_health = 50;
	heal = false;
}
string Shane::getName()const
{
	return my_name;
}
string Shane::getDescription()const
{
	return "Told by the community to be the Ameno guy";
}
void Shane::attackOne(enemy* target)
{
	//30% chance
	heal = false;
	my_health = my_health + 20;
	if (my_health > 100)
	{
		target->doDamage(rand()%20);
	}
}
void Shane::attackTwo(enemy* target)
{
	//20% chance
	heal = false;
	target->doDamage(15);
	my_health = my_health + 5;
}
void Shane::attackThree(enemy* target)
{
	//5% chance
	heal = false;
	if (my_health <= 20)
	{
		my_health += 50;
	}
	else
	{
		target->doDamage(25);
	}
}
void Shane::attackFour(enemy* target)
{
	//25% chance
	heal = false;
	target->doDamage(rand() % 10);
	for (int i = 0; i < rand() % 3; i++)
	{
		target->doDamage(rand()%5);
	}
}
void Shane::usePotion(enemy* target)
{
	//20%
	heal = true;
}
string Shane::attackOneName() const
{
	return "Ameno";
}
string Shane::attackTwoName() const
{
	return "Music Bot";
}
string Shane::attackThreeName() const
{
	return "Be a MAN!";
}
string Shane::attackFourName() const
{
	return "SANDSTORM";
}
string Shane::usePotionName() const
{
	return "Teleport";
}
int Shane::getHealth()const
{
	return my_health;
}
void Shane::doDamage(int damage)
{
	if (heal)
	{
		my_health = my_health;
	}
	else
	{
		my_health = my_health - damage;
	}
}
void Shane::resetHealth()
{
	my_health = 50;
}
#endif
