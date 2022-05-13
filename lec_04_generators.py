from time import time


# open console to play with this script. Tape 'python3 -i lec_04_generators.py'
# for iteration on yield use function 'next()'
def gen_filename():  # generate unical file name based on UNIX-time
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))

        sum = 234 + 123
        print(sum)


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('leonid')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
