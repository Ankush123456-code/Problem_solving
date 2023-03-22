from Problem_solving.Unit_test_practice.app.sample import add


def test_add():
    assert add(1, 2) == 3


def test_add2():
    assert add(3, 5) == 8
