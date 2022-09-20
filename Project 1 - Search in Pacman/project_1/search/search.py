# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    closedSet = set()  # History - states I've already visited

    # Create a dictionary to hold current state and path to get to it from the start
    current = {
        'state': problem.getStartState(),
        'path': []
    }
    openList = util.Stack()  # States that we know about that we can go next. Depth First Search has a stack as its
    # open list
    openList.push(current) # Push the initial state onto the open list

    # print("Start:", problem.getStartState())
    while not openList.isEmpty(): # Check that open list is not empty
        current = openList.pop()
        if problem.isGoalState(current['state']): # Check to see if we are at the goal
            return current['path'] # Return the path to the goal state
        closedSet.add(current['state']) # Add current state to the visited set
        potSuccessors = problem.getSuccessors(current['state']) # Get the list of successors
        # print("Current successors:", potSuccessors)
        for successor in potSuccessors: # Iterate through successors to check if they have been visited before
            # print(successor)
            # print(successor[0])
            # print(closedList)
            if successor[0] not in closedSet:
                # Push onto open list if not explored yet
                openList.push({
                    'state': successor[0],
                    'path': current['path'] + [successor[1]]
                        })


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    closedSet = set()  # History - states I've already visited

    # Create a dictionary to hold current state and path to get to it from the start
    current = {
        'state': problem.getStartState(),
        'path': []
    }
    openList = util.Queue()  # States that we know about that we can go next. Breadth First Search has a Queue as its
    # open list
    openList.push(current)  # Push the initial state onto the open list

    # print("Start:", problem.getStartState())
    while not openList.isEmpty():  # Check that open list is not empty
        current = openList.pop()
        if current['state'] not in closedSet:
            closedSet.add(current['state'])  # Add current state to the visited set
            if problem.isGoalState(current['state']):  # Check to see if we are at the goal
                return current['path']  # Return the path to the goal state
            potSuccessors = problem.getSuccessors(current['state'])  # Get the list of successors
            # print("Current successors:", potSuccessors)
            for successor in potSuccessors:  # Iterate through successors to check if they have been visited before
                # print(successor)
                # print(successor[0])
                # print(closedList)
                if successor[0] not in closedSet:
                    # Push onto open list if not explored yet
                    openList.push({
                        'state': successor[0],
                        'path': current['path'] + [successor[1]]
                    })



def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """

    closedSet = set()  # History - states I've already visited

    # Create a dictionary to hold current state and path to get to it from the start
    current = {
        'state': problem.getStartState(),
        'path': [],
        'cost': 0
    }
    openList = util.PriorityQueue()  # States that we know about that we can go next. Uniform Cost Search has a
    # Priority Queue as the open list
    openList.push(current, problem.getCostOfActions(current['path']))  # Push the initial state onto the open list,
    # and the initial cost = 0

    # print("Start:", problem.getStartState())
    while not openList.isEmpty():  # Check that open list is not empty
        current = openList.pop()
        if (current['state'] not in closedSet):
            closedSet.add(current['state'])  # Add current state to the visited set
            if problem.isGoalState(current['state']):  # Check to see if we are at the goal
                return current['path']  # Return the path to the goal state
            potSuccessors = problem.getSuccessors(current['state'])  # Get the list of successors
            # print("Current successors:", potSuccessors)
            for successor in potSuccessors:  # Iterate through successors to check if they have been visited before
                # print(successor)
                # print(successor[0])
                # print(closedList)
                if successor[0] not in closedSet:
                    # Push onto open list if not explored yet
                    openList.push({
                        'state': successor[0],
                        'path': current['path'] + [successor[1]],
                        'cost': current['cost'] + successor[2]
                    }, current['cost'] + successor[2])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """

    closedSet = set()  # History - states I've already visited

    # Create a dictionary to hold current state and path to get to it from the start
    current = {
        'state': problem.getStartState(),
        'path': [],
        'cost': 0
    }
    openList = util.PriorityQueue();  # States that we know about that we can go next. A* Search has a
    # Priority Queue as the open list
    openList.push(current, 0)  # Push the initial state onto the open list, and the initial f = 0

    # print("Start:", problem.getStartState())
    while not openList.isEmpty():  # Check that open list is not empty
        current = openList.pop()
        if (current['state'] not in closedSet):
            closedSet.add(current['state'])  # Add current state to the visited set
            if problem.isGoalState(current['state']):  # Check to see if we are at the goal
                return current['path']  # Return the path to the goal state
            potSuccessors = problem.getSuccessors(current['state'])  # Get the list of successors
            # print("Current successors:", potSuccessors)
            for successor in potSuccessors:  # Iterate through successors to check if they have been visited before
                # print(successor)
                # print(successor[0])
                # print(closedList)
                if successor[0] not in closedSet:
                    # Push onto open list if not explored yet
                    g = problem.getCostOfActions(current['path'] + [successor[1]]) # Cost to get to successor
                    h = heuristic(successor[0], problem) # Heuristic: Estimated cost to get to final distance
                    f = g + h # Value to determine priority of state
                    openList.push({
                        'state': successor[0],
                        'path': current['path'] + [successor[1]],
                        'cost': g
                    }, f)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

