# Multiprocessing utilities

from multiprocessing import Process, Pool, get_start_method, set_start_method, Queue
from logging import getLogger
from typing import Callable

__all__ = ["mp_print", "mp_exec"]

logger = getLogger(__name__)

try:
    set_start_method("fork")
    logger.info("Set start method to fork")
except:
    set_start_method("spawn")
    logger.warning("Failed to set start method to fork, multiprocessing will not be used")

is_mp = get_start_method() == "fork"
print_queue = Queue()

def _mp_print_proc_task():
    while True:
        if (str_ := print_queue.get()) is None:
            break
        print(str_)

def mp_print(str_: str):
    if is_mp:
        print_queue.put(str_)
    else:
        print(str_)

def mp_exec(func: Callable, args: tuple, unorder=False):
    if is_mp:
        _mp_print_proc = Process(target=_mp_print_proc_task, daemon=True)
        _mp_print_proc.start()

        with Pool() as pool:
            if unorder:
                yield from pool.imap_unordered(func, args)
            else:
                yield from pool.map(func, args)

        print_queue.put(None)
        _mp_print_proc.join()
    else:
        for arg in args:
            yield func(arg)
