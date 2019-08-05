# -*- coding: utf-8 -*-
# pylint: disable=C0321,C0111,C0103,R0903

from .util import n_gram


class AiMySearch():
    class MatchRateError(Exception):
        pass

    class TargetTextError(Exception):
        pass

    def __init__(self, search_target_word, target_text, fuzziness=0, match_rate=0.6):
        self.search_target_word = search_target_word
        if not target_text:
            raise self.TargetTextError('target_text should not be blank.')
        self.target_text = target_text
        self.fuzziness = fuzziness
        if not 0 < match_rate < 1:
            raise self.MatchRateError('match_rate should be between 0 and 1.')
        self.threshold = match_rate * len(search_target_word)

    def run(self):
        candidates = []
        for n_gram_num in list(range(
                len(self.search_target_word) - self.fuzziness,
                len(self.search_target_word) + self.fuzziness + 1)):
            for target_elm in n_gram(self.target_text, n_gram_num):
                count = 0
                if target_elm['text'] == self.search_target_word:
                    continue
                for t in target_elm['text']:
                    if t in self.search_target_word:
                        count += 1
                if count >= self.threshold:
                    candidates.append(target_elm)

        filtered = []
        sorted_candidates = sorted(candidates, key=lambda x: x['index'])

        for candidate in sorted_candidates:
            if not filtered:
                filtered.append(candidate)
            if filtered:
                last_elm = filtered[len(filtered)-1]
                last = last_elm["index"] + last_elm["length"]
                if candidate['index'] - last > 0:
                    filtered.append(candidate)
                else:
                    l = candidate['index'] - last_elm['index']
                    last_elm['text'] = last_elm['text'][0:l] + \
                        candidate['text']
                    last_elm['length'] = len(last_elm['text'])

        return list(filter(lambda x: self.search_target_word not in x['text'], filtered))
