# reinforcement_q_learning.py - REINFORCEMENT learning: a robot learns to reach the goal
# No extra libraries needed.
#
# World: 5 cells in a row.   [0] [1] [2] [3] [4=GOAL]
# Actions: 0 = move left, 1 = move right
# Reward: +10 for reaching the goal, -1 for every other step (so shorter is better)

import random

random.seed(1)
N_STATES = 5
GOAL = 4
ACTIONS = [0, 1]                      # left, right

# Q-table: how good each action is in each state (starts at 0)
q_table = [[0.0, 0.0] for _ in range(N_STATES)]

learning_rate = 0.5     # how much new experience changes old knowledge
discount = 0.9          # how much future rewards matter
explore_chance = 0.3    # sometimes try a random action to discover new things


def take_step(state, action):
    """The environment: returns the next state and the reward."""
    next_state = max(0, state - 1) if action == 0 else min(GOAL, state + 1)
    reward = 10 if next_state == GOAL else -1
    return next_state, reward


# Training: play 50 short games (episodes)
for episode in range(50):
    state = 0
    while state != GOAL:
        # choose an action: explore (random) or exploit (best known)
        if random.random() < explore_chance:
            action = random.choice(ACTIONS)
        else:
            action = 0 if q_table[state][0] > q_table[state][1] else 1

        next_state, reward = take_step(state, action)

        # Q-learning update rule
        best_future = max(q_table[next_state])
        old_value = q_table[state][action]
        q_table[state][action] = old_value + learning_rate * (
            reward + discount * best_future - old_value)

        state = next_state

# Show what the agent learned
print("State | Q(left) | Q(right) | Best action")
for state in range(GOAL):
    left, right = q_table[state]
    best = "right" if right > left else "left"
    print(f"  {state}   | {left:7.2f} | {right:8.2f} | {best}")
