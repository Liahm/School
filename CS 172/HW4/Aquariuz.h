#pragma once
#ifndef Aquariuz_
#define Aquariuz_

#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Enemy.h"

using namespace std;
//Easy Monster, first encounter
class Aquariuz : public enemy
{
private:
	string my_name;
	int my_health;
	bool heal;
public:
	Aquariuz(string n = "Aquariuz");

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

Aquariuz::Aquariuz(string n)
{
	my_name = n;
	my_health = 100;
	heal = false;
}
string Aquariuz::getName()const
{
	return my_name;
}
string Aquariuz::getDescription()const
{
	return "Legends say that the mythical creature called Aquariuz was fighting the all mighty Gorseval when suddenly he reached for a Lightning Hammer and never to be seen again.";
}
void Aquariuz::attackOne(enemy* target)
{
	//30% chance
	heal = false;
	target->doDamage(rand()%10);
}
void Aquariuz::attackTwo(enemy* target)
{
	//20% chance
	heal = false;
	target->doDamage(rand() % 20);
}
void Aquariuz::attackThree(enemy* target)
{
	//5% chance
	heal = false;
	target->doDamage(30);
}
void Aquariuz::attackFour(enemy* target)
{
	//25% chance
	heal = false;
	target->doDamage(10);
	my_health -= 5;
}
void Aquariuz::usePotion(enemy* target)
{
	//20% chance
	heal = true;

}
string Aquariuz::attackOneName() const
{
	return "Lightning Swipe";
}
string Aquariuz::attackTwoName() const
{
	return "Lightning Storm";
}
string Aquariuz::attackThreeName() const
{
	return "Thunderclap";
}
string Aquariuz::attackFourName() const
{
	return "Overload!";
}
string Aquariuz::usePotionName() const
{
	return "Charge";
}
int Aquariuz::getHealth()const
{
	return my_health;
}
void Aquariuz::doDamage(int damage)
{
	if (heal)
	{
		my_health += 20;
	}
	else
	{
		my_health = my_health - damage;
	}
}
void Aquariuz::resetHealth()
{
	my_health = 100;
}

#endif
