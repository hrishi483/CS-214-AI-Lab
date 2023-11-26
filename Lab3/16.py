import random
import time
import sys

def select_next_city(current_city,unvisited,pheromone,DisbetCities,alpha,beta):
    ph_level=pheromone[current_city]
    distance_level=DisbetCities[current_city][0]

    probablity=[]
#Calculate the probability
    for city in unvisited:
        probablity.append((ph_level[city]**alpha)*
        ((1/DisbetCities[current_city][city])**beta))
#Calculate the cummulative Probablity
    ProbSet=[]
    for x in probablity:
        ProbSet.append(x/sum(probablity))
#Selection of next city based on roulette wheel 
    nextCity=random.choices(unvisited,weights=ProbSet,k=1) 
    return nextCity[0]           




def update_pheromone(tour,pheromone,DisbetCity,Q):
    distance=0
    for i in range(len(tour)):
        distance+=DisbetCity[tour[i]][tour[(i+1)%len(tour)]]
    for i in range(len(tour)):
        pheromone[tour[i]][tour[(i+1)%len(tour)]]+=Q/distance



#Q is the evaporation rate
def evaporate_pheromone(pheromone,rho):
    for i in range(len(pheromone)):
        for j in range(len(pheromone)):
            pheromone[i][j]=(1-rho)*pheromone[i][j]


def calculate_cost(tour,DistbetCity):
    cost=0
    for i in range(len(tour)):
        cost+=DistbetCity[tour[i]][tour[(i+1)%len(tour)]]  #To calculate cost the lenght of tour distance between 
                                                       #one city to next one.for last city to the first one cyclic
    return cost

def antColony(Total_cities,DistbetCity,iterations,alpha,beta,rho,q):
    best_tour=[]
    best_tour=range(Total_cities)
    stop=begin-time.time()
    # iterations=200
    pheromone=[]
#initialize the pheromone levels for the cities as 0
    for i in range(Total_cities):
        temp=[]
        for j in range(Total_cities):
            temp.append(0.1)
        pheromone.append(temp)
#initially the bst costs is infinity 
    best_cost=float('INF')

#For each ant get the tour by selecting the first city randomly and the next one by roulette wheel         
    while stop<290:        
        for y in range(iterations):  #num_ants=Total_cities
            
            tour=[]
            unvisited=[]
            for i in range(0,Total_cities):
                unvisited.append(i)
            start=random.randint(0,Total_cities-1)
            unvisited.remove(start)
            tour.append(start)

            current_city=start
            for pl in range(0,Total_cities-1):
                next_city=select_next_city(current_city,unvisited,pheromone,DistbetCity,alpha,beta)
                unvisited.remove(next_city)
                tour.append(next_city)
                current_city=next_city
            tour_cost=calculate_cost(tour,DistbetCity)
            if tour_cost<best_cost:
                best_tour=tour
                best_cost=tour_cost
       
#Evaporate the pheromone on the paths        
        evaporate_pheromone(pheromone,rho)
#update the pheromone            
        update_pheromone(tour,pheromone,DistbetCity,q)
#check if the solution is better else do again        
        print(best_cost)
        best_tour.append(best_tour[0])
        print(best_tour)
        print("-"*100)
    return best_cost


if __name__ == '__main__':

    begin=time.time()
    given_data = open(sys.argv[1], "r")
    data = given_data.readlines()
    eucCheck = False
    print(data[0])
    if(data[0] == "euclidean"):
        eucCheck = 1

    CityCoordinates = []
    Total_cities=int(data[1])
    DistbetCity = []

    for i in range(Total_cities):
        c=[]
        for x in data[i+2].strip().split(' '):
            c.append(float(x))
        CityCoordinates.append(c)
        temp=[]
        for dist in data[Total_cities+2+i].strip().split(' '):
            temp.append(float(dist))
        DistbetCity.append(temp)

    # print(eucCheck)
    print(data[1])
    if eucCheck == True:
        if(int(data[1])==100):
            print(antColony(Total_cities,DistbetCity,900,9,9, 0.5, 10))
        elif(int(data[1])==250):
            print(antColony(Total_cities,DistbetCity,200,9,9, 0.5, 10))
        elif(int(data[1])==500):
            print(antColony(Total_cities,DistbetCity,500,9,9, 0.5, 10))
    else:
        if(int(data[1])==100):
            print(antColony(Total_cities,DistbetCity,850,20,20, 0.1, 10))
        elif(int(data[1])==250):
            print(antColony(Total_cities,DistbetCity,180,20,20, 0.1, 10))
        elif(int(data[1])==500):
            print(antColony(Total_cities,DistbetCity,32,15,15, 0.1, 8))
    