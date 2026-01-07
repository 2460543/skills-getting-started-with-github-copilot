from collections import Counter
from typing import Iterable, List, Tuple, Optional, Dict, Any


class FrequencyCounter:
    """Simple frequency counter wrapper around collections.Counter.

    Supports optional case-insensitive counting for strings.
    """

    def __init__(self, iterable: Optional[Iterable] = None, case_sensitive: bool = True):
        self._case_sensitive = case_sensitive
        self._counter: Counter = Counter()
        if iterable is not None:
            self.update(iterable)

    def _norm(self, item: Any) -> Any:
        if isinstance(item, str) and not self._case_sensitive:
            return item.lower()
        return item

    def update(self, iterable: Iterable) -> None:
        for item in iterable:
            self._counter[self._norm(item)] += 1

    def counts(self) -> Dict[Any, int]:
        return dict(self._counter)

    def most_common(self, n: Optional[int] = None) -> List[Tuple[Any, int]]:
        return self._counter.most_common(n)

    def total(self) -> int:
        return sum(self._counter.values())

    def unique(self) -> int:
        return len(self._counter)


def count_frequency(iterable: Iterable, case_sensitive: bool = True) -> Dict[Any, int]:
    """Convenience function returning a plain dict of frequencies."""
    fc = FrequencyCounter(iterable, case_sensitive=case_sensitive)
    return fc.counts()


__all__ = ["FrequencyCounter", "count_frequency"]
