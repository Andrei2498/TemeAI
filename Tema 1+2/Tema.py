import random
import math
import time

states = []
bkt_solution = 0
iddfs_solution = 0
a_star_solution = 0
random_times = []
backtracking_times = []
iddfs_times = []
random_length_of_result = []
backtracking_length_of_result = []
iddfs_length_of_result = []
a_star_times = []
a_star_length_of_result = []
algorithm_type = 0
infinite = 10000


class State:

    def __init__(self, boat_capacity, number_of_missionary_left, number_of_cannibals_left, boat_position,
                 number_of_missionary_right, number_of_cannibals_right):
        self.boat_capacity = boat_capacity
        self.number_of_missionary_left = number_of_missionary_left
        self.number_of_cannibals_left = number_of_cannibals_left
        self.boat_position = boat_position
        self.number_of_missionary_right = number_of_missionary_right
        self.number_of_cannibals_right = number_of_cannibals_right

    def __str__(self):
        return 'State(boat_capacity=' + str(self.boat_capacity) \
               + ', number_of_missionary_left=' + str(self.number_of_missionary_left) \
               + ', number_of_cannibals_left=' + str(self.number_of_cannibals_left) \
               + ', boat_position=' + str(self.boat_position) \
               + ', number_of_missionary_right=' + str(self.number_of_missionary_right) \
               + ', number_of_cannibals_right=' + str(self.number_of_cannibals_right) + ')'

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        if self.number_of_missionary_left == other.number_of_missionary_left \
                and self.number_of_missionary_right == other.number_of_missionary_right \
                and self.number_of_cannibals_left == other.number_of_cannibals_left \
                and self.number_of_cannibals_right == other.number_of_cannibals_right \
                and self.boat_position == other.boat_position \
                and self.boat_capacity == other.boat_capacity:
            return True
        return False

    def see_object(self):
        return self.__str__()


def make_random_state():
    cannibals = random.randint(3, 13)
    missionaries = random.randint(cannibals + 2, 15)
    if cannibals < 5:
        boat_capacity = 3
    elif 5 <= cannibals < 10:
        boat_capacity = 4
    else:
        boat_capacity = 5
    return boat_capacity, missionaries, cannibals


def average_list(list1):
    return sum(list1) / len(list1)


def is_final_state(state):
    if state.number_of_missionary_left + state.number_of_cannibals_left == 0 and state.boat_position == 2:
        return True
    else:
        return False


def transition_to_right(state, missionary_moved, cannibal_moved):
    if validation(state, missionary_moved, cannibal_moved):
        return State(state.boat_capacity, state.number_of_missionary_left - missionary_moved,
                     state.number_of_cannibals_left - cannibal_moved, 3 - state.boat_position,
                     state.number_of_missionary_right + missionary_moved,
                     state.number_of_cannibals_right + cannibal_moved)


def transition_to_left(state, missionary_moved, cannibal_moved):
    if validation(state, -missionary_moved, -cannibal_moved):
        return State(state.boat_capacity, state.number_of_missionary_left + missionary_moved,
                     state.number_of_cannibals_left + cannibal_moved, 3 - state.boat_position,
                     state.number_of_missionary_right - missionary_moved,
                     state.number_of_cannibals_right - cannibal_moved)


def validation(state, missionary_moved, cannibal_moved):
    new_state = State(state.boat_capacity, state.number_of_missionary_left - missionary_moved,
                      state.number_of_cannibals_left - cannibal_moved, 3 - state.boat_position,
                      state.number_of_missionary_right + missionary_moved,
                      state.number_of_cannibals_right + cannibal_moved)
    if 0 < new_state.number_of_missionary_left < new_state.number_of_cannibals_left:
        return False
    elif 0 < new_state.number_of_missionary_right < new_state.number_of_cannibals_right:
        return False
    elif missionary_moved + cannibal_moved > new_state.boat_capacity:
        return False
    elif algorithm_type == 0 and states.count(new_state) > 2:
        return False
    elif algorithm_type == 0 and new_state.number_of_cannibals_right-new_state.number_of_missionary_right > new_state.boat_capacity:
        return False
    return True


def is_valid_state(state):
    if state.number_of_cannibals_right < 0 \
            or state.number_of_cannibals_left < 0 \
            or state.number_of_missionary_right < 0 \
            or state.number_of_missionary_left < 0:
        return False
    if 0 < state.number_of_missionary_left < state.number_of_cannibals_left:
        return False
    elif 0 < state.number_of_missionary_right < state.number_of_cannibals_right:
        return False
    return True


def random_algorithm(b, missionary_moved, cannibal_moved, state):
    if state.number_of_cannibals_left + state.number_of_missionary_left < b and state.boat_position == 1:
        number_of_people_in_boat = random.randint(1, state.number_of_missionary_left + state.number_of_cannibals_left)
    elif state.boat_position == 2 and state.number_of_missionary_right > state.number_of_cannibals_right:
        number_of_people_in_boat = 1
    elif state.boat_position == 2 and state.number_of_missionary_right == state.number_of_cannibals_right:
        number_of_people_in_boat = random.randint(1, 2)
    elif state.boat_position == 2 and state.number_of_missionary_right < state.number_of_cannibals_right:
        number_of_people_in_boat = 1
        # number_of_people_in_boat = random.randint(1, state.number_of_cannibals_right + state.number_of_missionary_right)
    else:
        number_of_people_in_boat = random.randint(1, b)
    while number_of_people_in_boat > 0:
        new_person_in_boat = random.randint(1, 2)
        if new_person_in_boat == 1 and state.boat_position == 1 and state.number_of_missionary_left > missionary_moved:
            missionary_moved += 1
            number_of_people_in_boat -= 1
        elif new_person_in_boat == 1 and state.boat_position == 2 and state.number_of_missionary_right > missionary_moved:
            missionary_moved += 1
            number_of_people_in_boat -= 1
        elif new_person_in_boat == 2 and state.boat_position == 1 and state.number_of_cannibals_left > cannibal_moved:
            cannibal_moved += 1
            number_of_people_in_boat -= 1
        elif new_person_in_boat == 2 and state.boat_position == 2 and state.number_of_cannibals_right > cannibal_moved:
            cannibal_moved += 1
            number_of_people_in_boat -= 1
    if missionary_moved == 0:
        return str(0) + str(cannibal_moved)
    elif cannibal_moved == 0:
        return str(missionary_moved) + str(cannibal_moved)
    else:
        return str(missionary_moved) + str(cannibal_moved)


def strategy_random(state, count):
    states.clear()
    while not is_final_state(state) and count <= 100:
        count = count + 1
        missionary_moved = 0
        cannibal_moved = 0
        string = random_algorithm(state.boat_capacity, missionary_moved, cannibal_moved, state)
        missionary_moved = int(string[0])
        cannibal_moved = int(string[1])
        if state.boat_position == 1:
            aux = transition_to_right(state, missionary_moved, cannibal_moved)
            if aux is not None:
                states.append(aux)
                state = aux
        else:
            aux = transition_to_left(state, missionary_moved, cannibal_moved)
            if aux is not None:
                states.append(aux)
                state = aux
    else:
        if count > 100:
            reset(state)


def reset(state):
    states.clear()
    strategy_random(state, 0)


def new_generator(current_state, number_of_people):
    numbers = [(i, j) for i in range(0, number_of_people + 1) for j in range(0, number_of_people + 1) if i + j == number_of_people]
    state_list = []
    if number_of_people == 1:
        if current_state.boat_position == 1:
            return [State(current_state.boat_capacity, current_state.number_of_missionary_left - 1,
                          current_state.number_of_cannibals_left,
                          3 - current_state.boat_position, current_state.number_of_missionary_right + 1,
                          current_state.number_of_cannibals_right),
                    State(current_state.boat_capacity, current_state.number_of_missionary_left,
                          current_state.number_of_cannibals_left - 1,
                          3 - current_state.boat_position, current_state.number_of_missionary_right,
                          current_state.number_of_cannibals_right + 1)]
        elif current_state.boat_position == 2:
            return [State(current_state.boat_capacity, current_state.number_of_missionary_left + 1,
                          current_state.number_of_cannibals_left,
                          3 - current_state.boat_position, current_state.number_of_missionary_right - 1,
                          current_state.number_of_cannibals_right),
                    State(current_state.boat_capacity, current_state.number_of_missionary_left,
                          current_state.number_of_cannibals_left + 1,
                          3 - current_state.boat_position, current_state.number_of_missionary_right,
                          current_state.number_of_cannibals_right - 1)]
    if current_state.boat_position == 1:
        for item in numbers:
            state_list.append(State(current_state.boat_capacity, current_state.number_of_missionary_left - item[0], current_state.number_of_cannibals_left - item[1],
                                    3 - current_state.boat_position, current_state.number_of_missionary_right + item[0], current_state.number_of_cannibals_right + item[1]))
    elif current_state.boat_position == 2:
        for item in numbers:
            state_list.append(State(current_state.boat_capacity, current_state.number_of_missionary_left + item[0], current_state.number_of_cannibals_left + item[1],
                                    3 - current_state.boat_position, current_state.number_of_missionary_right - item[0], current_state.number_of_cannibals_right - item[1]))
    for it in state_list:
        if not is_valid_state(it):
            state_list.remove(it)
    return state_list


def strategy_backtracking(state):
    solution = [state]
    states.clear()
    k_list = [0]
    while not is_final_state(solution[-1]):
        if k_list[-1] >= state.boat_capacity:
            solution.pop(-1)
            k_list.pop(-1)
        if not is_final_state(solution[-1]) and k_list[-1] < state.boat_capacity:
            k_list[-1] += 1
            aux = new_generator(solution[-1], k_list[-1])
            if len(aux) >= 1:
                for it in aux:
                    states.append(it)
                    if solution[-1].boat_position == 1 and it not in solution and is_valid_state(it) and not is_final_state(solution[-1]):
                        if validation(it, solution[-1].number_of_missionary_left - it.number_of_missionary_left, solution[-1].number_of_cannibals_left - it.number_of_cannibals_left) and it.boat_position == 3 - solution[-1].boat_position:
                            solution.append(it)
                            k_list.append(0)
                            break
                    elif solution[-1].boat_position == 2 and it not in solution and is_valid_state(it) and not is_final_state(solution[-1]):
                        if validation(it, solution[-1].number_of_missionary_right - it.number_of_missionary_right, solution[-1].number_of_cannibals_right - it.number_of_cannibals_right) and it.boat_position == 3 - solution[-1].boat_position:
                            solution.append(it)
                            k_list.append(0)
    global bkt_solution
    bkt_solution = len(solution)


def generate_all(current_state, boat_capacity):
    result = []
    aux = []
    for i in range(1, boat_capacity + 1):
        aux = new_generator(current_state, i)
        for j in aux:
            result.append(j)
    return result


def strategy_iddfs(state):
    dfs_stack = [state]
    current_depth = 0
    correct_stack = [state]
    number_of_states_per_lvl = [1]

    while not is_final_state(correct_stack[-1]):
        number = 0
        if current_depth % 2 == 0:
            if correct_stack[-1].number_of_missionary_left + correct_stack[-1].number_of_cannibals_left < state.boat_capacity:
                for i in generate_all(dfs_stack[-1], correct_stack[-1].number_of_missionary_left + correct_stack[-1].number_of_cannibals_left):
                    if is_valid_state(i) and i not in correct_stack:
                        dfs_stack = dfs_stack + [i]
                        number += 1
            else:
                for i in generate_all(dfs_stack[-1], state.boat_capacity):
                    if is_valid_state(i) and i not in correct_stack:
                        dfs_stack = dfs_stack + [i]
                        number += 1
                current_depth += 1
        elif current_depth % 2 == 1:
            for i in generate_all(dfs_stack[-1], 1):
                if is_valid_state(i) and i not in correct_stack:
                    dfs_stack = dfs_stack + [i]
                    number += 1
            current_depth += 1
        number_of_states_per_lvl.append(number)
        if current_depth % 2 == 0:
            while not validation(correct_stack[-1], -dfs_stack[-1].number_of_missionary_left+correct_stack[-1].number_of_missionary_left, -dfs_stack[-1].number_of_cannibals_left + correct_stack[-1].number_of_cannibals_left):
                dfs_stack.pop()
                number_of_states_per_lvl[-1] -= 1
        else:
            while not validation(correct_stack[-1], dfs_stack[-1].number_of_missionary_right-correct_stack[-1].number_of_missionary_right, dfs_stack[-1].number_of_cannibals_right - correct_stack[-1].number_of_cannibals_right):
                dfs_stack.pop()
                number_of_states_per_lvl[-1] -= 1
        if number_of_states_per_lvl[-1] == 0:
            number_of_states_per_lvl.pop()
            current_depth -= 1
            correct_stack.pop()
            dfs_stack.pop()
        # print(len(dfs_stack))
        correct_stack = correct_stack + [dfs_stack[-1]]
    global iddfs_solution
    iddfs_solution = len(correct_stack)


def sort_by_cost(item_list):
    new_list = []
    for i in item_list:
        new_list = new_list + [(i, heuristic(i))]
    new_list.sort(key=lambda x: x[1])
    for i in range(0, len(new_list)):
        item_list[i] = new_list[i][0]
    return item_list


def strategy_a_star(state):
    dfs_stack = [state]
    current_depth = 0
    correct_stack = [state]
    number_of_states_per_lvl = [1]
    while not is_final_state(correct_stack[-1]):
        number = 0
        if current_depth % 2 == 0:
            if correct_stack[-1].number_of_missionary_left + correct_stack[-1].number_of_cannibals_left < state.boat_capacity:
                for i in reversed(sort_by_cost(generate_all(dfs_stack[-1], correct_stack[-1].number_of_missionary_left + correct_stack[-1].number_of_cannibals_left))):
                    if is_valid_state(i):
                        dfs_stack = dfs_stack + [i]
                        number += 1
            else:
                for i in reversed(sort_by_cost(generate_all(dfs_stack[-1], state.boat_capacity))):
                    if is_valid_state(i) and i not in correct_stack:
                        dfs_stack = dfs_stack + [i]
                        number += 1
                current_depth += 1
        elif current_depth % 2 == 1:
            for i in reversed(sort_by_cost(generate_all(dfs_stack[-1], 1))):
                if is_valid_state(i) and i not in correct_stack:
                    dfs_stack = dfs_stack + [i]
                    number += 1
            current_depth += 1
        number_of_states_per_lvl.append(number)
        if current_depth % 2 == 0:
            while not validation(correct_stack[-1], -dfs_stack[-1].number_of_missionary_left+correct_stack[-1].number_of_missionary_left, -dfs_stack[-1].number_of_cannibals_left + correct_stack[-1].number_of_cannibals_left):
                dfs_stack.pop()
                number_of_states_per_lvl[-1] -= 1
        else:
            while not validation(correct_stack[-1], dfs_stack[-1].number_of_missionary_right-correct_stack[-1].number_of_missionary_right, dfs_stack[-1].number_of_cannibals_right - correct_stack[-1].number_of_cannibals_right):
                dfs_stack.pop()
                number_of_states_per_lvl[-1] -= 1
        if number_of_states_per_lvl[-1] == 0:
            number_of_states_per_lvl.pop()
            current_depth -= 1
            correct_stack.pop()
            dfs_stack.pop()
        correct_stack = correct_stack + [dfs_stack[-1]]
    global a_star_solution
    a_star_solution = len(correct_stack)


def heuristic(state):
    now_sum = state.number_of_missionary_left + state.number_of_cannibals_left
    if now_sum % state.boat_capacity == 0:
        result = (now_sum/state.boat_capacity) * 2
    else:
        result = (now_sum/state.boat_capacity) * 2 + 1
    return result + infinite

"""
    bp = 1 -> left
    bp = 2 -> right
"""
if __name__ == "__main__":
    counting = 0
    while counting < 10:
        values = make_random_state()

        start_state = State(values[0], values[1], values[2], 1, 0, 0)
        initial_state = start_state

        start_time = time.time()
        states.append(start_state)
        strategy_random(start_state, 0)
        random_times.append(time.time()-start_time)
        random_length_of_result.append(len(states))

        start_time = time.time()
        strategy_backtracking(start_state)
        backtracking_times.append(time.time()-start_time)
        backtracking_length_of_result.append(bkt_solution)

        start_time = time.time()
        strategy_iddfs(start_state)
        iddfs_times.append(time.time()-start_time)
        iddfs_length_of_result.append(iddfs_solution)

        start_time = time.time()
        strategy_a_star(start_state)
        a_star_times.append(time.time()-start_time)
        a_star_length_of_result.append(a_star_solution)

        counting += 1

    print("Random results: ", end="")
    print(average_list(random_times), average_list(random_length_of_result))
    print("Backtracking results: ", end="")
    print(average_list(backtracking_times), average_list(backtracking_length_of_result))
    print("Iddfs results: ", end="")
    print(average_list(iddfs_times), average_list(iddfs_length_of_result))
    print("A* results: ", end="")
    print(average_list(a_star_times), average_list(a_star_length_of_result))
    # strategy_random(State(5, 15, 14, 1, 0, 0), 0)
    # strategy_backtracking(State(5, 14, 13, 1, 0, 0))
    # strategy_iddfs(State(5, 15, 14, 1, 0, 0))
    # strategy_a_star(State(5, 15, 14, 1, 0, 0))
