# Kaiwen zhu(kz8pr), Yanwen Wang(yw9cj)
import robot


def square():
    r = robot.Robot(1)
    r.say("Ready!")
    i = 1
    while r.check_east():
        r.east()
        i += 1
    x = i**2
    r.say(x)
    r.done()


def rect():
    r = robot.Robot(2)
    r.say("Ready!")
    i = 1
    j = 1
    while r.check_east():
        r.east()
        i += 1
    while r.check_south():
        r.south()
        j += 1
    x = i*j
    r.say(x)
    r.done()


def middle():
    r = robot.Robot(3)
    r.say("Ready!")
    i = 1
    j = 1
    while r.check_west():
        r.west()
    while r.check_north():
        r.north()
    while r.check_east():
        r.east()
        i += 1
    while r.check_south():
        r.south()
        j += 1
    x = i*j
    r.say(x)
    r.done()

