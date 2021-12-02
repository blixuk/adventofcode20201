#!/usr/bin/env python
# file: adventofcode2020/01/01.py
# author: blixuk
# Day 1: Sonar Sweep
# Answer: 1616

def main():
    input = get_input("input.txt")
    data = process_data(input)
    print(data)

def process_data(data:list) -> int:
    return [i > data[count - 1] for count, i in enumerate(data)].count(True) + 1

def get_input(path:str) -> list:
    with open(path) as f:
        return [line for line in f.read().splitlines()]

if __name__ == "__main__":
    main()
