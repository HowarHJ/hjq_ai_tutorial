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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
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
    history = set()  # 记录被查询过的状态
    node_fringe = util.Stack()  # 栈
    node_fringe.push((problem.getStartState(), []))  # 将初始状态和空动作压入栈中
    while node_fringe.isEmpty() is not True:
        node = node_fringe.pop()
        state = node[0]
        action = node[1]
        if problem.isGoalState(state) is True:
            return action  # 若是目标状态，返回对应动作
        if state not in history:
            history.add(state)
            successor = problem.getSuccessors(state)
            for s in successor:
                up_action = action + [s[1]]  # 更新路径动作
                node_fringe.push((s[0], up_action))  # 将后继状态和对应的动作压入栈中
    return action


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    history = set()
    node_fringe = util.Queue()
    node_fringe.push((problem.getStartState(), []))
    while node_fringe.isEmpty() is not True:
        node = node_fringe.pop()
        state = node[0]
        action = node[1]
        if problem.isGoalState(state) is True:
            return action
        if state not in history:
            history.add(state)
            successor = problem.getSuccessors(state)
            for s in successor:
                up_action = action + [s[1]]
                node_fringe.push((s[0], up_action))
    return action


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    history = set()
    node_fringe = util.PriorityQueue()
    node_fringe.push((problem.getStartState(), [], 0), 0)
    while node_fringe.isEmpty() is not True:
        node = node_fringe.pop()
        state = node[0]
        action = node[1]
        cost = node[2]
        if problem.isGoalState(state) is True:
            return action
        if state not in history:
            history.add(state)
            successor = problem.getSuccessors(state)
            for s in successor:
                up_action = action + [s[1]]
                up_cost = cost + s[2]
                node_fringe.push((s[0], up_action, up_cost), up_cost)
    return action


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    history = set()
    node_fringe = util.PriorityQueue()
    node_fringe.push((problem.getStartState(), [], 0),
                     heuristic(problem.getStartState(), problem))
    while node_fringe.isEmpty() is not True:
        node = node_fringe.pop()
        state = node[0]
        action = node[1]
        cost = node[2]
        if problem.isGoalState(state) is True:
            return action
        if state not in history:
            history.add(state)
            successor = problem.getSuccessors(state)
            for s in successor:
                up_action = action + [s[1]]
                up_cost = cost + s[2]
                node_fringe.push((s[0], up_action, up_cost),
                                 up_cost + heuristic(s[0], problem))
    return action


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
