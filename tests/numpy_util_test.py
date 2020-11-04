import numpy as np
import unittest

from src.davil import nutil


class TestNumpyUtils(unittest.TestCase):

    def test_copy_to_from_subarray_with_mask(self):
        sub = np.reshape(np.arange(1, 10), (3, 3))

        mask = np.array([[1, 0, 1],
                         [0, 1, 0],
                         [0, 1, 1]])

        ref = np.array([[1,   2,   3,  4,  5],
                        [6,   1,   8,  3, 10],
                        [11, 12,   5, 14, 15],
                        [16, 17,   8,  9, 20],
                        [21, 22,  23, 24, 25]])

        arr = np.reshape(np.arange(1, 26), (5, 5))
        nutil.copy_to_from_subarray(arr, sub, (1, 1), pivot='top_left', subarray_mask=mask)
        np.testing.assert_array_equal(arr, ref)

        arr = np.reshape(np.arange(1, 26), (5, 5))
        nutil.copy_to_from_subarray(arr, sub, (2, 2), pivot='center', subarray_mask=mask)
        np.testing.assert_array_equal(arr, ref)

    def test_copy_to_from_subarray_2d(self):
        sub = np.reshape(np.arange(1, 10), (3, 3))

        ref = np.array([[1,   2,  3,  4,  5],
                        [6,   1,  2,  3, 10],
                        [11,  4,  5,  6, 15],
                        [16,  7,  8,  9, 20],
                        [21, 22, 23, 24, 25]])

        arr = np.reshape(np.arange(1, 26), (5, 5))
        nutil.copy_to_from_subarray(arr, sub, (1, 1), pivot='top_left')
        np.testing.assert_array_equal(arr, ref)

        arr = np.reshape(np.arange(1, 26), (5, 5))
        nutil.copy_to_from_subarray(arr, sub, (2, 2), pivot='center')
        np.testing.assert_array_equal(arr, ref)

    def test_copy_to_from_subarray_2d_out_of_bounds(self):
        sub = np.reshape(np.arange(1, 10), (3, 3))

        ref1 = np.array([[1,   2,  3,  4,  5],
                         [6,   7,  8,  9, 10],
                         [11, 12, 13, 14, 15],
                         [16, 17, 18,  1,  2],
                         [21, 22, 23,  4,  5]])

        arr = np.reshape(np.arange(1, 26), (5, 5))
        nutil.copy_to_from_subarray(arr, sub, (3, 3), pivot='top_left')
        np.testing.assert_array_equal(arr, ref1)

        ref2 = np.array([[5,   6,  3,  4,  5],
                         [8,   9,  8,  9, 10],
                         [11, 12, 13, 14, 15],
                         [16, 17, 18, 19, 20],
                         [21, 22, 23, 24, 25]])

        arr = np.reshape(np.arange(1, 26), (5, 5))
        nutil.copy_to_from_subarray(arr, sub, (0, 0), pivot='center')
        np.testing.assert_array_equal(arr, ref2)

    def test_copy_to_from_subarray_3d(self):
        sub0 = np.reshape(np.arange(1, 10), (3, 3))
        sub1 = np.reshape(np.arange(10, 19), (3, 3))
        sub = np.stack([sub0, sub1], axis=2)

        ref_c0 = np.array([[1,  2,  3,  4, 5],
                          [6,   1,  2,  3, 10],
                          [11,  4,  5,  6, 15],
                          [16,  7,  8,  9, 20],
                          [21, 22, 23, 24, 25]])

        ref_c1 = np.array([[1,   2,  3,  4, 5],
                           [6,  10, 11, 12, 10],
                           [11, 13, 14, 15, 15],
                           [16, 16, 17, 18, 20],
                           [21, 22, 23, 24, 25]])

        ref = np.stack([ref_c0, ref_c1], axis=2)

        arr = np.reshape(np.arange(1, 26), (5, 5))
        arr = np.stack([arr, arr], axis=2)
        nutil.copy_to_from_subarray(arr, sub, (1, 1), pivot='top_left')
        np.testing.assert_array_equal(arr, ref)

        arr = np.reshape(np.arange(1, 26), (5, 5))
        arr = np.stack([arr, arr], axis=2)
        nutil.copy_to_from_subarray(arr, sub, (2, 2), pivot='center')
        np.testing.assert_array_equal(arr, ref)

    def test_copy_to_from_subarray_3d_out_of_bounds(self):
        sub0 = np.reshape(np.arange(1, 10), (3, 3))
        sub1 = np.reshape(np.arange(10, 19), (3, 3))
        sub = np.stack([sub0, sub1], axis=2)

        ref_c0 = np.array([[1,  2,  3,  4, 5],
                          [6,   7,  8,  9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18,  1,  2],
                          [21, 22, 23,  4,  5]])

        ref_c1 = np.array([[1,  2,  3,  4, 5],
                          [6,   7,  8,  9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 10, 11],
                          [21, 22, 23, 13, 14]])

        ref = np.stack([ref_c0, ref_c1], axis=2)

        arr = np.reshape(np.arange(1, 26), (5, 5))
        arr = np.stack([arr, arr], axis=2)
        nutil.copy_to_from_subarray(arr, sub, (3, 3), pivot='top_left')
        np.testing.assert_array_equal(arr, ref)

        arr = np.reshape(np.arange(1, 26), (5, 5))
        arr = np.stack([arr, arr], axis=2)
        nutil.copy_to_from_subarray(arr, sub, (4, 4), pivot='center')
        np.testing.assert_array_equal(arr, ref)

    def test_array_to_tuples(self):
        x = np.array([[1, 0, 3, 4, 5],
                      [0, 0, 0, 9, 0],
                      [0, 0, 1, 0, 5],
                      [0, 0, 0, 0, 0],
                      [0, 0, 3, 0, 0]])

        ref = [(0, 0),
               (0, 2),
               (0, 3),
               (0, 4),
               (1, 3),
               (2, 2),
               (2, 4),
               (4, 2)]

        for a, b in zip(ref, nutil.argwhere_to_tuples(np.argwhere(x))):
            assert a == b

    def test_resampling(self):
        x = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9],
                      [7, 8, 9]])

        locs = [(0, 0), (0.5, 0), (3, 2), (2.5, 1), (0.5, 1.5)]

        res = nutil.resample_2d(x, locs)

        np.testing.assert_array_equal(np.array([1.0, 2.5, 9.0, 8.0, 4.0]), res)

    def test_resampling_channelwise(self):
        x = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9],
                      [7, 8, 9]])
        x = nutil.sld([x, x])

        locs = [(0, 0), (0.5, 0), (3, 2), (2.5, 1), (0.5, 1.5)]
        vals = np.array([1.0, 2.5, 9.0, 8.0, 4.0])
        vals = nutil.sld([vals, vals])

        res = nutil.resample_2d_channelwise(x, locs)

        np.testing.assert_array_equal(vals, res)


if __name__ == '__main__':
    unittest.main()
