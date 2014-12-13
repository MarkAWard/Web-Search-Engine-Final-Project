from mrjob.job import MRJob

class TopSimilar(MRJob):

    def mapper(self, _, line):
        bus_pair, sim = line.split('\t', 1)
        bus = eval(bus_pair)
        similarity = eval(sim)
        yield bus[0], (similarity, bus[1]) 
        yield bus[1], (similarity, bus[0]) 

    def reducer(self, key, values):
        values = sorted(values, reverse=True)
        for i, value in enumerate(values):
            if i < 20:
                yield key, value
            else:
                return

if __name__ == '__main__':
    TopSimilar.run()
