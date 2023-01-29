# Advent of Code 2021
My solutions to 2021's [Advent of Code](https://adventofcode.com/2021/about).

The solutions are provided in Python, Lua, and as homebrew Nintendo 3DS programs (C++).

Each day has its own `README.md` file with the corresponding puzzle's description, automatically transformed into markdown, to ease the remembering and understanding of the solutions. Obviously, the creator of these puzzles and descriptions is [Eric Wastl](https://twitter.com/ericwastl).

Each program responsible for solving a puzzle also checks that the output generated is my own correct solution to that puzzle (which is hardcoded into the source code after solving the puzzle). This is done with an `assert` in the last (or second to last, if there's an `exit()`) line executed in the program. The programs also have some commented-out debug lines, or other explanations, to give some insight about how their development process went.

There were no specific objectives set for the solutions' code in terms of time, memory or code quality optimizations. My only goal was to code the solutions in languages I wanted to get more used to (Lua and 3DS C++).

**EDIT:** As much as I would like to code the solutions for all the days using Lua and C++, programming these kind of puzzles using those languages requires writing considerable amounts of boilerplate code for minor functionalities. In that regard, coding the solutions in Python seems like the right decision due to its builtin functionalities and flexibility. Lua and C++ offer no more advantage to me than learning a new language; however, recoding solutions that in Python take considerably less effort to program, or programming the Python builtin functionalities in these languages feels like a pointless chore. I feel like the right move to ease programming the solutions in these languages would be to expand my utility libraries to add some (more) of those Python builtin functionalitites. However, I don't have the time or desire to do so right now. Besides, adding functions to a language so that it feels more like another languge doesn't seem like the best way of learning that language.

~~I may or may not drop midway through the event. Puzzles completion is not guaranteed.~~

## Unfinished days

**Python**
 - Day 24 is not generic. The puzzle was solved by hand, and the programs are only used to validate the solution.

**Lua**
 - Day 8, part 2.
 - Day 15, part 2.
 - Days 16-25.

**3DS C++**
 - Day 4.
 - Day 5.
 - Days 8-25.
