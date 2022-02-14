import code_413_arithmetic_slices as c

def test_example_1():
    s = c.Solution()
    assert s.numberOfArithmeticSlices([1,2,3,4,]) == 3

def test_example_2():
    s = c.Solution()
    assert s.numberOfArithmeticSlices([1]) == 0