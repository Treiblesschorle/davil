import unittest

import numpy as np

from src.davil.lists import partition_train_test_validation


class TestPartitions(unittest.TestCase):

    def test(self):
        def check_sets(lists):
            for ts in zip(*lists):
                for t in ts:
                    t0 = ts[0].split('_')[0]
                    assert t0 == t.split('_')[0]

        xs = [np.arange(20) for _ in range(4)]
        chars = [chr(x) for x in range(97, 101, 1)]
        xs = [[str(xx) + '_' + c for xx in x] for x, c in zip(xs, chars)]

        trs, tes, vals = partition_train_test_validation(xs)

        check_sets(trs)
        check_sets(tes)
        check_sets(vals)

        assert len(trs[0]) == round(20 * 0.7)
        assert len(tes[0]) == round(20 * 0.1)
        assert len(vals[0]) == round(20 * 0.2)


if __name__ == '__main__':
    unittest.main()
