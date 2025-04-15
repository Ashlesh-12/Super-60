def test_numbers():
    assert 1 in [1,2,3]
def test_comparison():
    a,b=5,10
    assert a<b
def test_string():
    assert "fizz" in "fizzbuzz"
def test_failure():
    assert 1 in [2,3,4]