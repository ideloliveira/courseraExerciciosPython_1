from fatorial import fatorial

def test_fatorial0():
    assert fatorial(0) == 1
def test_fatorial1():
    assert fatorial(1) == 1
def test_fatorial_negativo():
    assert fatorial(-10) == 0
def test_fatorial4():
    assert fatorial(4) == 24
def test_fatorial5():
    assert fatorial(5) == 120
