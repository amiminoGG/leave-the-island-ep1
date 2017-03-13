import time
from contextlib import contextmanager

_s = 0
_e = 0

@contextmanager
def Timer():
    _s = time.time()
    try:
        yield
    finally:
        print("%.3f s" % (time.time() - _s))
