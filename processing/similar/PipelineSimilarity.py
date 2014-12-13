from mrjob.job import MRJob
from mrjob.step import MRStep
import re
from itertools import combinations

WORD = re.compile(r"[\w']+")

class PipelineSimilarity(MRJob):

    def count_words(self, _, line):
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
        
    def pair_businesses(self, word, values):
        for pair in combinations(values, 2):
            if pair[0][0] < pair[1][0]:
                yield (pair[0][0], pair[1][0]), (pair[0][1], pair[1][1], pair[0][2], pair[1][2])
            elif pair[0][0] > pair[1][0]:
                yield (pair[1][0], pair[0][0]), (pair[1][1], pair[0][1], pair[1][2], pair[0][2])
            else:
                pass

    def cosine_similarity(self, key, values):
        num = 0
        for counts in values:
            num += counts[0] * counts[1]
        yield key, float(num) / float(counts[2] * counts[3])

    def map_similar(self, bus, similarity):
        yield bus[0], (similarity, bus[1]) 
        yield bus[1], (similarity, bus[0]) 

    def reduce_similar(self, key, values):
        values = sorted(values, reverse=True)
        for i, value in enumerate(values):
            if i < 20:
                yield key, value
            else:
                return

    def steps(self):
        return [
            MRStep(mapper=self.count_words,
                reducer=self.pair_businesses),
            MRStep(reducer=self.cosine_similarity),
            MRStep(mapper=self.map_similar,
                reducer=self.reduce_similar)
        ]

if __name__ == '__main__':
    PipelineSimilarity.run()
