import random
from p5 import *
import time

cnt = 0

def bernoulli_trail():
    global cnt
    cnt += 1
    return random.randint(0, 1)

def setup():
    size(500, 500)

head_cnt = 0
p_head = 0
p_tail = 0

def draw():
    background(255)
    stroke(0)
    fill(255, 0, 0)
    rect((150, 300), -50, -p_head)
    fill(0, 255, 0)
    rect((300, 300), -50, -p_tail)

def mouse_pressed():
    global p_head, p_tail, head_cnt

    val = bernoulli_trail()
    head_cnt += val

    p_head = head_cnt * 150 / cnt
    p_tail = 150 - p_head

def key_pressed():
    if key == ' ':
        for i in range(100):
            mouse_pressed()

if __name__ == "__main__":
    run()