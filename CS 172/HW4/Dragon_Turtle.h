#pragma once

#ifndef DRAGON_TURTLE_
#define DRAGON_TURTLE_

#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Enemy.h"

using namespace std;
//Almost Last Boss
class Dragon_Turtle : public enemy
{
private:
	string my_name;
	int my_health;
	bool heal;
public:
	Dragon_Turtle(string n = "Dragon Turtle");

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

Dragon_Turtle::Dragon_Turtle(string n)
{
	my_name = n;
	my_health = 300;
	heal = false;
}
string Dragon_Turtle::getName()const
{
	return my_name;
}
string Dragon_Turtle::getDescription()const
{
	return "You have been walking on top of him this entire time and didn't notice?! He likes money and seem to have curative powers.";
}
void Dragon_Turtle::attackOne(enemy* target)
{
	//30% chance
	heal = false;
	target->doDamage(rand() % 20);
}
void Dragon_Turtle::attackTwo(enemy* target)
{
	//20% Chance
	heal = false;
	target->doDamage(0);
}
void Dragon_Turtle::attackThree(enemy* target)
{
	//5% chance
	heal = false;
	target->doDamage(60);
}
void Dragon_Turtle::attackFour(enemy* target)
{
	//25% chance
	heal = false;
	target->doDamage(10);
}
void Dragon_Turtle::usePotion(enemy* target)
{
	//20% chance
	heal = true;
}
string Dragon_Turtle::attackOneName() const
{
	return "Windbore Gust";
}
string Dragon_Turtle::attackTwoName() const
{
	return "Glare";
}
string Dragon_Turtle::attackThreeName() const
{
	return "World Shake";
}
string Dragon_Turtle::attackFourName() const
{
	return "Roar";
}
string Dragon_Turtle::usePotionName() const
{
	return "Guard";
}
int Dragon_Turtle::getHealth()const
{
	return my_health;
}
void Dragon_Turtle::doDamage(int damage)
{
	if (heal)
	{
		my_health = my_health -(damage/2);
	}
	else
	{
		my_health = my_health - damage;
	}
}
void Dragon_Turtle::resetHealth()
{
	my_health = 300;
}
#endif
