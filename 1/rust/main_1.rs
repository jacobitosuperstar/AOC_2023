use std::fs;
use std::collections::HashMap;
use std::iter::FromIterator;

fn main() {
    let file = fs::read_to_string("../input.txt")
    //let file = fs::read_to_string("../input_2.txt")
        .expect("Failed to load file.");

    let file_lines = file.lines(); // Iterator over "\n" in the lines

    // // creating a hashmap to store the values of the string and the numbers
    // let mut numbers_map: HashMap<&str, &str> = HashMap::new();

    // // storing the values of the strings into the hashmap
    // numbers_map.insert("one", "1");
    // numbers_map.insert("two", "2");
    // numbers_map.insert("three", "3");
    // numbers_map.insert("four", "4");
    // numbers_map.insert("five", "5");
    // numbers_map.insert("six", "6");
    // numbers_map.insert("seven", "7");
    // numbers_map.insert("eight", "8");
    // numbers_map.insert("nine", "9");

    let numbers_map: HashMap<&str, &str> = HashMap::from_iter([
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]);

    let mut response = 0;

    for line in file_lines {
        let mut numbers: Vec<char> = Vec::new(); // Creating a vector of chars

        for (i,letter) in line.chars().enumerate() {
            if char::is_digit(letter, 10) {
                numbers.push(letter);
            }

            for (key, value) in &numbers_map {
                let moving_line = &line[i..]; // with this I move around the string
                if moving_line.starts_with(key) {
                    numbers.push(value.chars().next().unwrap());
                }
            }

        }
        let elf_coordinates_vector = [numbers.first().unwrap(), numbers.last().unwrap()];
        let elf_coordinates = String::from_iter(elf_coordinates_vector)
            .parse::<i32>()
            .unwrap();
        // println!("{:?}", elf_coordinates);
        response += elf_coordinates;
    }
    println!("{}", response);
}
