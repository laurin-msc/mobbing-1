from sim import sim, Grid

def test_sim():
    assert Grid().columns == 10
    assert Grid().rows == 10
    assert Grid()[4, 2] == None
