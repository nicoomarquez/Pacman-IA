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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    frontera = util.Stack()
    # Just location, like [7, 7]
    ini = problem.getStartState()
    # (location, path)
    nodoini = (ini, [])
    frontera.push(nodoini)
    nodosvisitados = set()
    nodosvisitados.add(ini)
    while not frontera.isEmpty():
        # node[0] is location, while node[1] is path
        actual = frontera.pop()

        if problem.isGoalState(actual[0]):
            return actual[1]
        sucesores = problem.getSuccessors(actual[0])
        for sucesor in sucesores:
            if not sucesor[0] in nodosvisitados:
                frontera.push((sucesor[0], actual[1] + [sucesor[1]]))
                nodosvisitados.add(actual[0])

    return None


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    frontera = util.Queue()
    ini = problem.getStartState()
    nodoini = (ini, [])
    frontera.push(nodoini)
    nodosvisitados = set()
    nodosvisitados.add(ini)

    while not frontera.isEmpty():
        actual = frontera.pop() #la posicion 0 tiene la ubicacion y en la pos 1 el camino

        if problem.isGoalState(actual[0]):
            return actual[1]
        sucesores = problem.getSuccessors(actual[0])
        for sucesor in sucesores:
            if not sucesor[0] in nodosvisitados:
                frontera.push((sucesor[0], actual[1] + [sucesor[1]]))
                nodosvisitados.add(actual[0])

    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    frontera = util.PriorityQueue()
    ini = problem.getStartState()
    nodoini = (ini, [], 0)
    frontera.push(nodoini, 0)
    nodosvisitados = set()

    while not frontera.isEmpty():
        actual = frontera.pop()
        if problem.isGoalState(actual[0]):
            return actual[1]
        if actual[0] not in nodosvisitados:
            nodosvisitados.add(actual[0])
            for sucesor in problem.getSuccessors(actual[0]):
                if sucesor[0] not in nodosvisitados:
                    costo = actual[2] + sucesor[2]
                    frontera.push((sucesor[0], actual[1] + [sucesor[1]], costo), costo)

    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontera = util.PriorityQueue()
    resultados = util.PriorityQueue()
    ini = problem.getStartState()
    nodoini = (ini, [], 0)
    frontera.push(nodoini, 0)
    nodosvisitados = set()
    #nodosvisitados.add(ini)

    while not frontera.isEmpty():
        actual = frontera.pop()
        if problem.isGoalState(actual[0]):
           #print("Resultado: Nodo = "+str(actual[0])+"\n Mov = "+str(actual[1]) + "\n Costo= "+str(actual[2]))
           #resultados.push((actual[0],actual[1]),actual[2])
            return actual[1]
        else:
            if actual[0] not in nodosvisitados:
                nodosvisitados.add(actual[0])
                print("Sucesores de "+str(actual[0])+" con pos: "+str(actual[1])+" = "+str(problem.getSuccessors(actual[0])))

                for sucesor in problem.getSuccessors(actual[0]):
                    if sucesor[0] not in nodosvisitados:
                        costo = actual[2] + sucesor[2]
                        print(str(problem.getCostOfActions(actual[1])))
                        print("\n\n\n")
                        #print("costo = "+str(actual[2])+" + "+str(sucesor[2]) +" = " + str(costo))
                        costoTotal = costo + heuristic(sucesor[0], problem)
                        #print("Costo tot = "+str(costoTotal))
                        frontera.push((sucesor[0], actual[1] + [sucesor[1]], costo), costoTotal)
                        #print("agregando a la frontera: "+str(actual[1]))
    return None
    """print("\n\n")         
    if(resultados.isEmpty()):
        print("No hay nada")"""

    
   """ mejorResultado=resultados.pop()
    tupla=mejorResultado[0]
    print("El mejor costo: "+str() + "con tupla ( "+str(tupla[0])+" + " + str(tupla[1]) +" )")
    return mejorResultado[1]"""

def astarBackTracking(problem,resultados,candidatos,visitados):
    if problem.isGoalState(candidatos[1]):
        resultados.push(candidatos)
    else:
        if candidatos
    return resultados

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
