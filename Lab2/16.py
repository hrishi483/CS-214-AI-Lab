import copy 
import time
from sys import argv


def make_dict(state):
    dict={}
    for i in range(3):
        for j in range(len(state[i])):
            dict[state[i][j]]=tuple([i,j])
    return dict

def heuiristic1(curr_dict, goal_dict):
    h=0
#This function assigns values as +1 if present correct place else -1 
    for key,value in curr_dict.items():
        # print(key ,'->',value)
        coordinate_initial=value        
        coordinate_goal=goal_dict[key]
        if(coordinate_initial[0]==coordinate_goal[0] and coordinate_initial[1]==coordinate_goal[1]):
            h=h+1
        else:
            h=h-1
        # print(coordinate_initial,'->',coordinate_goal)
    return h
def heuristic2(curr_dict, goal_dict):
    h=0
    for key,value in curr_dict.items():
        # print(key ,'->',value)
        coordinate_initial=value        
        coordinate_goal=goal_dict[key]
        if(coordinate_initial[0]==coordinate_goal[0] and coordinate_initial[1]==coordinate_goal[1]):
            h=h+coordinate_initial[1]
        else:
            h=h-coordinate_initial[1]
        # print(coordinate_initial,'->',coordinate_goal)
    return h

#h=manhattan distance from the inital and goal state    
def heuristic3(curr_dict,goal_dict):
    h_val=0
    for keys , values in curr_dict.items():
        cur_coordinates = values
        goal_coordinates = goal_dict[keys]

        h_val=h_val-abs(cur_coordinates[0]-goal_coordinates[0])-abs(cur_coordinates[1]-goal_coordinates[1])

    return h_val


#**********************************MOVE GEN STARTS HERE********************************
#***********Working 80% sure********************************
def move_gen(curr_state,goal_dict,h):
    best_heuristic=h
    best_state=curr_state
#Pickup the block from top of any stack and place it on top of the remaining stacks to obtain new states
    succesors=[]
    for i in range(3):
        newState = curr_state.copy()
        
#Look out for empty List to avoid errors        
        if len(newState[i])>0:
            newState = copy.deepcopy(curr_state)
            top=newState[i].pop()
                
#To avoid placing the block in the same stack use if else
#make dict and try to store the state somewhere so that if 
            if i!=0:                   
                new_new_State = copy.deepcopy(newState)
                new_new_State[0].append(top)
                new_dict={}
                new_dict=make_dict(new_new_State)
                # print(new_new_State,heuristic2(new_dict,goal_dict))               
                curr_h=heuristic2(new_dict,goal_dict)
                if(curr_h>best_heuristic):
                    best_state=new_new_State
                    best_heuristic=curr_h
            if i!=1:
                new_new_State = copy.deepcopy(newState)
            
                new_new_State[1].append(top)     
                # new_new_State[1].append(top)
                new_dict={}
                new_dict=make_dict(new_new_State)
                # print(new_new_State,heuristic2(new_dict,goal_dict))
                curr_h=heuristic2(new_dict,goal_dict)
                if(curr_h>best_heuristic):
                    best_state=new_new_State
                    best_heuristic=curr_h

            if i!=2:
                new_new_State = copy.deepcopy(newState) 
                new_new_State[2].append(top)    
                # new_new_State[2].append(top)
                new_dict={}
                new_dict=make_dict(new_new_State)
                # print(new_new_State,heuristic2(new_dict,goal_dict))
                curr_h=heuristic2(new_dict,goal_dict)
                if(curr_h>best_heuristic):
                    best_state=new_new_State
                    best_heuristic=curr_h

    return best_state             


#**************************Driver Code for Hill Climbing Starts here************************
def Hill_Climbing(initial_state,goal_state,heuristic):
    start_timer=time.time()
    total_cost=0
    inital_dict=make_dict(initial_state)
    goal_dict=make_dict(goal_state)
    goal_heuristic=heuristic(goal_dict,goal_dict)
    curr_state=initial_state

#Loop till goal state is reached or local maxima is reached
    while True:
        curr_dict=make_dict(curr_state)
#Check if the goal state is acheived
        curr_heuristic=heuristic(curr_dict,goal_dict)
        if(heuristic(curr_dict,goal_dict)==goal_heuristic):
            print("START: ",initial_state)
            print("Goal Reached")
            print("GOAL:",goal_state)
            print("TOTAL COST: ",total_cost)
            end_timer=time.time()
            print("Time Taken: ",end_timer-start_timer)
            return curr_state

#else look for the successor states
        else:
            successor_state=move_gen(curr_state,goal_dict,curr_heuristic)
            total_cost+=1
            print(successor_state,heuristic(make_dict(successor_state),goal_dict))
            successor_dict=make_dict(successor_state)
# if the successor state is worst than the current state hill climbing will fail
            if(curr_heuristic>=heuristic(successor_dict,goal_dict)):
                end_timer=time.time()
                print("Time Taken: ",end_timer-start_timer)
                print ("Not possible to reach to goal state")
                return
#if the successor state is better than the current state make the successor state as current state 
            else:
                curr_state=successor_state


#*************Main Method of code begins********************************
if __name__ == '__main__':
    inital_state2=[['E','B','F'],
              ['D','A','C'],
              []]
    
    goal_state2=[['A','D','B'],
              ['E','F','C'],
              []]

    start_file = argv[1]

  
    with open (start_file, 'r') as fp:
        a = fp.readlines()

    inital_state = []
    for i in a:
        i = i.strip()
        inital_state.append(i.split(" "))

    goal_file = argv[2]


    with open (goal_file, 'r') as fp:
        b = fp.readlines()

    goal_state = []
    for i in b:
        i = i.strip()
        goal_state.append(i.split(" "))
        
    for i, val  in enumerate(goal_state):
        if val == [""]:
            goal_state[i] = []

    for i, val  in enumerate(inital_state):
        if val == [""]:
            inital_state[i] = []

 

    print("Start State :",inital_state2)
    print("Goal State:",goal_state2)
    print("Start")
    Hill_Climbing(inital_state2,goal_state2,heuiristic1)
    print("*"*150)
    Hill_Climbing(inital_state2,goal_state2,heuristic2)
    print("*"*150)
    Hill_Climbing(inital_state2,goal_state2,heuristic3)
    print("*"*150)
    

    
