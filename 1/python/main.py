def main():
    file = open("../input.txt", "r")
    # file = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    response = 0
    for line in file:
        line_split = "".join(filter(lambda i:i.isdigit(), line))
        elf_coordinates = f"{line_split[0]}{line_split[-1]}"
        response += int(elf_coordinates)
    return response


if __name__ == "__main__":
    print(main())
