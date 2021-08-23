from mlproject.distance import haversine

a=1
b=2
c=3
d=4
def test_type_distance():
    assert type(haversine(a, b, c, d)) == float
