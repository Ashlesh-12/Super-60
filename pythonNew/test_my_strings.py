from my_strings import to_uppercase,capitalize,to_lowercase
def test1():
    assert to_uppercase("ashlesh") == "ASHLESH"
    
def test2():
    assert capitalize("ashlesh") == "Ashlesh"
    
def test3():
    assert to_lowercase("ASHLESH") == "ashlesh"