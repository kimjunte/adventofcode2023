def get_game_info(game_line, game_info):
    game_number,turns = game_line.split(":")[0], game_line.split(":")[1]
    min_block = {}

    for turn in turns.split(";"):
        for block in turn.split(","):
            num, color = block.split(" ")[1], block.split(" ")[2]
            if color in min_block:
                min_block.update({color: max([min_block[color], int(num)])})
            else:
                min_block.update ({color: int(num)})
    game_number = int(game_number.split(" ")[1])

    game_info.update({game_number: min_block})
    return game_info

def is_game_possible(r_limit,g_limit,b_limit, game_value):
    """
    return true or false if game is possible

    game_line_info looks like: {1: {'red': 12, 'blue': 10, 'green': 10}}

    return game number if true else return false
    """
    if game_value["red"] <= r_limit and game_value["blue"] <= b_limit and game_value["green"] <= g_limit:
        return True
    else:
        return False

def validate(a, b):
    assert a == b, f"a: {a}, b: {b}"
    return a == b

def test():
    # Problem 2
    validate(get_game_info("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", {}), {1: {'blue': 6, 'red': 4, 'green': 2}})
    validate(get_game_info("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", {}), {2: {'blue': 4, 'red': 1, 'green': 3}})
    validate(get_game_info("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", {}), {3: {'blue': 6, 'red': 20, 'green': 13}})
    validate(get_game_info("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", {}), {4: {'blue': 15, 'red': 14, 'green': 3}})
    validate(get_game_info("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", {}), {5: {'blue': 2, 'red': 6, 'green': 3}})

    validate(is_game_possible(0, 0, 0, {"red": 1, "blue": 1, "green": 1}), False)
    validate(is_game_possible(2, 2, 2, {"red": 1, "blue": 1, "green": 1}), True)
    validate(is_game_possible(2, 2, 2, {"red": 4, "blue": 4, "green": 4}), False)
    validate(is_game_possible(1, 1, 1, {"red": 1, "blue": 1, "green": 1}), True)
    return None

def main():
    game_info = {}
    with open("input.txt", "r") as magicalElfFile:
        for line in magicalElfFile.readlines():
            striped_line = line.strip()
            get_game_info(striped_line, game_info)

    sum = 0 
    power = 0

    for game_number, game_values in game_info.items():
        if is_game_possible(12, 13, 14, game_values):
            sum = sum + game_number
        power = power + (game_values["red"] * game_values["green"] * game_values["blue"]) 

    print(f"Total sum of all game possible is {sum}")
    print(f"The power of all games added together is {power}")
            


if __name__ == "__main__":
    test()
    main()
