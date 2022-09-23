import pytest
from goal import Comparison, balance

inputs = iter(['500', '709.83', 'goal'])

def fake_input(prompt):
    return next(inputs)

class TestInputGoal:
    def test_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        compare = Comparison(balance())
        assert compare.input_goal() == 500
        assert compare.input_goal() == 709.83

    def test_alphabets(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        compare = Comparison(balance())
        with pytest.raises(ValueError):
            compare.input_goal()
