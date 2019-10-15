import random
import math

states = []
algorithm_type = 0


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


def initialize():
    print("Initialize state...")
    state = State(3, 3, 3, 1, 0, 0)
    return state


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
    elif algorithm_type == 0 and new_state in states:
        return False
    return True


def is_valid_state(state):
    if state.number_of_cannibals_right < 0 \
            or state.number_of_cannibals_left < 0 \
            or state.number_of_missionary_right < 0 \
            or state.number_of_missionary_left < 0:
        return False
    return True


def random_algorithm(b, missionary_moved, cannibal_moved, state):
    if state.number_of_cannibals_left + state.number_of_missionary_left < b and state.boat_position == 1:
        number_of_people_in_boat = random.randint(1, state.number_of_missionary_left + state.number_of_cannibals_left)
    elif state.number_of_missionary_right + state.number_of_cannibals_right < b and state.boat_position == 2:
        number_of_people_in_boat = random.randint(1, state.number_of_cannibals_right + state.number_of_missionary_right)
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
            reset()


def reset():
    restart = initialize()
    states.clear()
    strategy_random(restart, 0)


def generate_solution(state, number_people):
    result = []
    canibal = 0
    misionar = number_people
    while len(result) <= math.ceil(number_people / 2) + (1 - number_people % 2):
        result.append(State(state.boat_capacity,
                            state.number_of_missionary_left + int(math.pow(-1, state.boat_position) * misionar),
                            state.number_of_cannibals_left + int(math.pow(-1, state.boat_position) * canibal),
                            3 - state.boat_position,
                            state.number_of_missionary_right - int(math.pow(-1, state.boat_position) * misionar),
                            state.number_of_cannibals_right - int(math.pow(-1, state.boat_position) * canibal)))

        result.append(State(state.boat_capacity,
                            state.number_of_missionary_left + int(math.pow(-1, state.boat_position) * canibal),
                            state.number_of_cannibals_left + int(math.pow(-1, state.boat_position) * misionar),
                            3 - state.boat_position,
                            state.number_of_missionary_right - int(math.pow(-1, state.boat_position) * canibal),
                            state.number_of_cannibals_right - int(math.pow(-1, state.boat_position) * misionar)))
        canibal += 1
        misionar -= 1
    if number_people % 2 == 0:
        result.pop(len(result) - 1)

    return result


def strategy_backtracking(state):
    solution = [state]
    k_list = [0]
    while not is_final_state(solution[len(solution) - 1]):
        if k_list[len(k_list) - 1] > state.boat_capacity:
            solution.pop(len(solution) - 1)
            k_list.pop(len(k_list) - 1)
        if not is_final_state(solution[len(solution) - 1]):
            k_list[len(k_list) - 1] += 1
            aux = generate_solution(solution[len(solution) - 1], k_list[len(k_list) - 1])
            for it in aux:
                if ((validation(it,solution[len(solution) - 1].number_of_missionary_left - it.number_of_missionary_left,solution[len( solution) - 1].number_of_cannibals_left - it.number_of_cannibals_left) and it.boat_position == 2) or (validation(it, solution[len(solution) - 1].number_of_missionary_right - it.number_of_missionary_right, solution[len(solution) - 1].number_of_cannibals_right - it.number_of_cannibals_right) and it.boat_position == 1)) and it not in solution and is_valid_state( it):
                    solution.append(it)
                    k_list.append(0)
                    break
    for i in solution:
        print(i.see_object())


"""
    bp = 1 -> left
    bp = 2 -> right
"""
if __name__ == "__main__":
    print("Start....")
    start_state = initialize()
    # strategy_random(start_state, 0)
    strategy_backtracking(start_state)
