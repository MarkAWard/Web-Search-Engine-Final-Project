from mrjob.job import MRJob

class ComputeSimilarity(MRJob):

    def mapper(self, _, line):
        bus_pair, count_pair = line.split('\t', 1)
        bus = eval(bus_pair)
        counts = eval(count_pair)
        yield bus, counts 

    def reducer(self, key, values):
        num = 0
        for counts in values:
            num += counts[0] * counts[1]
        yield key, float(num) / float(counts[2] * counts[3])

if __name__ == '__main__':
    ComputeSimilarity.run()
