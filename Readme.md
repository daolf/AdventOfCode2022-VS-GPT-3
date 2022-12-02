# Advent of Code 2022 VS GPT-3

This repository is an attempt to solve the famous [Advent Of Code](https://adventofcode.com) code puzzles with the GPT-3 AI model.

Basically, every day, I will ask [GPT-3 chat](https://chat.openai.com/chat) interface to solve problem:
- I'll send them the raw problem statement
- Add "assume that the input is in a file called 'day_X.txt'"
- Run the output script
- When not working, I'll simply paste the exception in the chat interface

## File structure:

- day_X_a.py: Solution given from GPT
- day_X_input.txt: Input of the problem
- day_X_gpt.png: Screenshot of my "conversation" with the agent (file corrupted for day 1)

## Results:

| Day   | GPT-3|
|-------|--|
| 1 - 1 | ✅|
| 1 - 2 | ✅|
| 2 - 1 | ❌|
| 2 - 2 | ❌|


*Each days, there are 2 problemes to solve, but n°2 can only be solved after n°1 has been solved already.*
