import textdistance as td
import multiprocessing as mp


def dist(s1, s2, s3):
    if s3 == "L":
        return td.levenshtein(s1, s2)
    elif s3 == "D":
        return td.damerau_levenshtein(s1, s2)
    else:
        return -1

s1 = input()
s2 = input()

s3 = input()

with mp.Pool(processes=1) as pool:
    process = pool.apply_async(dist, (s1, s2, s3))
    try:
        print(process.get(timeout=1))
    except mp.context.TimeoutError:
        print(-1)

