"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was CVCWCRTVQ.

--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was CNSCZWLVT.
"""

crates = [['W', 'R', 'F'], ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
         ['P', 'M', 'Z', 'N', 'L'], ['J', 'C', 'H', 'R'],
         ['C', 'P', 'G', 'H', 'Q', 'T', 'B'], ['G', 'C', 'W', 'L', 'F', 'Z'],
         ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'], ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
         ['J', 'W', 'H', 'G', 'R', 'S', 'V']]
instructions = """ move 2 from 4 to 9
move 5 from 2 to 9
move 1 from 5 to 1
move 3 from 1 to 4
move 2 from 4 to 6
move 7 from 6 to 9
move 5 from 3 to 9
move 1 from 8 to 6
move 3 from 2 to 3
move 12 from 9 to 3
move 4 from 9 to 7
move 15 from 3 to 9
move 1 from 1 to 5
move 2 from 6 to 5
move 18 from 9 to 1
move 6 from 8 to 1
move 1 from 8 to 7
move 5 from 7 to 2
move 6 from 1 to 2
move 7 from 9 to 6
move 6 from 1 to 3
move 5 from 3 to 9
move 3 from 9 to 1
move 1 from 7 to 9
move 4 from 2 to 1
move 5 from 6 to 3
move 1 from 3 to 4
move 1 from 5 to 9
move 2 from 9 to 6
move 5 from 5 to 9
move 10 from 1 to 8
move 4 from 3 to 8
move 3 from 4 to 9
move 4 from 6 to 9
move 14 from 8 to 6
move 1 from 3 to 8
move 14 from 9 to 4
move 6 from 1 to 6
move 1 from 8 to 2
move 3 from 5 to 8
move 1 from 8 to 9
move 1 from 8 to 1
move 5 from 4 to 9
move 1 from 8 to 4
move 3 from 9 to 4
move 3 from 7 to 5
move 7 from 6 to 3
move 7 from 4 to 1
move 3 from 9 to 1
move 7 from 2 to 3
move 1 from 4 to 8
move 8 from 6 to 2
move 2 from 7 to 4
move 1 from 7 to 4
move 1 from 7 to 9
move 1 from 5 to 9
move 1 from 9 to 4
move 1 from 4 to 2
move 8 from 4 to 9
move 1 from 4 to 2
move 5 from 9 to 4
move 2 from 6 to 9
move 1 from 6 to 9
move 1 from 8 to 1
move 13 from 3 to 2
move 1 from 3 to 9
move 2 from 6 to 8
move 1 from 8 to 1
move 14 from 1 to 7
move 4 from 2 to 1
move 2 from 9 to 5
move 3 from 9 to 7
move 1 from 8 to 2
move 4 from 1 to 5
move 1 from 4 to 7
move 3 from 9 to 1
move 7 from 7 to 4
move 14 from 2 to 8
move 3 from 1 to 7
move 3 from 5 to 4
move 2 from 1 to 9
move 11 from 8 to 9
move 3 from 7 to 8
move 3 from 8 to 6
move 6 from 4 to 3
move 2 from 6 to 8
move 8 from 4 to 3
move 3 from 8 to 7
move 2 from 8 to 2
move 2 from 3 to 9
move 1 from 6 to 8
move 5 from 2 to 7
move 10 from 9 to 7
move 1 from 8 to 5
move 3 from 5 to 2
move 6 from 7 to 5
move 19 from 7 to 3
move 9 from 5 to 9
move 6 from 2 to 6
move 2 from 7 to 3
move 29 from 3 to 8
move 2 from 7 to 9
move 5 from 8 to 1
move 12 from 9 to 6
move 1 from 3 to 8
move 1 from 2 to 7
move 1 from 3 to 1
move 10 from 6 to 1
move 1 from 6 to 7
move 9 from 1 to 9
move 2 from 1 to 2
move 12 from 9 to 4
move 7 from 6 to 3
move 8 from 3 to 7
move 5 from 7 to 6
move 19 from 8 to 3
move 10 from 4 to 6
move 1 from 4 to 6
move 6 from 8 to 6
move 1 from 4 to 2
move 6 from 6 to 3
move 3 from 2 to 7
move 13 from 6 to 3
move 1 from 9 to 1
move 6 from 1 to 8
move 1 from 6 to 5
move 1 from 5 to 4
move 3 from 7 to 1
move 2 from 1 to 3
move 11 from 3 to 8
move 1 from 4 to 3
move 3 from 8 to 4
move 1 from 7 to 5
move 3 from 8 to 9
move 2 from 9 to 2
move 7 from 8 to 3
move 1 from 7 to 9
move 1 from 1 to 4
move 32 from 3 to 4
move 1 from 5 to 9
move 2 from 8 to 3
move 2 from 6 to 4
move 1 from 9 to 4
move 1 from 9 to 2
move 3 from 3 to 1
move 1 from 8 to 6
move 1 from 6 to 2
move 1 from 9 to 3
move 1 from 1 to 7
move 1 from 8 to 7
move 2 from 3 to 8
move 1 from 8 to 4
move 1 from 1 to 2
move 2 from 4 to 8
move 1 from 1 to 8
move 26 from 4 to 6
move 3 from 8 to 5
move 3 from 7 to 6
move 7 from 6 to 3
move 18 from 6 to 8
move 16 from 8 to 9
move 1 from 5 to 1
move 2 from 8 to 3
move 3 from 9 to 8
move 3 from 6 to 4
move 2 from 5 to 4
move 1 from 6 to 4
move 2 from 7 to 2
move 2 from 3 to 9
move 4 from 8 to 3
move 1 from 1 to 2
move 6 from 9 to 7
move 2 from 2 to 5
move 12 from 3 to 1
move 9 from 9 to 2
move 10 from 1 to 3
move 2 from 5 to 9
move 8 from 4 to 7
move 13 from 7 to 6
move 6 from 6 to 5
move 4 from 5 to 3
move 2 from 5 to 4
move 8 from 4 to 3
move 1 from 7 to 2
move 15 from 2 to 7
move 8 from 3 to 7
move 1 from 1 to 6
move 7 from 7 to 1
move 5 from 1 to 6
move 7 from 3 to 2
move 3 from 1 to 6
move 12 from 7 to 9
move 12 from 9 to 8
move 1 from 7 to 1
move 2 from 9 to 5
move 1 from 1 to 9
move 4 from 4 to 2
move 4 from 8 to 4
move 2 from 7 to 2
move 4 from 6 to 5
move 4 from 8 to 9
move 1 from 8 to 4
move 5 from 5 to 3
move 5 from 2 to 4
move 5 from 9 to 5
move 1 from 3 to 6
move 1 from 7 to 8
move 12 from 3 to 9
move 4 from 2 to 6
move 7 from 4 to 9
move 13 from 6 to 4
move 3 from 6 to 9
move 4 from 4 to 2
move 1 from 3 to 4
move 21 from 9 to 7
move 4 from 2 to 1
move 3 from 5 to 4
move 8 from 7 to 6
move 2 from 7 to 2
move 11 from 4 to 2
move 1 from 9 to 7
move 1 from 5 to 7
move 1 from 1 to 8
move 5 from 2 to 5
move 1 from 3 to 5
move 2 from 4 to 9
move 3 from 4 to 8
move 3 from 1 to 8
move 1 from 9 to 6
move 8 from 7 to 8
move 9 from 6 to 5
move 1 from 9 to 6
move 1 from 6 to 4
move 3 from 7 to 5
move 1 from 6 to 9
move 12 from 5 to 1
move 2 from 5 to 8
move 1 from 9 to 6
move 2 from 7 to 6
move 9 from 1 to 8
move 1 from 6 to 9
move 1 from 9 to 2
move 1 from 4 to 2
move 2 from 6 to 7
move 5 from 8 to 3
move 2 from 7 to 4
move 16 from 8 to 5
move 2 from 3 to 8
move 7 from 5 to 1
move 3 from 3 to 8
move 7 from 5 to 7
move 4 from 5 to 2
move 6 from 7 to 9
move 2 from 9 to 6
move 2 from 9 to 2
move 1 from 6 to 8
move 12 from 2 to 6
move 2 from 9 to 6
move 1 from 5 to 2
move 3 from 5 to 4
move 9 from 2 to 6
move 6 from 8 to 3
move 1 from 7 to 5
move 1 from 6 to 7
move 1 from 7 to 8
move 1 from 5 to 8
move 5 from 1 to 2
move 3 from 4 to 5
move 4 from 6 to 8
move 5 from 2 to 9
move 5 from 8 to 4
move 1 from 1 to 4
move 9 from 8 to 4
move 1 from 2 to 3
move 3 from 6 to 8
move 4 from 9 to 2
move 2 from 6 to 4
move 2 from 3 to 1
move 4 from 4 to 7
move 6 from 4 to 5
move 10 from 6 to 8
move 4 from 1 to 9
move 4 from 7 to 5
move 3 from 3 to 9
move 6 from 9 to 8
move 2 from 2 to 9
move 8 from 4 to 3
move 2 from 2 to 7
move 1 from 4 to 9
move 6 from 3 to 8
move 2 from 7 to 8
move 6 from 5 to 9
move 5 from 5 to 6
move 2 from 5 to 9
move 7 from 9 to 5
move 2 from 1 to 9
move 6 from 5 to 8
move 1 from 5 to 1
move 2 from 3 to 6
move 1 from 3 to 6
move 4 from 9 to 5
move 1 from 3 to 4
move 1 from 1 to 2
move 1 from 2 to 1
move 1 from 6 to 8
move 14 from 8 to 5
move 6 from 5 to 1
move 16 from 8 to 3
move 2 from 8 to 2
move 10 from 6 to 7
move 1 from 6 to 9
move 2 from 2 to 9
move 2 from 7 to 3
move 1 from 8 to 5
move 3 from 9 to 1
move 4 from 9 to 5
move 9 from 3 to 8
move 2 from 3 to 6
move 5 from 3 to 8
move 1 from 4 to 2
move 12 from 8 to 4
move 1 from 8 to 9
move 4 from 5 to 9
move 7 from 7 to 1
move 10 from 5 to 2
move 2 from 5 to 2
move 1 from 6 to 5
move 2 from 5 to 2
move 5 from 2 to 6
move 4 from 9 to 6
move 6 from 4 to 9
move 2 from 3 to 4
move 6 from 4 to 7
move 6 from 7 to 5
move 10 from 1 to 5
move 4 from 1 to 2
move 4 from 6 to 3
move 6 from 9 to 7
move 2 from 4 to 9
move 7 from 7 to 6
move 1 from 9 to 7
move 2 from 9 to 8
move 2 from 8 to 2
move 1 from 2 to 5
move 3 from 8 to 4
move 4 from 2 to 7
move 3 from 4 to 7
move 2 from 3 to 5
move 2 from 3 to 2
move 18 from 5 to 3
move 6 from 3 to 1
move 8 from 3 to 1
move 8 from 7 to 9
move 9 from 2 to 5
move 3 from 2 to 3
move 7 from 3 to 7
move 3 from 6 to 4
move 1 from 7 to 1
move 7 from 6 to 7
move 1 from 2 to 9
move 1 from 4 to 2
move 13 from 7 to 2
move 10 from 5 to 3
move 1 from 2 to 9
move 7 from 1 to 5
move 8 from 9 to 5
move 1 from 9 to 5
move 1 from 9 to 8
move 1 from 8 to 2
move 8 from 5 to 3
move 18 from 3 to 5
move 2 from 4 to 1
move 3 from 2 to 5
move 27 from 5 to 1
move 17 from 1 to 5
move 2 from 2 to 3
move 1 from 6 to 5
move 2 from 2 to 5
move 1 from 6 to 4
move 1 from 6 to 9
move 2 from 3 to 5
move 17 from 5 to 6
move 1 from 9 to 3
move 6 from 2 to 4
move 1 from 3 to 2
move 3 from 4 to 9
move 1 from 2 to 9
move 1 from 4 to 7
move 3 from 5 to 2
move 2 from 5 to 1
move 1 from 5 to 2
move 1 from 7 to 3
move 18 from 1 to 4
move 1 from 3 to 1
move 5 from 4 to 2
move 1 from 5 to 1
move 9 from 2 to 7
move 1 from 4 to 5
move 1 from 2 to 9
move 8 from 6 to 2
move 13 from 4 to 2
move 2 from 4 to 9
move 1 from 5 to 2
move 1 from 6 to 8
move 6 from 7 to 5
move 1 from 8 to 4
move 1 from 7 to 6
move 1 from 6 to 1
move 7 from 6 to 5
move 1 from 7 to 9
move 6 from 9 to 3
move 2 from 9 to 7
move 2 from 5 to 7
move 4 from 7 to 8
move 4 from 5 to 4
move 1 from 6 to 7
move 3 from 3 to 8
move 6 from 5 to 9
move 2 from 3 to 5
move 4 from 4 to 7
move 1 from 3 to 1
move 2 from 2 to 3
move 6 from 9 to 6
move 1 from 7 to 1
move 19 from 2 to 4
move 2 from 5 to 6
move 2 from 8 to 9
move 2 from 1 to 2
move 2 from 2 to 5
move 2 from 4 to 3
move 4 from 6 to 2
move 1 from 7 to 8
move 6 from 1 to 8
move 3 from 5 to 1
move 5 from 2 to 5
move 1 from 6 to 7
move 9 from 8 to 1
move 2 from 3 to 6
move 4 from 6 to 5
move 1 from 6 to 2
move 9 from 5 to 2
move 3 from 4 to 6
move 12 from 4 to 6
move 1 from 9 to 4
move 1 from 3 to 1
move 3 from 4 to 8
move 1 from 3 to 6
move 6 from 6 to 2
move 1 from 4 to 5
move 3 from 6 to 2
move 4 from 1 to 5
move 1 from 5 to 1
move 2 from 8 to 9
move 7 from 6 to 3
move 1 from 3 to 1
move 1 from 8 to 1
move 3 from 8 to 9
move 4 from 3 to 5
move 3 from 7 to 3
move 5 from 3 to 7
move 1 from 9 to 1
move 4 from 9 to 2
move 15 from 2 to 7
move 14 from 1 to 7
move 5 from 5 to 1
move 9 from 7 to 2
move 1 from 9 to 6
move 1 from 7 to 4
move 1 from 4 to 6
move 2 from 6 to 2
move 9 from 2 to 5
move 4 from 2 to 4
move 4 from 7 to 5
move 6 from 5 to 9
move 7 from 1 to 8
move 6 from 2 to 8
move 1 from 1 to 2
move 3 from 9 to 5
move 18 from 7 to 8
move 2 from 4 to 6
move 2 from 4 to 6
move 3 from 7 to 6
move 3 from 5 to 3
move 1 from 2 to 6
move 5 from 6 to 8
move 29 from 8 to 1
move 2 from 3 to 5
move 25 from 1 to 6
move 2 from 9 to 5
move 1 from 7 to 8
move 6 from 8 to 2
move 1 from 9 to 1
move 15 from 6 to 8
move 1 from 3 to 8
move 14 from 8 to 7
move 5 from 1 to 3
move 1 from 6 to 2
move 2 from 5 to 7
move 10 from 6 to 2
move 4 from 5 to 7
move 6 from 5 to 1
move 2 from 1 to 4
move 19 from 7 to 9 """

import re

class Solution:
    def __init__(self, stacks, instruction_string):
        self.stacks = stacks
        self.instructions = instruction_string.split('\n')


    def move(self, quantity, from_stack, to_stack):
        crates = []
        while len(self.stacks[from_stack - 1]):
            if len(crates) == quantity:
                break
            crate = self.stacks[from_stack - 1].pop()
            crates.insert(0, crate)
        self.stacks[to_stack - 1].extend(crates)


    def read_instruction(self, instruction):
        numbers = re.findall(r'\d+', instruction)
        if len(numbers) != 3:
            return {'quantity': 0, 'from_stack': 0, 'to_stack': 0}
        return {'quantity': int(numbers[0]), 'from_stack': int(numbers[1]), 'to_stack': int(numbers[2])}


    def get_message(self):
        output = ''
        for stack in self.stacks:
            stack_length = len(stack)
            if stack_length > 0:
                output += stack[len(stack) - 1]
        return output


    def move_routine(self):
        for instruction in self.instructions:
            payload = self.read_instruction(instruction)
            self.move(payload['quantity'], payload['from_stack'], payload['to_stack'])

solution = Solution(crates, instructions)
solution.move_routine()
print(solution.get_message())
