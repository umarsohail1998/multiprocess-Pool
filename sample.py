from multiprocessing import Pool
import time
 
def func(x):
    return x + 2
 
with Pool(2) as pool:
    arr = []
    for _ in tqdm.tqdm(pool.imap_unordered(func, range(100000)), total=100000):
        arr.append(x)
