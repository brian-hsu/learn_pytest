def test_addition_false():
    result = add(2, 3)
    assert result == 2, "加法結果應該等於5"

def add(x, y):
    return x + y

def test_addition():
    result = add(2, 3)
    assert result == 5, "加法結果應該等於5"

def test_subtraction():
    result = add(5, 3)
    assert result != 2, "減法結果應該不等於2"

def test_subtraction_false():
    result = add(5, 3)
    assert result == 0