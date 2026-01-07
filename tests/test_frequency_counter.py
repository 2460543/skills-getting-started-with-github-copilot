import pytest

from src.frequency_counter import FrequencyCounter, count_frequency


def test_basic_counts_case_insensitive():
    fc = FrequencyCounter("aabbcA", case_sensitive=False)
    assert fc.counts() == {"a": 3, "b": 2, "c": 1}
    assert fc.total() == 6
    assert fc.unique() == 3
    assert fc.most_common(2) == [("a", 3), ("b", 2)]


def test_count_frequency_helper():
    data = ["x", "y", "x", "z", "X"]
    d = count_frequency(data, case_sensitive=False)
    assert d == {"x": 3, "y": 1, "z": 1}
