from mrjob.job import MRJob
import re
from itertools import combinations

WORD = re.compile(r"[\w']+")

class CountAndPair(MRJob):

    def mapper(self, _, line):
        b_id, review = line.split('\t',1)
        b_id = b_id.strip('"').strip("'")
        words = WORD.findall(review)
        
        # require this many words in order to compute similarity
        if len(words) < 50:
            return

        word_counts = {}
        for word in words:
            if word not in word_counts.keys():
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        norm = 0.0    
        for count in word_counts.values():
            norm += count**2
        norm = norm**.5
        
        for word, count in word_counts.items():
            yield word, (b_id, count, norm)
        

    def reducer(self, word, values):
        for pair in combinations(values, 2):
            if pair[0][0] < pair[1][0]:
                yield (pair[0][0], pair[1][0]), (pair[0][1], pair[1][1], pair[0][2], pair[1][2])
            elif pair[0][0] > pair[1][0]:
                yield (pair[1][0], pair[0][0]), (pair[1][1], pair[0][1], pair[1][2], pair[0][2])
            else:
                pass

if __name__ == '__main__':
    CountAndPair.run()
