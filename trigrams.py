# -*- coding: utf-8 -*-

import io
import re
import random
import sys

def init_write(fp="sherlock_small.txt", uw=50):
    file_text = open_fileFun(fp)
    sher_dic = gen_dic(file_text)
    gen_text(uw, sher_dic)



def open_fileFun(file_path):
    open_file = io.open(file_path, "r")
    file_text = open_file.read()
    return file_text

def gen_dic(file_text):
    new_dic = {}
    new_list = re.split("\W+", file_text)
    for idx, item in enumerate(new_list):
        if idx == (len(new_list) - 3):
            break
        else:
            new_dic.update({(new_list[idx], new_list[idx + 1]): new_list[idx + 2]})
    return new_dic

def gen_text(usr_words, sher_dic):
    first = sher_dic.get(random.choice(sher_dic.keys()))
    second = sher_dic.get(random.choice(sher_dic.keys()))
    story = first + " " + second

    for word in range(usr_words - 2):
        if sher_dic.get((first, second)):
            third = sher_dic.get((first, second))
            story += " " + third
            first = second
            second = third
        else:
            third = sher_dic.get(random.choice(sher_dic.keys()))
            story += " " + third
            first = second
            second = third
    print story

if __name__ == "__main__":
    init_write(sys.argv[1], int(sys.argv[2]))
