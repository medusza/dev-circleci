from main import add


def test_add():
    assert add(1, 2) == 3
    print("Test add() passed...")
    
if __name__ == "__main__":
    test_add()