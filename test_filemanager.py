from questions import return_input
from money import func
from console_file import func_console
def test_funcs():
    assert func()==None

def test_return():
    assert return_input('15') == 15

def test_console():
    assert func_console() == None