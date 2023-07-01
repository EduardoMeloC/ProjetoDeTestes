import stairMatrix

class TestStairMatrixPredicado():
    def test_stairMatrix_1(self):
        input_arr = [0,1,1,0]
        assert (stairMatrix.isStairMatrix(2, 2, input_arr) == 'N')