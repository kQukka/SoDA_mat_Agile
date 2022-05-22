IDX_ACTION_LEFT = 0
IDX_ACTION_DOWN = 1
IDX_ACTION_RIGHT = 2
IDX_ACTION_UP = 3
IDX_ACTION = (IDX_ACTION_LEFT, IDX_ACTION_DOWN, IDX_ACTION_RIGHT, IDX_ACTION_UP)

INITIAL_ACTION_UP = 'U'
INITIAL_ACTION_DOWN = 'D'
INITIAL_ACTION_RIGHT = 'R'
INITIAL_ACTION_LEFT = 'L'
INITIAL_ACTION = (INITIAL_ACTION_LEFT, INITIAL_ACTION_DOWN, INITIAL_ACTION_RIGHT, INITIAL_ACTION_UP)

STR_ACTION_UP = 'Up'
STR_ACTION_DOWN = 'Down'
STR_ACTION_RIGHT = 'Right'
STR_ACTION_LEFT = 'Left'
STR_ACTION = (STR_ACTION_LEFT, STR_ACTION_DOWN, STR_ACTION_RIGHT, STR_ACTION_UP)

INITIAL_ENV_START = 'S'
INITIAL_ENV_GOAL = 'G'
INITIAL_ENV_FLOOR = 'F'
INITIAL_ENV_OBSTACLE = 'H'


ID_GRID_FLOOR = 0
ID_GRID_FLOOR_CURRENT = 1
ID_GRID_FLOOR_PASSED = 2

ID_GRID_ITEM_EMPTY = 10
ID_GRID_ITEM_EXIST = 11
ID_GRID_ITEM_TAKEN = 11

ID_GRID_OBSTACLE = 88
ID_GRID_START = 66
ID_GRID_GOAL = 99

# reward
# REWARD_NONE = 0
# REWARD_NOT_MOVE = -10
# REWARD_MOVE = 1
# REWARD_OBSTACLE = -10
# REWARD_OUT_GIRD = -10
# REWARD_RETURN = -10
# REWARD_GOAL = 10

# step result
ID_NOT_MOVE = 0
ID_GENERAL_MOVE = 1
ID_OBSTACLE = 2
ID_OUT_GRID = 3
ID_RETURN = 4
ID_GOAL = 5
STR_RESULT = ('ID_NOT_MOVE', 'ID_GENERAL_MOVE', 'ID_OBSTACLE', 'ID_OUT_GRID', 'ID_RETURN', 'ID_GOAL')


# reward
class REWARD:
    def __init__(self):
        self.NONE = 0
        self.NOT_MOVE = -10
        self.MOVE = 0
        self.OBSTACLE = -10
        self.OUT_GIRD = -10
        self.RETURN = -10
        self.GOAL = 10
        self.NAME = ['NONE', 'NOT_MOVE', 'MOVE', 'OBSTACLE', 'OUT_GIRD', 'RETURN', 'GOAL']


