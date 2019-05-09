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
    frontera, nodosvisitados = inicializar("dfs", False, problem)

    #return recursivo(problem, frontera, nodosvisitados) #Descomentar esta linea y comentar la siguiente
    return iterativo(problem, frontera, nodosvisitados)
    #return ['West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'East', 'East', 'East', 'North', 'North', 'North', 'North', 'North', 'North', 'North', 'East', 'East', 'South', 'South', 'South', 'South', 'South', 'South', 'East', 'East', 'North', 'North', 'North', 'North', 'North', 'North', 'East', 'East', 'South', 'South', 'South', 'South', 'East', 'East', 'North', 'North', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'South', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West']

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    frontera,nodosvisitados = inicializar("bfs", False, problem)

    return recursivo(problem, frontera, nodosvisitados)
    #return iterativo(problem, frontera, nodosvisitados) #Descomentar esta linea y comentar la anterior

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontera, nodosvisitados = inicializar("ucs", True, problem)

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
    frontera, nodosvisitados = inicializar("astar", True, problem)

    while not frontera.isEmpty():
        actual = frontera.pop()
        if problem.isGoalState(actual[0]):
            return actual[1]
        if actual[0] not in nodosvisitados:
            nodosvisitados.add(actual[0])
            for sucesor in problem.getSuccessors(actual[0]):
                if sucesor[0] not in nodosvisitados:
                    costo = actual[2] + sucesor[2]
                    costoTotal = costo + heuristic(sucesor[0], problem)
                    frontera.push((sucesor[0], actual[1] + [sucesor[1]], costo), costoTotal)

    return None


#Metodos auxiliares

"""
Este metodo se encarga de inicializar las estructuras necesarias y agregar el primer nodo a la frontera
para resolver el ejercicio.
Si es ucs o astar se instancia una cola con prioridad
Si es bfs se instancia una cola comun
Si es dfs se instancia una pila

#Devuelve
Conjunto con nodosvisitados inicializado
Pila, Cola, Cola prioridad segun corresponda con la frontera y el primer nodo insertado
"""
def inicializar(searchmethod, tienecosto, problem):
    nodosvisitados = set()
    ini = problem.getStartState()
    frontera = util.PriorityQueue() if searchmethod == "ucs" or searchmethod == "astar" else util.Queue() if searchmethod == "bfs" else util.Stack()

    if tienecosto:
        frontera.push((ini, [], 0), 0)
    else:
        frontera.push((ini, []))

    return frontera,nodosvisitados

"""
Agrega a la frontera los sucesores del elemento actual siempre y cuando no hayan sido visitados.
No valido para las busquedas que incorporen costos.
"""
def addSuccessors(sucesores,frontera, nodosvisitados, actual):
    for sucesor in sucesores:
        if not sucesor[0] in nodosvisitados:
            frontera.push((sucesor[0], actual[1] + [sucesor[1]]))

"""
Resuelve de manera recursiva los metodos de busqueda dfs o bfs
"""
def recursivo(problem, frontera, nodosvisitados):
    # defino los casos bases
    if frontera.isEmpty():
        return None

    actual = frontera.pop()
    if problem.isGoalState(actual[0]):
        return actual[1]
    # caso recursivo, tengo que seguir buscando
    nodosvisitados.add(actual[0])
    sucesores = problem.getSuccessors(actual[0]) #lista de sucesores
    addSuccessors(sucesores,frontera, nodosvisitados, actual)
    return recursivo(problem, frontera, nodosvisitados)

"""
Resuelve de manera iterativa los metodos de busqueda dfs o bfs
"""
def iterativo(problem, frontera, nodosvisitados):
    while not frontera.isEmpty():
        actual = frontera.pop()
        nodosvisitados.add(actual[0])
        if problem.isGoalState(actual[0]):
            return actual[1]
        sucesores = problem.getSuccessors(actual[0])
        addSuccessors(sucesores, frontera, nodosvisitados, actual)

    return None

"""Comandos que se pueden utilizar

py pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar #Usa la nullHeuristic definida en este archivo
py pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
py pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic

py pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
py pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
py pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

Osea...los mapas son tinyMaze, mediumMaze y bigMaze, este ultimo se le agrega el parametro -z que es zoom
ya que el tamaño normal no entra en una pantalla normal.
Dentro de estos mapas funcionan todos estos metodos de busqueda
"""
# Abbreviations11
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

