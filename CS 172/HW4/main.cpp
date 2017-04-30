#include <iostream>
#include <string>
#include <stdlib.h> //This is where random numbers live
#include <time.h> //To set the random number generator
#include "Hero.h"
#include "Enemy.h"
#include "Dragon_Turtle.h"
#include "Aquariuz.h"
#include "Garm.h"
#include "Wiingy.h"
#include "Shane.h"

void print_results(enemy* attacker, enemy* defender, string attack, int hchange);
int cast = 10;
int potions = 6;

enemy* battle(enemy* e1, enemy* e2)
{
	//e1->resetHealth();
	e2->resetHealth();

	cout << "Starting Battle Between " << endl;
	cout << e1->getName() << endl;
	cout << e2->getName() << ": " << e2->getDescription() << endl;

	enemy* attacker = NULL;
	enemy* defender = NULL;

		attacker = e2;
		defender = e1;

	cout << attacker->getName() << " goes first. " << endl;

	//AI
	//Using code from previous lab.
	while (e1->getHealth() > 0 && e2->getHealth() > 0)
	{
		int move = rand() % 100 + 1;

		int before_health = defender->getHealth();

		if (move >= 1 && move <= 30)
		{
			//Attack 1
			attacker->attackOne(defender);
			print_results(attacker, defender, attacker->attackOneName(), before_health - defender->getHealth());
		}
		if (move >= 31 && move <= 50)
		{
			//Attack 2
			attacker->attackTwo(defender);
			print_results(attacker, defender, attacker->attackTwoName(), before_health - defender->getHealth());
		}
		if (move >= 51 && move <= 55)
		{
			//Attack 3
			attacker->attackThree(defender);
			print_results(attacker, defender, attacker->attackThreeName(), before_health - defender->getHealth());
		}
		if (move >= 56 && move <= 80)
		{
			//Attack 4
			attacker->attackFour(defender);
			print_results(attacker, defender, attacker->attackFourName(), before_health - defender->getHealth());
		}
		if (move >= 81 && move <= 100)
		{
			//Heal/block/defensive move
			attacker->usePotion(attacker);
			print_results(attacker, attacker, attacker->usePotionName(), before_health - attacker->getHealth());
		}

		//Player
		int before_health_2 = attacker->getHealth();
		int choice;
		cout << "It's your turn, what do you want to do. " << endl;
		cout << "Attack(1), Shield(2), Fireball(3), Potion(4), Exit(5)." << endl;
		cin >> choice;
		if (choice == 1)
		{
			//70% chance of dealing normal damage
			if (move >= 1 && move <= 70)
			{
				defender->attackOne(attacker);
				print_results(defender, attacker, defender->attackOneName(), before_health_2 - attacker->getHealth());
			}
			//30% chance of dealing a critical blow
			if (move >= 71 && move <= 100)
			{
				defender->attackTwo(attacker);
				print_results(defender, attacker, defender->attackTwoName(), before_health_2 - attacker->getHealth());
			}
		}
		else if (choice == 2)
		{//Shield blocks 100%
			defender->attackFour(attacker);
			print_results(defender, attacker, defender->attackFourName(), before_health_2 - attacker->getHealth());
		}
		else if (choice == 3)
		{
			//Fireballs
			if (cast > 0)
			{
				cast--;
				defender->attackThree(attacker);
				print_results(defender, attacker, defender->attackThreeName(), before_health_2 - attacker->getHealth());
				cout << cast << " remaining fireballs " << endl;
			}
			else
				cout << "No more fireballs" << endl;
		}
		else if (choice == 4)
		{
			//40 HP potions
			if (potions > 1)
			{
				potions--;
				defender->usePotion(defender);
				print_results(defender, defender, defender->usePotionName(), before_health_2 - defender->getHealth());
				cout << "You used potion and healed for 40" << endl;
				cout << potions << " remaining potions" << endl;
			}
			else
			{
				//bug, it will, for some reason, continue healing even after 0 potions are left when there is no code for it to run.
				//not sure how to fix it.
				cout << "No more potions" << endl;
			}
		}
		else if (choice == 5)
		{
			cout << "Thanks for playing the game" << endl;
			return 0;
		}
		else if (choice != 1 || choice != 2 || choice != 3 || choice != 4 || choice != 5)
		{
			cout << "Yea... your turn is over because of your decision." << endl;
		}
		cout << e1->getName() << " at " << e1->getHealth() << " health." << endl;
		cout << e2->getName() << " at " << e2->getHealth() << " health." << endl;
	}
	if (e1->getHealth() < 1 && e2->getHealth() < 1)
	{
		cout << "Both the hero and the enemy died. You might have reached " << e2->getName() << " but your efforts are useless. You will never see your home again." << endl;
		return NULL;
	}
	if (e1->getHealth() < 1)
	{
		cout << e2->getName() << " destroyed you. You will never see the world again" << endl;
		return e2;
	}
	if (e2->getHealth() <1)
	{
		cout << "You defeated " << e2->getName() << endl;
		return e1;
	}
	cout << "ugh, I don't know what happened" << endl;
	return NULL;
}

void print_results(enemy* attacker, enemy* defender, string attack, int hchange)
{
	cout << attacker->getName() << " used " << attack;
	cout << " on " << defender->getName() << endl;
	cout << "The attack did " << hchange << " damage." << endl;
}

int main()
{
	string name;
	string choice;
	cout << "Welcome to our world Hero." << endl;
	cout << "What's your name?" << endl;
	getline(cin, name);
	cout << "Wait, you aren't the chosen one." << endl;
	cout << "Yes... yes... anyway, you will do " << name << " your mission is to go to the top of the mountain and kill Garm." << endl;
	cout << "You can't go back to your world until you kill him because he was the one who summoned you for some reason." << endl;
	cout << "Here you go, a sword, armor, the all mighty spell in a flask and potions." << endl;
	cout << "Go Hero!" << endl;
	cout << endl << endl;
	cout << "Instructions, You have 5 choices, attack, defend, magic, heal and escape." << endl;
	cout << "Press the number key besides the word to activate it. If you press something else it might cause your death." << endl;
	cout << "Understood? y/n" << endl;
	getline(cin, choice);
	if (choice == "y")
	{
		enemy* first = new Hero(name);
		enemy* second = new Aquariuz("Aquariuz");
		enemy* Third = new Shane("Shane");
		enemy* Fourth = new Garm("Garm");
		enemy* Fifth = new Dragon_Turtle("Dragon_Turtle");
		enemy* Final = new Wiingy("Wiingy");

		enemy* FightOne = battle(first, second);
		if (second->getHealth() < 1)
		{
			cout << first->getDescription() << endl;
			cout << "You have defeated Aquariuz, like, wth was that fight." << endl;
			enemy* FightTwo = battle(first, Third);
			if (Third->getHealth() < 1)
			{
				cout << "You just killed Shane, The right hand of Garm. His heals were strong right?" << endl;
				enemy* FightThird = battle(first, Fourth);
				if (Fourth->getHealth() < 1)
				{
					cout << "Did... did he just kill himself?" << endl;
					cout << "Time to go back..." << endl << endl;
					cout << "What the Heck is this." << endl;
					enemy* FightFourth = battle(first, Fifth);
					if (Fifth->getHealth() < 1)
					{
						cout << "WHAT THE HECK, THIS WASN'T A MOUNTAIN, AND WHAT THE HECK JUST APPEARED?!" << endl;
						enemy* FightFinal = battle(first, Final);
						cout << "YOU HAVE DEFEATED THE MASTER MIND!" << endl;
					}
				}
			}
		}
	}
	else
	{
		cout << "well, I will close the game" << endl;
		return 0;
	}
}