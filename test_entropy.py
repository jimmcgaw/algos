from entropy import compute_entropy, compute_cross_entropy
import pytest


class TestEntropy:
    def test_entropy_uniform_distribution(self):
        # entropy is maximum when all values are equally probable
        entropy = compute_entropy(list(range(1,31)))
        assert entropy == pytest.approx(3.401197381662154)

    def test_entropy_degenerate_distribution(self):
        # entropy where only one value is observed multiple times
        assert compute_entropy([7] * 30) == 0.0


class TestCrossEntropy:
    def test_cross_entropy_inaccurate_guesses(self):
        X = [1,1,1,1]
        Y = [1,2,3,4]
        cross_entropy = compute_cross_entropy(X, Y)
        assert cross_entropy == pytest.approx(1.3862943611198906)

    def test_cross_entropy_perfect_guesses(self):
        X = Y = [1,1,1,2,2,3]
        cross_entropy = compute_cross_entropy(X, Y)
        assert cross_entropy == pytest.approx(1.0114042647073516)
        # if X = Y, then cross entropy will be entropy of X
        assert cross_entropy == pytest.approx(compute_entropy(X))