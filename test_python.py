import numpy as np
from math import pi, sqrt, hypot
def filt_nums(arg):
    if arg%2!=0:
        return False
    else:
        return True
print('dasda')
def test_funcs():
    assert list(filter(filt_nums, list(range(10)))) == list(range(0,10,2))
    assert list(map(lambda x: x**2, list(range(10)))) == list(np.arange(10)**2)
    assert sorted([1,6,3,7,2,6,4]) == [1, 2, 3, 4, 6, 6, 7]
    assert round(pi,3) == 3.142
    assert sqrt(4) == 2
    assert pow(2,4) == 16
    assert int(hypot(2,4)) == 4