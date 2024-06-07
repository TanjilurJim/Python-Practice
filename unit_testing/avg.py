def avg(L):
    if not L:
        return None
    return sum(L)/len(L)

def test_avg():
    assert 3.0 == avg([1,2,3,4,5])
