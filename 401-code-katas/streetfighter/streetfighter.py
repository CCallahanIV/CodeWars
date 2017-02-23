"""Solution for https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python"""


def street_fighter_selection(fighters, initial_position, moves):
    """Given initial fighters, position, and moves list return all selected fighters."""
    selected = []
    curr_pos = list(initial_position)
    for move in moves:
        if move == "up":
            if curr_pos[0] != 0:
                curr_pos[0] -= 1
        elif move == "left":
            if curr_pos[1] != 0:
                curr_pos[1] -= 1
            else:
                curr_pos[1] = len(fighters[0]) - 1
        elif move == "right":
            if curr_pos[1] != len(fighters[0]) - 1:
                curr_pos[1] += 1
            else:
                curr_pos[1] = 0
        else:
            if curr_pos[0] != len(fighters) - 1:
                curr_pos[0] += 1
        selected.append(fighters[curr_pos[0]][curr_pos[1]])
    return selected
