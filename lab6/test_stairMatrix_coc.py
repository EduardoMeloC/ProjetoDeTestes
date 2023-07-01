import stairMatrix

class TestStairMatrixPredicado():
    def test_stairMatrix_1(self):
        input_arr = [0,1,1,0]
        assert (stairMatrix.isStairMatrix(2, 2, input_arr) == 'N')

    def test_stairMatrix_2(self):
        input_arr = [1,1,1,0]
        assert (stairMatrix.isStairMatrix(2, 2, input_arr) == 'N')

    def test_stairMatrix_3(self):
        input_arr = [0,0,0,0]
        assert (stairMatrix.isStairMatrix(2, 2, input_arr) == 'S')