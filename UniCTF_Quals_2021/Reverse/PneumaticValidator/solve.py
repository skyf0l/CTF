#!/usr/bin/env python3

import numpy as np
import os
import string
import re
from functools import partial
from multiprocessing import Pool
import logging

# enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

'''

first loop -> HTB{PN7Um4t1C_l0g1C}
second loop -> HTB{pN3Um4t1C_l0g1C}

'''

BINARY = './pneumaticvalidator'

NB_PROCESSES = 10

FLAG_LENGTH = 0x14
POSSIBLE_CHARS = string.ascii_letters + string.digits + '_{}'

BREAKPOINT_ADDRESS = hex(0x555555559631)


# calculate fitness of char at index by using gdb-peda
# the aim is to set a breakpoint at the end of fitness calculation function
# then, run the program the partial flag, and read the RAX register in which is stored the fitness
def calculate_char_fitness(char: str, char_index: int, partial_flag: str) -> str:
    # replace char at index in partial_flag
    partial_flag = partial_flag[:char_index] + char + partial_flag[char_index + 1:]

    # generate gdb command to set breakpoint and run program with partial flag
    gdb_cmd = f'b *{BREAKPOINT_ADDRESS}\nr {partial_flag}'

    # generate shell command to run gdb-peda with gdb command
    cmd = f'echo "{gdb_cmd}" | gdb {BINARY} 2> /dev/null'

    # run command in shell and get output
    output = os.popen(cmd).read()

    # get fitness stored in RAX register from output
    m = re.search(r'RAX.+(0x[0-9a-f]+)', output)
    fitness = int(m.group(1), 16)

    # print fitness for debug
    logging.debug(f'Fitness of {char}: {fitness} ({partial_flag})')

    # return fitness
    return fitness


# find char at index by bruteforce all possible chars and return the one with lowest fitness
def find_char(char_index: int, partial_flag: str) -> str:

    # create a pool of processes to increase speed
    with Pool(processes=NB_PROCESSES) as pool:

        # create partial function with char_index and partial_flag
        # because we need it to pass multiple arguments to the pool
        f = partial(calculate_char_fitness, char_index=char_index, partial_flag=partial_flag)

        # process function in parallel with pool.map
        result = pool.map(f, POSSIBLE_CHARS)

    # get char with lowest fitness
    best_char_id = np.argmin(result)
    best_char = POSSIBLE_CHARS[best_char_id]

    # return most probable char
    return best_char


def find_flag(flag: str) -> str:

    for i in range(FLAG_LENGTH):
        # get most probable char at index
        char = find_char(i, flag)
        # replace char in flag
        flag = flag[:i] + char + flag[i + 1:]
        # print partial flag
        logging.info(f'Char {i + 1}/{FLAG_LENGTH}: {char} ({flag})')

    # return most probable flag
    return flag


def main():
    # create flag template
    flag = '.' * FLAG_LENGTH

    # find flag from template
    flag = find_flag(flag)
    logging.info(f'First iteration flag: {flag}')

    # reiterate with already found flag to confirm it and avoid false positives
    flag = find_flag(flag)
    logging.info(f'Second iteration flag: {flag}')

    logging.info(f'Flag is: {flag}')


if __name__ == '__main__':
    main()
