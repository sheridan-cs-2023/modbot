import random
import re


class Chain:

    def __init__(self):
        self._elements = {None: {}}
        self._previous = self._elements[None]

    def add(self, tokens):
        previous = self._elements[None]
        token_list = tokens
        token_list.append(None)

        for token in token_list:
            if token not in self._elements:
                self._elements[token] = {}

            if token not in previous:
                previous[token] = 0

            previous[token] += 1
            previous = self._elements[token]

    def generate(self, max_len=0):
        """Generate output from the chain, up to the length specified by 'max_len'. Note that the maximum length
        is approximate and might be exceeded by the length of a word."""
        output = []
        total_len = -1
        previous = None
        while (max_len is 0) or total_len <= max_len:
            if len(self._elements[previous]) > 0:
                result = random.choices(list(self._elements[previous].keys()), weights=self._elements[previous].values())
                previous = result[0]

                if previous is None:
                    return output

                output.append(result[0])
                total_len += len(result[0]) + 1
            else:
                return output
        return output
