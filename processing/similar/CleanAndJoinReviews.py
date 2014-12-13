from mrjob.job import MRJob
import json
from nltk.stem import PorterStemmer
import re
import string


stopwords = ["a","about","above","actual","after","again","against","all","also","alway","am","an","and","anoth","any","anyth","are","area","around","as","ask","at","b","back","be","because","been","before","being","below","between","both","but","by","c","came","can","come","could","d","day","did","didn","do","does","doing","don","down","during","e","each","els","enough","even","ever","everi","everyth","expect","f","feel","few","find","first","for","found","from","further","g","get","give","go","good","got","great","h","had","has","have","having","he","her","here","hers","herself","him","himself","his","how","i","if","im","in","into","is","isn","it","its","itself","j","just","k","know","l","let","like","ll","locat","look","lot","m","made","make","mani","me","more","most","much","my","myself","n","need","never","nice","no","nor","not","noth","now","o","of","off","ok","on","once","one","only","or","other","our","ours","ourselves","out","over","own","p","peopl","place","put","q","r","re","realli","right","s","said","same","say","see","seem","servic","she","should","sinc","so","some","someth","st","still","such","sure","t","take","tell","th","than","that","the","their","theirs","them","themselves","then","there","these","they","thing","think","this","those","though","thought","through","time","to","told","too","took","tri","two","u","under","until","up","us","use","usual","v","ve","very","w","want","was","wasn","way","we","well","went","were","what","when","where","which","while","who","whom","why","will","with","work","would","x","y","yet","you","your","yours","yourself","yourselves","z"]

PUNC = re.compile('[%s]' % re.escape(string.punctuation))
WORD = re.compile(r"[\w']+")
STOP = re.compile(r'\d+|[^\x00-\x7F]+|\b(' + r'|'.join(stopwords) + r')\b\s*')
PS = PorterStemmer()

class CleanAndJoinReviews(MRJob):

    def mapper(self, _, line):
        obj = json.loads(line)
        words = [PS.stem(w) for w in WORD.findall(STOP.sub('', PUNC.sub(' ', obj['text'].lower())))]
        yield obj['business_id'], ' '.join([word for word in words if word not in stopwords])

    def reducer(self, b_id, reviews):
        yield b_id, " ".join(reviews)

if __name__ == '__main__':
    CleanAndJoinReviews.run()
