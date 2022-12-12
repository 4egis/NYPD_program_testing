from homework import take_from_list, calculate
import pytest
import os
import json


@pytest.mark.parametrize(
    "li,indices",
    [([0, 1, 2, 3], [1.0, 2.0, 3.0]), ([1, 2, 3], ['a', 'b']), ([5, 4, 3, 2], 'as')]
)
def test_take_from_list_ValueError(li, indices):
    with pytest.raises(ValueError, match="Indices should be integer or list of integers"):
        take_from_list(li, indices)


@pytest.mark.parametrize(
    "li,indices",
    [([0, 1, 2, 3], 5), ([], 0), ([5, 4, 3, 2], [1, 2, 3, 4])]
)
def test_take_from_list_IndexError(li, indices):
    with pytest.raises(IndexError, match="is to big for list of length"):
        take_from_list(li, indices)

@pytest.mark.parametrize(
    "li,indices,answ",
    [([0, 1, 2, 3], 2, [2]),
     ([], [], []),
     ([5, 4, 3, 2], [1, 3], [4, 2]),
     ('asdf', [0, 0, 0, 1], ['a', 'a', 'a', 's']),
     ([[1, 2, 3, 4], [4, 3, 2, 1]], [1], [[4, 3, 2, 1]]),
     ([[],[],[],[]], [1, 2], [[],[]]),
     ([0, 1, 2, 'asd', [[[0], [1]], 1]], [-1, -2, -4], [[[[0], [1]], 1], 'asd', 1])]
)
def test_take_from_list_return(li, indices, answ):
    assert take_from_list(li, indices) == answ


current_dir = os.path.dirname(__file__)
in_file = os.path.join(current_dir, "input.json")
out_file = os.path.join(current_dir, "output.json")

@pytest.mark.skipif(not os.path.exists(in_file), reason="Missing input file")
def test_calculate():
    calculate(in_file, out_file)
    assert os.path.exists(out_file)
    with open(out_file, 'r') as f_p:
        data = json.load(f_p)
        assert data == [81, 62, 78, 67, 89, 33, 106, 126, 112, 20, 56, 128, 106, 3, 107]


def test_calculate_wrong_in_file():
    in_file = os.path.join(current_dir, "asd.json")
    with pytest.raises(FileNotFoundError):
        calculate(in_file, out_file)


