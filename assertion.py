def test_sum():
    assert sum([1,1,1]) == 3, "should be 3"

def test_sum_tuple():
    assert sum((1,2,2)) == 4, "should be 5"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")