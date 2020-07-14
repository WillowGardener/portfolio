import random as r
import pygame
import math

#Here is all the pre-game setup stuff
pygame.init()
screen = pygame.display.set_mode((960,640))
background = pygame.image.load("grass background.png")

#The foundation of the ecosystem, pops up regularly and is eaten by varmints
class Grass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("grass.png")
        self.energy = 5

    def draw(self):
        screen.blit(self.img,(self.x,self.y))

#Base class for both varmints and predators
class Animal:
    def __init__(self,x,y):
        self.name = self.baby_name()
        self.age = 0
        self.pregnant = False
        self.sex = self.chromosomer()
        self.x = x
        self.y = y
        #the awareness attribute is how far away the animal can sense food, predators, and mates
        self.awareness = 25
        self.start_energy = 10
        self.energy = self.start_energy
        #metabolism is how quickly the animal burns through energy
        self.metabolism = 3
        self.speed = 3
        self.libido = r.randint(10,30)

    #names the animal
    def baby_name(self):
        prefix_list = ["Da","Ka","Sha","Ma","Gla","Tre","Ru","Ron","Tu","Sue","Fo","Jo","Jenni","Po","Minni","Deli","Aissa","Mai","Jeze","Ja","Sa","Diy","Ami","Sala","Oli","Dem","Li","Ev","Ah","Moha","Ahme","Kaja","Na","Jona","Regi","Sher","A","Sa","Ma","Ta","Shel","Wil","Rag","Ud","Uth","Aga","Ab","Dah","Bre"]
        suffix_list = ["ren","ron","ana","lyn","da","paul","ra","bu","bob","role","tana","nissa","aqua","ray","lah","tou","mouna","bel","din","ya","nata","ba","med","lith","a","vi","via","ver","than","nald","lock","sha","ley","son","nar","red","tha","dou","by","lia","ria","von","onna","doul","mad"]
        prefix = r.choice(prefix_list)
        suffix = r.choice(suffix_list)
        name = prefix+suffix
        return name

    #determines the sex of the animal
    def chromosomer(self):
        genitals = r.randint(1,2)
        if genitals == 1:
            sex = "female"
        elif genitals == 2:
            sex = "male"
        return sex

    #not used in the current version of the program; causes the animal to stop moving and stop being able to reproduce, but keeps the animal on the screen so that it can be eaten
    def die(self):
        self.sex = "none"
        self.speed = 0

    #gives a list of an animal's stats. This is mostly for testing right now
    def __repr__(self):
        return f"Name: {self.name}\nSex: {self.sex}\nAge: {self.age}\nEnergy: {self.energy}\nSpeed: {self.speed}\nAwareness: {self.awareness}\nParental Investment: {self.parental_investment}\nLibido:{self.libido}\nMetabolism: {self.metabolism}\nPregnant? {self.pregnant}\n"

    #draws the animal on the screen
    def draw(self):
        screen.blit(self.img,(self.x,self.y))

    def move(self):
        #moves the animal according to their randomly chosen path. Execute this once per loop
        self.x +=self.x_move
        self.y +=self.y_move
        #if the animal is starting to go off-screen, this makes them reverse direction and stay on screen
        if self.x > 936: 
            self.x_move*=-1
            self.x = 936
        elif self.x <24:
            self.x_move*=-1
            self.x = 24
        if self.y > 606: 
            self.y_move*=-1
            self.y =606
        elif self.y <24:
            self.y_move*=-1
            self.y = 24

    #determines how far away an object is from the animal
    def proximity(self,target):
        distance_x = abs(self.x - target.x)
        distance_y = abs(self.y-target.y)
        distance = math.sqrt(pow(distance_x,2)+pow(distance_y,2))
        #print(distance)
        return distance

    #determines whether a varmint is occupying the same space as an object
    def adjacent(self,target):
        distance = self.proximity(target)
        if distance < 16:
            return True
    
    def move_toward(self,target):
        #while self.x != target.x or self.y != target.y:
        if self.x >= target.x:
            self.x_move = -1 * self.speed
        elif self.x <= target.x:
            self.x_move = self.speed
        if self.y >= target.y:
            self.y_move = -1 * self.speed
        elif self.y <= target.y:
            self.y_move = self.speed

    def move_away(self,target):
        #instructs the animal to change its movement to go in the opposite direction of whatever the target is:
        if self.x >= target.x:
            self.x_move = self.speed
        elif self.x <= target.x:
            self.x_move = -1 * self.speed
        if self.y >= target.y:
            self.y_move = self.speed
        elif self.y <= target.y:
            self.y_move = -1 * self.speed

    def eat(self,a_list):
        for item in a_list:
            #looks at all the items in the list and checks how far away they are
            prox = self.proximity(item)
            #checks to see if that item is close enough to eat
            eat = self.adjacent(item)
            if eat == True:
                #if the item is close enough to eat, that item is deleted and removed from its list, and its energy is added to the animal's
                self.energy+=item.energy
                a_list.remove(item) 
                del item    
            elif prox < self.awareness:
                #if the item is not close enough to eat, the animal moves toward the item
                self.move_toward(item)

    def mate(self,species_list):
        #checks to see if the animal is a female of sexual maturity with enough energy to get pregnant. If she has a higher libido, she will mate even if she's hungry
        if self.sex == "female" and self.age >= 1 and self.energy >= (self.start_energy * self.libido/10):
            for v in species_list:
                #she checks all the members of her species and singles out the ones who are male, of sexual maturity, and have enough energy to provide
                if v.sex == "male" and v.age >= 1 and v.energy >= (self.start_energy * self.libido/10):
                    mateable = self.proximity(v)
                    if mateable < self.awareness:
                        #then she magically gets pregnant just by looking at him
                        self.pregnant = True
                        #depending on his degree of parental investment, a heritable trait, he will give some of his energy to her so she does not die in childbirth
                        v.energy -= (self.parental_investment * v.energy)
                        self.energy += (self.parental_investment * v.energy)
                        break

   
                        
                        

class Predator(Animal):
    def __init__(self,x,y, mom = None):
        super().__init__(x,y)
        self.img = pygame.image.load("fox.png")
        self.x_move = r.randint(-3,3)
        self.y_move = r.randint(-3,3)
        #when the animals are generated at the beginning of the simulation, they have no parents and get randomized traits. After that, their traits are inherited
        # from their mothers, with mutations that change traits by up to 25% 
        if mom == None:
            self.awareness = r.randint(50,100)
        else: 
            self.awareness = r.randint(int(mom.awareness*.75),int(mom.awareness*1.25))
        self.start_energy = 20
        self.energy = self.start_energy
        if mom == None:
            self.speed = r.randint(3,6)
        else:
            self.speed = r.randint(int(.75*mom.speed),int(1.25*mom.speed))
        self.metabolism = .5 + (self.speed/3) + (self.awareness/30)
        #parental investment determines how much food a dad gives to his mate after getting her pregnant
        if mom == None:
            self.parental_investment = (r.randint(5,50))/100
        else:
            investment = r.randint(int(.75*mom.parental_investment),int(1.25*mom.parental_investment))
            #I had to cap parental investment at 1, because otherwise varmints evolve to break the law of conservation of energy; the fathers will kill themselves
            #in order to give their mates more energy than they actually have. This results in bunny black holes.
            if investment > 1:
                investment = 1
            self.parental_investment = investment
        #animals with high libido will mate even when they might not have enough food to support children    
        if mom == None:
            self.libido = r.randint(10,30)
        else:
            self.libido = r.randint(int(.75*mom.libido),int(1.25*mom.libido))
        #animals with high greed will eat even when they're full
        if mom == None:
            self.greed = r.randint(1,4)
        else:
            self.greed = r.randint(int(.75 * mom.greed),int(1.25*mom.greed)) 

    def mate(self,species_list):
        if self.sex == "female" and self.age >= 1 and self.energy >= (self.start_energy * self.libido/10):
            for v in species_list:
                if v.sex == "male" and v.age >= 1:
                    mateable = self.proximity(v)
                    if mateable < self.awareness:
                        self.pregnant = True
                        self.pregnant = True
                        v.energy -= (self.parental_investment * v.energy)
                        self.energy += (self.parental_investment * v.energy)
                        break

       

class Varmint(Animal):
    def __init__(self,x,y, mom = None):
        super().__init__(x,y)
        self.img = pygame.image.load("rabbit.png")
        self.x_move = r.randint(-3,3)
        self.y_move = r.randint(-3,3)
        if mom == None:
            self.awareness = r.randint(40,80)
        else:
            self.awareness = r.randint(int(.75 * mom.awareness),int(1.25*mom.awareness))
        if mom == None:
            self.speed = r.randint(2,5)
        else:
            self.speed = r.randint(int(.75*mom.speed),int(1.25*mom.speed))  
        self.start_energy = 10
        self.energy = self.start_energy
        self.metabolism = .5 + (self.speed/3) + (self.awareness/30)
        if mom == None:
            self.parental_investment = (r.randint(5,50))/100
        else:
            investment = r.randint(int(.75*mom.parental_investment),int(1.25*mom.parental_investment))
            if investment > 1:
                investment = 1
            self.parental_investment = investment
        if mom == None:
            self.libido = r.randint(10,30)
        else:
            self.libido = r.randint(int(.75*mom.libido),int(1.25*mom.libido))
        if mom == None:
            self.greed = r.randint(1,4)
        else:
            self.greed = r.randint(int(.75 * mom.greed),int(1.25*mom.greed)) 

    

    


def main():
    #Setting a timer to go off every 4 seconds; each time the timer ticks, this will indicate 1 in-simulation year and will trigger various events
    NEW_YEAR = pygame.USEREVENT + 1
    pygame.time.set_timer(NEW_YEAR,4000)
    ENERGY_LOSS = pygame.USEREVENT + 2
    pygame.time.set_timer(ENERGY_LOSS,500)
    year_counter = 0

    #Creates a bunch of grass, varmints, and predators at random points
    varmint_list = []
    for i in range(80):
        varm = Varmint(r.randint(40,920),r.randint(40,600))
        varmint_list.append(varm)
    
    plant_list = []
    for i in range(60):
        plant = Grass(r.randint(40,920),r.randint(40,600))
        plant_list.append(plant)    

    predator_list = []
    for i in range(6):
        pred = Predator(r.randint(40,920),r.randint(40,600))
        predator_list.append(pred)

    running = True
    while running:
        #fills in the background image continuously
        
        screen.blit(background,(0,0))

        #All events go in this for loop
        for event in pygame.event.get():
            #Quits the simulation if the 'X' button in the top right corner is clicked
            if event.type == pygame.QUIT:
                running = False

            #Causes varmints and predators to lose some energy every .5 seconds, and if their energy is 0 or less, they die
            elif event.type == ENERGY_LOSS:
                for varm in varmint_list:
                    varm.energy -= varm.metabolism                    
                    if varm.energy <= 0:
                        varmint_list.remove(varm)
                        del varm
                for pred in predator_list:
                    pred.energy -= pred.metabolism
                    if pred.energy <= 0:
                        predator_list.remove(pred)
                        del pred

            #simulates 1 in-game year every 4 seconds            
            elif event.type == NEW_YEAR:
                year_counter+=1                
                print(f"Happy new year! {year_counter}")
                
                for varm in varmint_list:
                    #Ages varmints. In the current version, they do not die of old age                    
                    varm.age+=1
                    '''if varm.age >= 8:
                        varm.die()'''
                    
                    if varm.pregnant == True:                        
                        for n in range(r.randint(3,5)):
                            #creates a litter of 3-5 varmints which inherit some traits from their mother
                            baby_varm = Varmint(varm.x,varm.y,varm)
                            varmint_list.append(baby_varm)
                            #pregnancy is exhausting. The pregnant varmint loses energy and gives it to her children
                            varm.energy -= varm.start_energy
                        varm.pregnant = False
                for pred in predator_list:
                                       
                    pred.age+=1
                    '''if pred.age >= 10:
                        pred.die()'''
                    if pred.pregnant == True:
                        for n in range(1):
                            baby_pred = Predator(pred.x,pred.y,pred)
                            predator_list.append(baby_pred)
                            pred.energy -= pred.start_energy
                        pred.pregnant = False
                print(f"there are {len(varmint_list)} varmints and {len(predator_list)} predators")
                        
        #instructs varmints to eat and mate
        for varm in varmint_list:
            for pred in predator_list:
                danger = varm.proximity(pred)
                if danger < varm.awareness:
                    varm.move_away(pred)
            varm.mate(varmint_list)
            #a varmint with a higher greed attribute will eat even when they're full
            if varm.energy <= varm.start_energy * varm.greed:
                varm.eat(plant_list)
            
            
            #moves varmints according to their AI
            varm.move()

            #refreshes varmints in their new spot
            varm.draw()

        #same thing as above, but for predators eating varmints
        for pred in predator_list:
            pred.move()
            pred.mate(predator_list)
            if pred.energy <= pred.start_energy * pred.greed:            
                pred.eat(varmint_list)
            pred.draw()

        #refreshes the plant
        for plant in plant_list:
            plant.draw()
            
        #generates new plants    
        for n in range(1):
            plant = Grass(r.randint(40,920),r.randint(40,600))
            plant_list.append(plant)

        #updates the display to reflect the changes above
        pygame.display.update()

if __name__ == "__main__":
    main()