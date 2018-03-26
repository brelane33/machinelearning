# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
from collections import namedtuple
from game import Directions
from game import Configuration
from game import Agent
from game import Actions
from pacman import GameState

node = namedtuple("node", "state, parent, action, pathCost")

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
  return  [s,s,w,s,w,w,s,w]


def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

  Use the 'node' data type defined at the beginning. As an example, the root node can be created 
  like so: root = node(problem.getStartState(), None, None, 0), where the parent node and the action 
  that led to the root node are both 'None', meaning nil.
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  #"*** YOUR CODE HERE ***"
  #util.raiseNotDefined()


  goalPath = []

  stackOpen = util.Stack()
  stackClosed = util.Stack()
  pathStack = util.Queue()

  loopcounter = 0

  root = node(problem.getStartState(), None, None, 0)

  stackOpen.push(root)

  successor = []

  while(not stackOpen.isEmpty()):
    loopcounter = loopcounter + 1
    
    child = stackOpen.pop()

    print "child direction:", child[2], "iteration: ", loopcounter


    if problem.isGoalState(child[0]):
      print "victory!"
      while(child[1] != None):
        pathStack.push(child[2])
        child = child[1]
      print pathStack.list
      return pathStack.list
      

    successor = (problem.getSuccessors(child[0]))

    tempstuff = []

    for i in successor:
      tempstuff.append(node(i[0], child, i[1], i[2]))

    stackClosed.push(child[0])

    for i in tempstuff:
      if(i.state not in stackOpen.list and i.state not in stackClosed.list):
        stackOpen.push(i)

    print "Length open: ", len(stackOpen.list)
    print "Length closed: ", len(stackClosed.list)

    print "children (begin while): ", tempstuff, "iteration: ", loopcounter
    #print "open (begin while): ", stackOpen.list, "iteration: ", loopcounter
    #print "closed (begin while): ", stackClosed.list, "iteration: ", loopcounter


    print "Children: ", child
  

def breadthFirstSearch(problem):
  """Search the shallowest nodes in the search tree first. [p 81]"""
  #*** YOUR CODE HERE ***"
  goalPath = []

  stackOpen = util.Queue()
  stackClosed = util.Queue()
  pathStack = util.Queue()

  loopcounter = 0

  root = node(problem.getStartState(), None, None, 0)

  stackOpen.push(root)

  successor = []

  while(not stackOpen.isEmpty()):
    loopcounter = loopcounter + 1
    
    child = stackOpen.pop()

    print "child 2 direction:", child[2], "iteration: ", loopcounter


    if problem.isGoalState(child[0]):
      print "victory!"
      while(child[1] != None):
        pathStack.push(child[2])
        child = child[1]
      print pathStack.list
      return pathStack.list
      

    successor = (problem.getSuccessors(child[0]))

    tempstuff = []

    for i in successor:
      tempstuff.append(node(i[0], child, i[1], i[2]))

    stackClosed.push(child[0])

    for i in tempstuff:
      if(i.state not in stackOpen.list and i.state not in stackClosed.list):
        stackOpen.push(i)
      
def uniformCostSearch(problem):
  #"Search the node of least total cost first. "
  #"*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

#def aStarSearch(problem, heuristic=util.manhattanDistance)
def aStarSearch(problem, heuristic=nullHeuristic):
#"Search the node that has the lowest combined cost and heuristic first.""

  loopcounter = 0

  queueOpen = util.PriorityQueue()
  pathqueue = util.Queue()

  root = node(problem.getStartState(), None, None, 0)

  #print "heuristic: ", heuristic(root, problem)
  queueOpen.push(root, heuristic(root.state, problem))

  successor = []
  tempstuff = []
  visited = []

  while(not queueOpen.isEmpty()):
    loopcounter = loopcounter + 1

    child = queueOpen.pop()

    successors = []
    goodstuff = []

    if problem.isGoalState(child[0]):
      print "victory!"
      print "our children: ", child
      print "our neighbors: ", visited
      while(child[1] != None):
        pathqueue.push(child[2])
        child = child[1]
      print pathqueue.list
      return pathqueue.list

    successors = problem.getSuccessors(child[0])

    if child[0] not in visited:
      visited.append(child[0])

    for i in successors:
      temp = [i][0]
      tempLoc = temp[0]
      tempDir = temp[1]
      tempCost = temp[2]
    
      goodstuff.append(node(tempLoc, child, tempDir, tempCost))

    for i in goodstuff:
      if(i.state not in visited):
        queueOpen.push(i, heuristic(i.state, problem))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
