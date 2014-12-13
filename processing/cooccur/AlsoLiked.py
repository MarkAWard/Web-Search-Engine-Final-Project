from mrjob.job import MRJob
from mrjob.step import MRStep
from itertools import combinations
import json

class AlsoLiked(MRJob):

    def map_user_biz(self, _, line):
        obj = json.loads(line)
        if obj["stars"] >= 3:
            yield obj["user_id"], obj["business_id"]
        
    def pair_businesses(self, user, values):
        for pair in combinations(values, 2):
            if pair[0] < pair[1]:
                yield (pair[0], pair[1]), 1
            elif pair[0] > pair[1]:
                yield (pair[1], pair[0]), 1
            else:
                pass

    def combine(self, pair, counts):
        yield pair, sum(counts)

    def output_each_biz(self, pair, counts):
        count = sum(counts)
        if count >= 10:
            yield pair[0], (count, pair[1])
            yield pair[1], (count, pair[0])

    def reduce_pairs(self, key, values):
        values = sorted(values, reverse=True)
        for i, value in enumerate(values):
            if i < 10:
                yield key, value
            else:
                return

    def steps(self):
        return [
            MRStep(mapper=self.map_user_biz,
                reducer=self.pair_businesses),
            MRStep(combiner=self.combine,
                reducer=self.output_each_biz),
            MRStep(reducer=self.reduce_pairs)
        ]

if __name__ == '__main__':
    AlsoLiked.run()
