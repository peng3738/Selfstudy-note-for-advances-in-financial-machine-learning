import multiprocessing as mp

def f(x):
    return x*x

if __name__ == '__main__':
    pool =mp.Pool(processes=4)              # start 4 worker processes

    # print "[0, 1, 4,..., 81]"
    print(pool.map(f, range(10)))

    # print same numbers in arbitrary order
    for i in pool.imap_unordered(f, range(10)):
        print(i)
