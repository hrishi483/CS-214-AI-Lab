# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions


    directions = {}
    st = util.Stack()
#Stores the ACTIONS taken to reach the goal state from the start state
    path = []

    # get root node and add to fringe
    root = problem.getStartState()
    st = util.Stack()
#Stack contains the current,action and parent of the current
    st.push((root, 'start',None ))
    # while nodes still exist on fringe
    while not st.isEmpty():
        front = st.pop()

#check if the front of the stack is the goal state and if it is then backtack till we reachthe start state again
        if problem.isGoalState(front[0]):
            while front[1] != 'start':
                path.append(front[1])
                front = directions[front[2]]   #get the parent
            #Since we are backtracking we need to store the actions from the goal to start but return in start to goal format
            return list(reversed(path))
        else:
#else if the state is not start state then we explore the children of the nodes
            for succ in problem.getSuccessors(front[0]):
            #before pushing into the stack check if the node already existes to avoid repetation
                if succ[0] not in directions:
                    st.push((succ[0], succ[1],front[0] )) #Push (child,actions,parent)

                directions[front[0]] = front     #Store the parent of the nodes

    return None


    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start=problem.getStartState()
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    if (problem.isGoalState(start)):
        return []
    goal=None

    q=util.Queue()
    q.push(start)
    visited=[]
    actions=[]
    direction={}
    visited.append(start)
    path = {}
    path[start]=None

    if not problem.isGoalState(start):
     while not q.isEmpty():
            front=q.pop()
            visited.append(front)
            if(problem.isGoalState(front)):
                goal=front
                break
            else:
                for j in problem.getSuccessors(front):
                    if(j[0] not in visited):
                        q.push(j[0])
                        direction[j[0]]=j[1]
                        visited.append(j[0])
                        path[j[0]] = front
    node=goal
    while node:
        if node:
            curr_action=direction.get(node)

            actions.append(curr_action)
        node=path[node]
    #TO remove the null action stored for starting we are deleting the last element and returning the remaining
    del actions[-1]

    return list(reversed(actions))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    print "Hi"
#code for UCS starts
    start = problem.getStartState()
    open=util.PriorityQueue()
    closed=[]
    path=[]
    parent={} #child:parent
    actions={} #node:action
    open.push(start,0)
    goal=start





    while not open.isEmpty():
        node,parent_cost=open.pop()
        if problem.isGoalState(node):
            goal=node

            print "Hi"
            closed.append(node)
            print "Type of node",type(node)

        else:
            Successors=[]
            Successors=problem.getSuccessors(node)
            for succ in Successors:
                print
                "Type of succ", type(succ[0])
                print
                "Type of closed", type(closed[0])
                if (succ[0] not in closed):

                    succ_cost=parent_cost+succ[2]
                    parent[succ[0]]=node
                    actions[succ[0]]=succ[2]
                    open.push(succ[0],succ_cost)



    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
