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
from util import *
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


    motherNode = [problem.getStartState(), 0, 0, 0, 0, 0]
    frontier = Stack()
    frontier.push(motherNode)
    explored = []
    stackList = []
    stackList.append(motherNode[0])
    pathList = []
    visited = 0
    while 1==1:
        if frontier.isEmpty():
            return 'Failure'
        node = frontier.pop()
        stackList.append(node[0])
        explored.append(node)

        if problem.isGoalState(node[0]):
            explored = explored[:: -1]
            while node != motherNode:
                pathList.append(node[1])
                for element in explored:
                    if element[0] == node[3] :
                        pathList.append(element[1])
                        node = element
                        explored.remove(element)

            pathList = pathList[:: -1]
            pathList.remove(0)
            return pathList
        for childNodes in problem.getSuccessors(node[0]):
            child = [childNodes[0], childNodes[1], childNodes[2], node[0],node[1],node[2]]
            if child[0] in stackList:
                visited+=1

            if child not in explored and child[0]!=node[3] and visited<2 :
                frontier.push(child)
                explored.append(child)
                stackList.append(child[0])
        visited = 0
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    frontier = Queue()
    explored = [] # nodes to create path
    visited = 0
    pathList = []
    checkerList = [] # states
    if problem.isGoalState(problem.getStartState()):
        return []
    motherNode = [problem.getStartState(), 0, 0, []]
    frontier.push(motherNode)
    while not frontier.isEmpty():
        node = frontier.pop()

        if problem.isGoalState(node[0]):
            explored.append(node)
            explored = explored[:: -1]
            while node != motherNode:
                pathList.append(node[1])
                for element in explored:
                    if element[0] == node[3][0]:
                        pathList.append(element[1])
                        node = element
            pathList = pathList[:: -1]
            pathList.remove(0)
            return pathList

        explored.append(node)
        checkerList.append(node[0])

        for childNodes in problem.getSuccessors(node[0]):
            child = [childNodes[0], childNodes[1], childNodes[2]]
            child.append(node)

            if child[0] in checkerList:
                visited=1

            if visited == 0:
                frontier.push(child)
                checkerList.append(child[0])

            visited=0

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""


    frontier = PriorityQueue()
    explored = [] # nodes to create path
    visited = 0
    pathList = []
    checkerList = [] # states
    allCosts = {}
    check2 = []
    explored2 = []

    if problem.isGoalState(problem.getStartState()):
        return []
    motherNode = [problem.getStartState(), 0, 0, []]
    frontier.push(motherNode,0)
    while not frontier.isEmpty():

        node = frontier.pop()

        if problem.isGoalState(node[0]):
            explored.append(node)
            explored = explored[:: -1]
            while node != motherNode:
                pathList.append(node[1])
                for element in explored:
                    if element[0] == node[3][0]:
                        pathList.append(element[1])
                        node = element
            pathList = pathList[:: -1]
            pathList.remove(0)
            return pathList

        explored.append(node)
        explored2.append(node[0])
        checkerList.append(node[0])

        for childNodes in problem.getSuccessors(node[0]):
            cost = childNodes[2]+node[2]
            child = [childNodes[0], childNodes[1], cost]
            child.append(node)


            if child[0] in checkerList:
                visited=1

            if child[0] not in explored2:
                if child[0] not in check2:
                    frontier.push(child,child[2])
                    check2.append(child[0])
                    allCosts[child[0]] = child[2]
                    checkerList.append(child[0])
                elif allCosts[child[0]] > child[2]:
                    for x in explored:
                        if x[0] == child[0]:
                            x = child
                    frontier.push(child, child[3][2] + childNodes[2])
                    allCosts[child[0]] = child[2]

            visited=0

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

    def pqFunc(node):
        return node[2] + heuristic(node[0], problem)


    frontier = PriorityQueueWithFunction(pqFunc)
    explored = [] # nodes to create path
    visited = 0
    pathList = []
    checkerList = [] # states
    allCosts = {}
    check2 = []
    explored2 = []

    if problem.isGoalState(problem.getStartState()):
        return []
    motherNode = [problem.getStartState(), 0, 0, []]
    frontier.push(motherNode)
    while not frontier.isEmpty():

        node = frontier.pop()

        if problem.isGoalState(node[0]):
            explored.append(node)
            explored = explored[:: -1]
            while node != motherNode:
                pathList.append(node[1])
                for element in explored:
                    if element[0] == node[3][0]:
                        pathList.append(element[1])
                        node = element
            pathList = pathList[:: -1]
            pathList.remove(0)
            return pathList

        explored.append(node)
        explored2.append(node[0])
        checkerList.append(node[0])

        for childNodes in problem.getSuccessors(node[0]):
            cost = childNodes[2]+node[2]
            child = [childNodes[0], childNodes[1], cost]
            child.append(node)


            if child[0] in checkerList:
                visited=1

            if child[0] not in explored2:
                if child[0] not in check2:
                    frontier.push(child)
                    check2.append(child[0])
                    allCosts[child[0]] = child[2]
                    checkerList.append(child[0])
                elif allCosts[child[0]] > child[2]:
                    for x in explored:
                        if x[0] == child[0]:
                            x = child
                    frontier.push(child)
                    allCosts[child[0]] = child[2]

            visited=0


    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
