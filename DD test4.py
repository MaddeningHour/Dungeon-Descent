from abc import ABC, abstractmethod
from random import *


#Creating an abstract class for User Game Characters
class characterType(ABC):
    def __init__(self, name, health, speed, luck, damage, experience):
        self.name = name
        self.health = health
        self.speed = speed
        self.luck = luck
        self.damage = damage
        self.experience = experience
        self.inventory = []
    

    #Method to return inventory of the player
    def openInventory(self):
        return self.inventory


    #Method to add items to the inventory:
    def addToInventory(self, item):
        if not isinstance(item, Health_Items):
            raise ValueError('ERROR: Item cannot be added to inventory')
        else:
            self.inventory.append(item.name)


    def respawn(self):
        if not self.is_alive():
            self.health = 50


    #Method to get name
    def getName(self):
        return self.name


    #Method to set name
    def setName(self, name):
        self.name = name


    #Method to get damage
    def getDamage(self):
        return self.damage
    

    #Method to get speed
    def getSpeed(self):
        return self.speed
    

    #Abstractmethod to change the values of the player
    @abstractmethod
    def ChangeValues(self, type, amount):
        pass


    #Method to attack enemies  
    def attack(self):
        return self.damage


    #Method to take damage 
    def take_damage(self, amount):
        self.health -= amount


    #Method to determine if a character is alive.
    def is_alive(self):
        return self.health > 0
    
    #Method to set character HP to 0 and death message.
    def death_sequence(self):
        if not self.is_alive():
            self.health = 0
            print(f'{self.name} was slain...')

    #Method to level up the character. Plus health, speed, luck, and reset experience to 0.
    def Level_Up(self, amount):
        self.experience += amount
        
        if self.experience >= 15:
            print(f'{self.name} leveled up!')
            self.health += 15
            self.speed += 5
            self.luck += 5
            self.experience = 0


    #Method to compare speeds between a player and an enemy. Returns true if player is faster. False enemywise.
    def CompareSpeed(self, enemy):
        if not isinstance(enemy, enemyType):
            raise ValueError('Ok?')
        
        if self.speed > enemy.speed:
            return True
        
        elif enemy.speed > self.speed:
            return False
        
        else:
            return False

        
    #Method to fight against enemies. 
    def FightSequence(self, enemy):
        #Validating to check th
        if not isinstance(enemy, (characterType, enemyType)):
            raise ValueError('Invalid thing.')
          
        playerAttack = self.attack()
        enemyAttack = enemy.attack()
        playerAttacked = self.take_damage(enemyAttack)
        enemyAttacked = enemy.take_damage(playerAttack)
        
        if self.CompareSpeed(enemy) ==  True:


            print(f'\n{self.name} attacked {enemy.getName()} with the power of {self.getDamage()}')
            enemyAttacked

            if enemy.is_alive():
                print(f'{enemy.getName()} attacked {self.name} with the power of {enemy.getDamage()}\n')   
                playerAttacked
            
            elif not enemy.is_alive():
                print(f'{enemy.name} was slained brutally by {self.name}')
                
            
            

        else:
            print(f'\n{enemy.getName()} attacked {self.name} with the power of {enemy.getDamage()}')
            playerAttacked
            
            if self.is_alive():

                print(f'{self.name} attacked {enemy.getName()} with the power of {self.getDamage()}\n')    
                enemyAttacked
            
            elif not self.is_alive():
                print(f'{self.name} was finished by a mere foe. Pathetic.')
            


    def PlayerActionChoices(self, enemy):
        x = True

        while x == True:

            if not isinstance(enemy, (characterType, enemyType)):
                raise ValueError('Invalid thing.')
            
        
            
            if enemy.is_alive() and self.is_alive():
                print(f'\nYou are in combat with {enemy}\n')
            
            else:
                return False
            
            myPossibleChoices = ['ATTACK', 'INVENTORY', 'STATS', 'RUN']
            myChoice =  input(f'What would you like to do ({myPossibleChoices[0]}\t{myPossibleChoices[1]}\t{myPossibleChoices[2]}\t{myPossibleChoices[3]}): ').upper()
            while myChoice not in myPossibleChoices:
                print('ERROR! INVALID CHOICE!')
                myChoice =  input(f'What would you like to do ({myPossibleChoices[0]}\t{myPossibleChoices[1]}\t{myPossibleChoices[2]}\t{myPossibleChoices[3]}): ').upper()

            
            
            if myChoice == myPossibleChoices[0]:
                self.FightSequence(enemy)
                x = False
                return True
            
            elif myChoice == myPossibleChoices[1]:
                print(self.openInventory())
                
            
            elif myChoice == myPossibleChoices[2]:
                print('You checked your stats:\n')
                print(self)
            
            else:
                print(f'{self.name} ran away successfully.')
                x = False
                return False
        
    #Method to convert a players luck into an 'odds' percentage.
    def LuckToOdds(self):
        return (self.luck//10)

    #Method to return object as a string. 
    def __str__(self):
        return (f'\n{self.name}:\nHealth: {self.health}\nAttack: {self.damage}\nSpeed: {self.speed}\nLuck: {self.luck}\nExperience: {self.experience}')



        
        
    

        
 
#A class of the abstract class(characterType) known as strength.
class Beserker(characterType):
    #Initializing our Beserker.
    def __init__(self, name, health=100, speed=40, luck=40, damage=15, experience = 0):
        #Using super() method to initialize all of the variables of the parent class.
        super().__init__(name, health, speed, luck, damage, experience)
        

   
    
    #Method to update the the values of our stats. Using type we determine which stat and using amount we adjust accordingly. 
    def ChangeValues(self):
        choices = ['SPEED','HEALTH','LUCK']
        amount = 10
        type = input(f'What stat would you like to buff (SPEED\tHEALTH\tLUCK): ').upper().strip()

        while type not in choices:
            print('ERROR! Invalid choice!')
            type = input(f'What stat would you like to buff (SPEED\tHEALTH\tLUCK): ').upper().strip()



        if type == 'SPEED':
            self.speed += amount
        elif type == 'HEALTH':
            self.health += amount
        elif type == 'LUCK':
            self.luck += amount
        else:
            print('No values were changed.')
    
    

#Abstract class to create our enemies. All enemies have a name, health, speed, and luck variable.
class enemyType(ABC):
    def __init__(self, name, health, speed, luck, damage, experience):
        self.name = name
        self.health = health
        self.speed = speed
        self.luck = luck
        self.damage = damage
        self.experience = experience
    
    #Method to get name.
    def getName(self):
        return self.name
    
    #Method to get speed.
    def getSpeed(self):
        return self.speed
    
    def getDamage(self):
        return self.damage

    @abstractmethod
    def respawn(self):
        pass

    #Method to attack.
    def attack(self):
        return self.damage

    #Method to take damage.
    def take_damage(self, amount):
        self.health -= amount
    
    #Method to check if this object is alive.
    def is_alive(self):
        return (self.health > 0)
    
    def ChangeValues(self, type, amount):
        if type == 'SPEED':
            self.speed += amount
        
        elif type == 'HEALTH':
            self.health += amount

        elif type == 'DAMAGE':
            self.damage += amount

        else:
            print(f'No values were changed for {self.name}')
    
    def __str__(self):
        return (f'{self.name}:\nHealth: {self.health} \nSpeed: {self.speed}\nLuck: {self.luck}\nDamage: {self.damage}')
    




#Class of the abstract class(enemyType).
class Skeleton(enemyType):
    #Initalizing the variables of our Skeleton of enemyType.
    def __init__(self, name='Skullz', health=50, speed=10, luck=10, damage=5, experience = 20):
        super().__init__(name, health, speed, luck, damage, experience)
    
        
    def respawn(self):
        if not self.is_alive():
            self.health = 50            
    

class Cave_Bat(enemyType):
    def __init__(self, name = 'Batty', health = 25, speed = 50, luck = 10, damage = 10, experience = 10):
        super().__init__(name, health, speed, luck, damage, experience)
    

    def respawn(self):
        if not self.is_alive():
            self.health = 25

class Health_Items(ABC):
    def __init__(self, name, healthPoints):
        self.name = name
        self.healthPoints = healthPoints
    def heal(self, enemy):
        if not isinstance(enemy, characterType ):
            raise ValueError 

        print(f'{enemy.name} Used {self.name} for {self.healthPoints} hp')
        enemy.health += self.healthPoints


class SmallHealthPotion(Health_Items):
    def __init__(self, name = 'Small Health Potion', healthPoints = 25):
        super().__init__(name, healthPoints)


class LargeHealthPotion(Health_Items):
    def __init__(self, name = 'Large Health Potion', healthPoints = 50):
        super().__init__(name, healthPoints)

def MultipleEnemy(*enemy):
    myEnemies = []
    for i in enemy:
        if not isinstance(i, enemyType):
            raise ValueError('Could not append enemy to the list')
        else:
            myEnemies.append(i)
    
    return myEnemies

def multipleEnemyIsAlive(enemies):
    for enemy in enemies:
        if not isinstance(enemy, enemyType):
            raise ValueError('Something later here')
        if enemy.is_alive():
            print('At least one enemy is alive!')
            return False
        else:
            print('All enemies are dead')
            return True
    
    
    
        
def gameStart():
    
        #Grabbing a name from the user.
    PlayerName = input('What is the name of your warrior?: ')

    #Initializing a Beserker class with the PlayerName, Health, Speed, Luck, and Strength.
    Player = Beserker(PlayerName)
    skeletonEnemy = Skeleton('Skullz')
    skeletonEnemy2 = Skeleton('Skullz2')
    batEnemy = Cave_Bat('Batty')
    
    #Enemies get stronger each round. This variable stores the previous buffs plus the new buffs. 
    
    mySmallPotion = SmallHealthPotion()
    myLargePotion = LargeHealthPotion()
    Player.addToInventory(mySmallPotion)
    Player.addToInventory(myLargePotion)
    myEnemies = MultipleEnemy(skeletonEnemy, skeletonEnemy2, batEnemy)
    #interactionLogic2(Player, myEnemies)
    interactionLogic3(Player, myEnemies)
        

    while True:
        respawn = input('Would you like to continue down the dungeon(YES or NO): ').strip().upper()

        while respawn not in ['YES', 'NO']:
            print('ERROR: Not a valid choice!')
            respawn = input('Would you like to continue down the dungeon(YES or NO): ').strip().upper()
        
        if respawn == 'YES':
            interactionLogic3(Player, myEnemies)
        else:
            break




def interactionLogic2(Player, GameEnemy):
    x =True
    
    if not isinstance(Player, characterType):
        raise ValueError('Invalid player model!')
    for i in GameEnemy:
        if not isinstance(i, enemyType):
            print('NOPE!')
        else:
            print('Yea')
    while x == True:
        print('Im here right now')
        for i in GameEnemy:
            myChoice = Player.PlayerActionChoices(i)
            
            if (myChoice == True) and i.is_alive():
                
                if not i.is_alive():
                    print(f'{i.name} died!')
                    print(Player.Level_Up(i.experience))
                    continue
                
                
                elif not Player.is_alive():
                    print('You died!')
                    x = False
            
            
            elif myChoice == False:
                x = False
                break

def interactionLogic3(Player, GameEnemy):
    x =True
    
    if not isinstance(Player, characterType):
        raise ValueError('Invalid player model!')
    for i in GameEnemy:
        if not isinstance(i, enemyType):
            print('NOPE!')
        else:
            print('Yea')
    while not multipleEnemyIsAlive(GameEnemy):
            for i in GameEnemy:
                myChoice = Player.PlayerActionChoices(i)
                
                
                if (myChoice == True):
                    
                    if not i.is_alive():
                        print(f'{i.name} died!')
                        continue
                    
                    
                    elif not Player.is_alive():
                        print('You died!')
                        x = False
                    print(f'{i.name} is currently at {i.health}')

                
                
                else:

                    break
            if myChoice == False:
                break
            
                
            
    
     
def test():
    skeletonEnemy = Skeleton('Skullz',0)
    skeletonEnemy2 = Skeleton('Skullz2',0)
    batEnemy = Cave_Bat('Batty',0)
    
    #Enemies get stronger each round. This variable stores the previous buffs plus the new buffs. 
    

    myEnemies = MultipleEnemy(skeletonEnemy, skeletonEnemy2, batEnemy)
    print(multipleEnemyIsAlive(myEnemies))
gameStart()
