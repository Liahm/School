
#ifndef Wiingy_
#define Wiingy_

#include <string>
#include "Enemy.h"

using namespace std;
//Last boss

class Wiingy : public enemy
{
private:
	string my_name;
	int my_health;
	bool heal;
public:
	Wiingy(string n = "Wiingy");

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

Wiingy::Wiingy(string n)
{
	my_name = n;
	my_health = 200;
	heal = false;
}
string Wiingy::getName()const
{
	return my_name;
}
string Wiingy::getDescription()const
{
	return "After killing The Dragon Turtle, a Winged creature appears. Wiingy, the The Eternal appears. She managed to kill 9 people in less than 10 seconds.";
}
void Wiingy::attackOne(enemy* target)
{
	//30% chance
	heal = false;
	target->doDamage(8);
	for (int i = 0; i < rand() % 5; i++)
	{
		target->doDamage(4);
		if(i>3)
			my_health -= 4;
	}
	//idea taken from http://i.imgur.com/2jNYQp2.jpg
}
void Wiingy::attackTwo(enemy* target)
{
	//20% chance
	heal = false;
	target->doDamage(15);
}
void Wiingy::attackThree(enemy* target)
{
	//5% chance
	for (int i = 0; i < 9; i++)
	{
		target->doDamage(rand() % 5);
	}

}
void Wiingy::attackFour(enemy* target)
{
	//25% chance
	heal = false;
	target->doDamage(3);
	if (my_health <= 100)
	{
		my_health = my_health + (rand() % 20);
	}
	else
		target->doDamage(17);
}
void Wiingy::usePotion(enemy* target)
{
	//20%
	heal = true;
}
string Wiingy::attackOneName() const
{
	return "Wiingy said \"No, no no no\" in a high pitch";
}
string Wiingy::attackTwoName() const
{
	return "Pew Pew Pew";
}
string Wiingy::attackThreeName() const
{
	return "Savage";
}
string Wiingy::attackFourName() const
{
	return "Salute the Sun";
}
string Wiingy::usePotionName() const
{
	return "Magical Trip";
}
int Wiingy::getHealth()const
{
	return my_health;
}
void Wiingy::doDamage(int damage)
{
	if (heal)
	{
		my_health += 30;
	}
	else
	{
		my_health = my_health - damage;
	}
}
void Wiingy::resetHealth()
{
	my_health = 200;
}

#endif
