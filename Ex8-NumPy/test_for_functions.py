from general_functions_native import *
from general_functions_vec import *

def test_ndarray_equal():
    matrix1 = numpy.array([[1.0, 2.0, 3.0000001], [4.0, 5.0, 6.0]])
    matrix2 = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    # print(f"Test1: {ndarray_equal(matrix1, matrix2)}")
    assert ndarray_equal(matrix1, matrix2) == True
    matrix3 = numpy.array([[1.0, 2.0, 3.00001], [4.0, 5.0, 6.0]])
    matrix4 = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    # print(f"Test2: {ndarray_equal(matrix3, matrix4)}")
    assert ndarray_equal(matrix3, matrix4) == False
    matrix5 = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    matrix6 = numpy.array([[1.0, 2.1, 3.0], [4.0, 5.0, 6.1]])
    # print(f"Test3: {ndarray_equal(matrix5, matrix6)}")
    assert ndarray_equal(matrix5, matrix6) == False
    matrix7 = numpy.array([[1.0, 2.0, 3.0000005], [4.0, 5.0, 6.0]])
    matrix8 = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.00001]])
    # print(f"Test4: {ndarray_equal(matrix7, matrix8)}")
    assert ndarray_equal(matrix7, matrix8) == False
    matrix9 = numpy.array([[1.0, 2.0, 3.0, 4.0], [4.0, 5.0, 6.0]])
    matrix10 = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    # print(f"Test5: {ndarray_equal(matrix9, matrix10)}")
    assert ndarray_equal(matrix9, matrix10) == False

def test_list_equal():
    matrix1 = [[1.0, 2.0, 3.0000001], [4.0, 5.0, 6.0]]
    matrix2 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    # print(f"Test1:{list_equal(matrix1, matrix2)}") 
    assert list_equal(matrix1, matrix2) == True
    matrix3 = [[1.0, 2.0, 3.00001], [4.0, 5.0, 6.0]]
    matrix4 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    # print(f"Test2:{list_equal(matrix3, matrix4)}")
    assert list_equal(matrix3, matrix4) == False
    matrix5 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    matrix6 = [[1.0, 2.1, 3.0], [4.0, 5.0, 6.1]]
    # print(f"Test3:{list_equal(matrix5, matrix6)}")
    assert list_equal(matrix5, matrix6) == False
    matrix7 = [[1.0, 2.0, 3.0000005], [4.0, 5.0, 6.0]]
    matrix8 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.00001]]
    # print(f"Test4:{list_equal(matrix7, matrix8)}")
    assert list_equal(matrix7, matrix8) == False
    matrix9 = [[1.0, 2.0, 3.0, 4.0], [4.0, 5.0, 6.0]]
    matrix10 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    # print(f"Test5:{list_equal(matrix9, matrix10)}")
    assert list_equal(matrix9, matrix10) == False

def test_sum_matrix_native():
    matrix_4x4 = [[1.1, 2.2, 3.3, 4.4],  
    [5.5, 6.6, 7.7, 8.8],  
    [9.9, 10.1, 11.2, 12.3],  
    [13.4, 14.5, 15.6, 16.7]]
    assert sum_matrix_native(matrix_4x4, 0) == [29.9, 33.4, 37.8, 42.2]
    assert sum_matrix_native(matrix_4x4, 1) == [11.0, 28.6, 43.5, 60.2]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    assert sum_matrix_native(matrix,0) == [12,15,18]
    assert sum_matrix_native(matrix,1) == [6,15,24]
 
def test_sum_matrix_vec():
    A = numpy.array(
    [[4,3,8,10],
    [6,0,5,14],
    [1,5,9,-3]])
    print(sum_matrix_vec(A,0)) # [11 8 22 21]
    print(sum_matrix_vec(A,1)) # [25 25 12]

def test_mul_mat_native():
    A0 = [[1, 4, 6],[8, 9, 7],[4, 6, 3]]
    B0 = [[1, 2],[1, 4],[1, 3]]
    assert mul_mat_native(A0,B0) == [[11.0, 36.0], [24.0, 73.0], [13.0, 41.0]]
    A1 = [[1, 2, 3],[4, 5, 6]]
    B1 = [[7, 8],[9, 10],[11, 12]]
    assert mul_mat_native(A1,B1) == [[58.0, 64.0], [139.0, 154.0]]
    A2 = [[1, 2], [3, 4], [5, 6]]
    B2 = [[7, 8, 9, 10], [11, 12, 13, 14]]
    assert mul_mat_native(A2, B2) == [[29.0, 32.0, 35.0, 38.0], [65.0, 72.0, 79.0, 86.0], [101.0, 112.0, 123.0, 134.0]]
    A3 = [[2, 3], [1, 4]]
    B3 =  [[5, 6, 7], [8, 9, 10]]
    assert mul_mat_native(A3, B3) == [[34.0, 39.0, 44.0], [37.0, 42.0, 47.0]]
    A4 = [[1, 2, 3],[4, 5, 6]]
    B4 = [[7, 8],[9, 10]]
    try:
        mul_mat_native(A4,B4)
        print("Error wasn't raised for\n A: {A4}\n B: {B4}\n, not good!")
    except Exception as e:
        (f"Error {e} was raised correctly for\n A: {A4}\n B: {B4}")
    A5 = [[1, 2],[3, 4],[5, 6]]
    B5 = [[7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18]]
    try:
        mul_mat_native(A5,B5)
        print("Error wasn't raised for\n A: {A5}\n B: {B5}\n, not good!")
    except Exception as e:
        print(f"Error {e} was raised correctly for\n A: {A5}\n B: {B5}")


def test_inverse_native():  
    A0 =[[1,-1],[-1,2]]
    B0 =[[2,1],[1,1]]
    assert is_inverse_native(A0,B0) == True
    A1 =[[4,3,8],[6,2,5],[1,5,9]]
    B1 =[[-0.14285714,0.26530612,-0.02040816],[-1,0.57142857,0.57142857],[0.57142857,-0.34693878,-0.20408163]]
    assert is_inverse_native(A1,B1) == True
    A2 =[[4,3,8],[6,2,5],[1,5,9]]
    B2 =[[0,1,2],[3,4,5],[6,7,8]]
    assert is_inverse_native(A2,B2) == False

def test_inverse_vec():
    A0 = numpy.array([[4, 3, 8],[6, 2, 5],[1, 5, 9]])
    B0 = numpy.array([[-0.14285714,0.26530612,-0.02040816],[-1,0.57142857,0.57142857],[ 0.57142857,-0.34693878,-0.20408163]])
    assert is_inverse_vec(A0,B0) == True
    A1 = numpy.array([[4, 3, 8],[6, 2, 5],[1, 5, 9]])
    B1 = numpy.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
    assert is_inverse_vec(A1,B1) == False

