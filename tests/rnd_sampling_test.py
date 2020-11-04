import unittest

from src.davil.sampling import sample_index_multinominal


class TestRandomIndexMultinominal(unittest.TestCase):

    def test(self):
        epsilon = 300
        num_samples = 100000

        probs = [0.1, 0.3, 0.4, 0.2]

        nums = [0, 0, 0, 0]
        for _ in range(num_samples):
            r = sample_index_multinominal(probs)
            nums[r] += 1

        print(nums)

        for i, n in enumerate(nums):
            assert abs(n - (probs[i] * num_samples)) < epsilon


if __name__ == '__main__':
    unittest.main()
