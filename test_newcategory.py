import pytest
from record import Category

inputs = iter(['a', 'b'])

def fake_input(prompt):
    return next(inputs)

class TestCategory:
    def test_new_income_category(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)

        new_1 = Category(Category.income_category)
        assert new_1.new_category() == Category.income_category.append('a')

    def test_new_expense_category(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)

        new_2 = Category(Category.expense_category)
        assert new_2.new_category() == Category.expense_category.append('b')
        





    