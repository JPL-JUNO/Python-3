"""
@Title: 素数队列
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-19 22:26:50
@Description: 
"""

import math
import time
import multiprocessing
from multiprocessing import Queue
import argparse
# 由父进程来表明没有可用的工作，也称为哨兵，因为它确保终结处理循环
FLAG_ALL_DONE = b"WORK_FINISHED"
# 由工作者来确认它已经看到了毒药，并把自己关闭
FLAG_WORKER_FINISHED_PROCESSING = b"WORKER_FINISHED_PROCESSING"


def check_prime(possible_primes_queue: Queue, definite_primes_queue: Queue):
    while True:
        n = possible_primes_queue.get()
        if n == FLAG_ALL_DONE:
            definite_primes_queue.put(FLAG_WORKER_FINISHED_PROCESSING)
            break
        else:
            if n % 2 == 0:
                continue
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    break
            else:
                definite_primes_queue.put(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Primes Queue")
    parser.add_argument("nbr_workers", type=int,
                        help="Number of primes workers, e.g. 1, 2, 4, 8")
    args = parser.parse_args()
    print(args)

    primes = []
    manager = multiprocessing.Manager()
    possible_prime_queue = manager.Queue()
    definite_primes_queue = manager.Queue()

    processes = []
    for _ in range(args.nbr_workers):
        p = multiprocessing.Process(target=check_prime,
                                    args=(possible_prime_queue, definite_primes_queue))
        processes.append(p)
        p.start()
    t1 = time.time()
    number_range = range(100_000_000, 101_000_000)

    for possible_prime in number_range:
        possible_prime_queue.put(possible_prime)
    print("ALL JOBS ADDED TO THE QUEUE")

    for n in range(args.nbr_workers):
        possible_prime_queue.put(FLAG_ALL_DONE)
    print("NOW WAITING FOR RESULTS...")
    processors_indicating_they_have_finished = 0

    while True:
        new_result = definite_primes_queue.get()
        if new_result == FLAG_WORKER_FINISHED_PROCESSING:
            print("WORKER {} HAS JUST FINISHED".format(
                processors_indicating_they_have_finished))
            processors_indicating_they_have_finished += 1
            if processors_indicating_they_have_finished == args.nbr_workers:
                break
        else:
            primes.append(new_result)
    assert processors_indicating_they_have_finished == args.nbr_workers
    print("Took:", time.time() - t1)
    print(len(primes), primes[:10], primes[-10:])
