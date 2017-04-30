
#ifndef GARM_
#define GARM_

#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Enemy.h"

using namespace std;
//Third boss
class Garm : public enemy
{
private:
	string my_name;
	int my_health;
	bool heal;
public:
	Garm(string n = "Garm");

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

Garm::Garm(string n)
{
	my_name = n;
	my_health = 500;
	heal = false;
}
string Garm::getName()const
{
	return my_name;
}
string Garm::getDescription()const
{
	return "Someone with special needs and will scream \"Aloha Snackbar\" ";
}
void Garm::attackOne(enemy* target)
{
	//30% chance
	heal = false;
	target->doDamage(10);
	my_health -= 10;
	if (my_health <= 250)
	{
		target->doDamage(15);
		my_health -= 15;
	}
}
void Garm::attackTwo(enemy* target)
{
	//20% chance
	heal = false;
	target->doDamage(8);
	my_health -= 8;
	for (int i = 0; i < rand() % 3; i++)
	{
		target->doDamage(8);
		my_health -= 8;
	}
}
void Garm::attackThree(enemy* target)
{
	//5% chance
	heal = false;
	if (my_health <= 250)
	{
		target->doDamage((rand() % 80)+30);
		my_health -= my_health;
	}
}
void Garm::attackFour(enemy* target)
{
	//25% chance
	heal = false;
	target->doDamage(10);
	my_health += 5;
}
void Garm::usePotion(enemy* target)
{
	//20% chance
	heal = true;
}
string Garm::attackOneName() const
{
	return "Spit";
}
string Garm::attackTwoName() const
{
	return "Sloth Swipe";
}
string Garm::attackThreeName() const
{
	if (my_health <= 250)
		return "ALOHA SNACKBAR!";
	else
		return "You guys are crazy";
}
string Garm::attackFourName() const
{
	return "You've been kick out from the server";
}
string Garm::usePotionName() const
{
	return "WHAT IS THIS?!";
}
int Garm::getHealth()const
{
	return my_health;
}
void Garm::doDamage(int damage)
{
	if (heal)
	{
		my_health -= 50;
	}
	else if(my_health <= 250 )
	{
		my_health = my_health - damage;
	}
	else
	{
		my_health = my_health - (damage * 2);
	}
}
void Garm::resetHealth()
{
	my_health = 500;
}

#endif
