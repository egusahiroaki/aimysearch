# -*- coding: utf-8 -*-


class AiMySearch():
    class MatchRateError(Exception):
        pass

    def __init__(self, search_target_word, target_text, fuzziness=0, match_rate=0.6):
        self.search_target_word = search_target_word
        self.target_text = target_text
        self.fuzziness = fuzziness
        if not (match_rate > 0 and match_rate < 1):
            raise self.MatchRateError('match_rate should be between 0 and 1.')
        self.threshold = match_rate * len(search_target_word)

    def n_gram(self, target, n):
        return [{"text": target[index:index + n], "index": index, "length": n} for index in range(len(target) - n + 1)]

    def run(self):
        search_target_word = self.search_target_word
        target_text = self.target_text

        candidates = []
        for n_gram_num in list(range(len(search_target_word) - self.fuzziness, len(search_target_word) + self.fuzziness + 1)):
            for target_elm in self.n_gram(target_text, n_gram_num):
                count = 0
                if target_elm['text'] == search_target_word:
                    continue
                for t in target_elm['text']:
                    if t in search_target_word:
                        count += 1
                if count >= self.threshold:
                    candidates.append(target_elm)

        filtered = []
        sorted_candidates = sorted(candidates, key=lambda x: x['index'])

        for candidate in sorted_candidates:
            if len(filtered) == 0:
                filtered.append(candidate)
            if len(filtered) > 0:
                last_elm = filtered[len(filtered)-1]
                last = last_elm["index"] + last_elm["length"]
                if candidate['index'] - last > 0:
                    filtered.append(candidate)
                else:
                    l = candidate['index'] - last_elm['index']
                    last_elm['text'] = last_elm['text'][0:l] + \
                        candidate['text']

        return list(filter(lambda x: search_target_word not in x['text'], filtered))
