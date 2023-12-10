numbers_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    file = open("../input.txt", "r")
    # file = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    # file = [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen",
    # ]
    response = 0
    for line in file:
        numbers = []
        for i, letter in enumerate(line):
            if letter.isdigit():
                numbers.append(letter)
            for key, value in numbers_dict.items():
                if line[i:].startswith(key):
                    numbers.append(value)
        elf_coordinates = f"{numbers[0]}{numbers[-1]}"
        response += int(elf_coordinates)
    return response


if __name__ == "__main__":
    print(main())
