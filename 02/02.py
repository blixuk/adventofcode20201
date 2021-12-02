#!/usr/bin/env python
# file: adventofcode2020/02/02.py
# author: blixuk
# Day 2: Dive: Part 2
# Answer: 

class Submarine:

    def __init__(self, course:list) -> None:
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.move(self.plot(course))

    def plot(self, data:list) -> list:
        return [tuple(course.split()) for course in data]

    def move(self, course:list) -> None:
        for direction, amount in course:
            if direction == "up":
                self.aim -= int(amount)
            elif direction == "down":
                self.aim += int(amount)
            elif direction == "forward":
                self.horizontal += int(amount)
                self.depth += (self.aim * int(amount))
            else:
                pass
            print(f"Direction: {direction} Amount: {amount} Depth: {self.depth} Horizontal: {self.horizontal} Aim: {self.aim}")

    def get_depth(self) -> int:
        return self.depth

    def get_horizontal(self) -> int:
        return self.horizontal
    
    def get_aim(self) -> int:
        return self.aim

    def get_final_position(self) -> int:
        return self.horizontal * self.depth

def main():
    input = get_input("input.txt")
    submarine = Submarine(input)
    print(f"Depth: {submarine.get_depth()}")
    print(f"Horizontal: {submarine.get_horizontal()}")
    print(f"Final: {submarine.get_final_position()}")

def get_input(path:str) -> list:
    with open(path) as f:
        return [line for line in f.read().splitlines()]

if __name__ == "__main__":
    main()
