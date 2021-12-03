#!/usr/bin/env python
# file: adventofcode2020/03/01.py
# author: blixuk
# Day 3: Binary Diagnostic
# Answer: 011111101100

def main():
    input = get_input("input.txt")
    rates = get_gamma_epsilon_rate(input)
    power = get_power_consumption(rates)
    print(power)

def get_gamma_epsilon_rate(input:list) -> tuple:
    compare = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    for data in input:
        for i in range(len(data)):
            if data[i] == "1":
                compare[i][0] += 1
            else:
                compare[i][1] += 1
    gamma_rate = []
    epsilon_rate = []
    for data in compare:
        if data[0] > data[1]:
            gamma_rate.append("1")
            epsilon_rate.append("0")
        else:
            gamma_rate.append("0")
            epsilon_rate.append("1")
    return (''.join(gamma_rate), ''.join(epsilon_rate))

def get_power_consumption(input:tuple) -> int:
    return int(input[0], 2) * int(input[1], 2)

def get_input(path:str) -> list:
    with open(path) as f:
        return [line for line in f.read().splitlines()]

if __name__ == "__main__":
    main()
