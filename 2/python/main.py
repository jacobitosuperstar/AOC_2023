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
        possible_games += i+1
        line = line.strip()
        _, games = line.split(":")
        game_results = games.split(";")
        game_results = ",".join(game_results)
        rolls = game_results.split(",")
        for roll in rolls:
            roll = roll.strip()
            roll_components = roll.split(" ")
            if cubes[roll_components[-1]] < int(roll_components[0]):
                possible_games -= i+1
                break
    return possible_games


if __name__ == "__main__":
    print(main())
