#!/usr/bin/env python
# file: adventofcode2020/01/02.py
# author: blixuk
# Day 1: Sonar Sweep: Part 2
# Answer: 1645

def main():
    input = get_input("input.txt")
    data = process_data(input)
    print(data)

def process_data(data:list) -> int:
    return [data[i] > data[i - 3] for i in range(3, len(data))].count(True)

def get_input(path:str) -> list:
    with open(path) as f:
        return [int(line) for line in f.read().splitlines()]

if __name__ == "__main__":
    main()
