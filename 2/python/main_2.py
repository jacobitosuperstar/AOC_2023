cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def main():
    # file = open("../test_input.txt", "r")
    file = open("../input.txt", "r")
    possible_games = 0
    for i,line in enumerate(file):
        line = line.strip()
        _, games = line.split(":")
        game_results = games.split(";")
        game_results = ",".join(game_results)
        rolls = game_results.split(",")
        roll_dict = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for roll in rolls:
            roll = roll.strip()
            roll_components = roll.split(" ")
            if roll_dict[roll_components[-1]] < int(roll_components[0]):
                roll_dict[roll_components[-1]] = int(roll_components[0])
        value = roll_dict["red"]*roll_dict["green"]*roll_dict["blue"]
        print(value)
        possible_games += value
    return possible_games


if __name__ == "__main__":
    print(main())
