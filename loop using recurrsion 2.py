def loop(start = 0, end = 1, step = 1):
    loop_s = start
    loop_end = end
    loop_step = step
    now_s = start
    print(now_s)
    now_s = start + step
    if now_s <= end - step:
        return loop(start = now_s, end = loop_end, step = loop_step)

loop(0, 10, 2)
