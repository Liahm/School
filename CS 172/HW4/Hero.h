#ifndef HERO_
#define HERO_


#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Enemy.h"

using namespace std;
//Easy Monster, first encounter
class Hero : public enemy
{
private:
	string my_name;
	int my_health;
	bool heal;
	bool shield;
public:
	Hero(string n = "Hero");

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

Hero::Hero(string n)
{
	my_name = n;
	my_health = 200;
	heal = false;
}
string Hero::getName()const
{
	return my_name;
}
string Hero::getDescription()const
{
	return "Oh great Hero from another dimension. Your objective is to reach the top of the mountain and defeat Garm, the autistic villain. Oh, you will see this a lot.";
}
void Hero::attackOne(enemy* target)
{
	//Sword - 70%
	heal = false;
	shield = false;
	target->doDamage(10);
	//no one said anything about magical swords
	if (my_health <= 100)
	{
		target->doDamage((rand()%15)+10);
	}
}
void Hero::attackTwo(enemy* target)
{
	//Critical Sword - 30%
	heal = false;
	shield = false;
	target->doDamage((rand()%10)+20);
}
void Hero::attackThree(enemy* target)
{
	//Fireball
	heal = false;
	shield = false;
	target->doDamage((rand()%30)+20);
}
void Hero::attackFour(enemy* target)
{
	//Shield
	heal = false;
	shield = true;
}
void Hero::usePotion(enemy* target)
{
	heal = true;
	shield = false;
}
string Hero::attackOneName() const
{
	return "Sword Slice!";
}
string Hero::attackTwoName() const
{
	return "Sword Slash";
}
string Hero::attackThreeName() const
{
	return "Fireball!";
}
string Hero::attackFourName() const
{
	return "Block!";
}
string Hero::usePotionName() const
{
	return "Potion";
}
int Hero::getHealth()const
{
	return my_health;
}
void Hero::doDamage(int damage)
{
	if (heal)
	{
		my_health += 40;
	}
	else if (shield)
	{
		my_health = my_health-(damage/2);
	}
	else
	{
		my_health = my_health - damage;
	}
}
void Hero::resetHealth()
{
	my_health = 200;
}



#endif 