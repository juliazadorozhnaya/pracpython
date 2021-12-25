import collections
import random
import asyncio
import sys

L = list(eval(input()))
random.shuffle(L)
LL = L.copy()


async def mege(b0, b1, e1,  n, eL, eR, eCur):
    if b1 - b0 != 0:
        await eL.wait()
        await eR.wait()

    b, e0, i = b0, b1, b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    eCur.set()




async def joiner():
    task_ev, n = [], 0
    events = collections.defaultdict(asyncio.Event)
    for p in range(4):
        b = 2 ** (p + 1)
        for i in range(0, len(L), b):
            task_ev.append(asyncio.create_task(mege(i, i + b // 2, i + b, n, events[4 * i + p], events[4 * (i + b // 2) + p], events[4 * i + p + 1])))
        for i in events:
            events[i].set()
        await asyncio.gather(*task_ev)

asyncio.run(joiner())
print(L)
