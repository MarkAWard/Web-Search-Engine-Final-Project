from mrjob.job import MRJob
import json
from nltk.stem import PorterStemmer
import re
import string


stopwords = ["a","about","above","actual","after","again","against","all","also","alway","am","an","and","anoth","any","anyth","are","area","around","as","ask","at","b","back","be","because","been","before","being","below","between","both","but","by","c","came","can","come","could","d","day","did","didn","do","does","doing","don","down","during","e","each","els","enough","even","ever","everi","everyth","expect","f","feel","few","find","first","for","found","from","further","g","get","give","go","good","got","great","h","had","has","have","having","he","her","here","hers","herself","him","himself","his","how","i","if","im","in","into","is","isn","it","its","itself","j","just","k","know","l","let","like","ll","locat","look","lot","m","made","make","mani","me","more","most","much","my","myself","n","need","never","nice","no","nor","not","noth","now","o","of","off","ok","on","once","one","only","or","other","our","ours","ourselves","out","over","own","p","peopl","place","put","q","r","re","realli","right","s","said","same","say","see","seem","servic","she","should","sinc","so","some","someth","st","still","such","sure","t","take","tell","th","than","that","the","their","theirs","them","themselves","then","there","these","they","thing","think","this","those","though","thought","through","time","to","told","too","took","tri","two","u","under","until","up","us","use","usual","v","ve","very","w","want","was","wasn","way","we","well","went","were","what","when","where","which","while","who","whom","why","will","with","work","would","x","y","yet","you","your","yours","yourself","yourselves","z"]

CITY_IDS = ["RU7bd3h2f6pBlf8BfAyxGQ","CxYMVhOnWQuYaVv7wTAiAg","dPIsxsqE22IZ-R43NalT0g","N-urZV7AHwkI2oavPqJDtQ","gCaIfAJ93W6fvmKuasF6Xw","V92ePy2VVqDfy1RSsjKW6w","S_xSSU0IbNGFwOUTHFNtpA","qB8D8KlvcWfwoREPIICO1w","xcJa7SUk9rSQbxkErstfew","JdG5e8zfYTu6_P29lQ-Wig","-KedUrm_YGt2s4Q9p_Q6Mg","qXh_8dyoLpniX1pv5jquOA","7oC0qcOg-XSt4Xo1_u-9XA","rqn5hFLMJVHaQvfu2Czl5A","d1PfS_bozULtBY4PjF3D-w","-DpB583IrJuH1ehHu-U8sw","Sn6Urb4rcxLD1nFZibNdfQ","0ggseJ7x1t-I-I8GA6knjw","T-Ouo3opXRiUEyGoBT0aoA","OdJvpUlDXp3K-0pI_uNkoA","HepbklWPmInGoNOThnpc9w","Rii78kjj-488O-ehx3f6Jw","QtXP6bCfwJEvLoHjJb7mSg","JkAmtVX7OhCY2b9Fu6Hskw","rKMPry_7sf-OlRkI8T8NRw","ggjWK5GsZQyUmGNoZaqMFQ","_7CLb8wr3ZqJsD8w3nQsOw","KW5Cp3UOPy0KIK22lWRTxg","ZiDnZGOCsr9xBGEL9ihzjg","043WqIgVYVRdUItQ4wuKPw","39C414-SwTpyes-9lbqkLg","9HXjkcyjIVCFErU6SxQb9g","M1-3lbWDPV-crfnkapFMwg","b88HUwXarEDlFehKzaqzBg","Ol8v3U-v4gq7lN0iIXqvXw","H4b7mZm90HzNez-ISrtChw","vOryuuNyZcQDAtOgJ3hKCA","UE826ZlmmHHJ3Hctgph5qw","58C-JxSMV3h0rI4z8TH_TA","avdAlf9EVns62HrsjryVzg","Ctx6jhtPjAb1WgSaNoEieQ","DhABkJUEv-Lc6W_64BzB5g","lZ3MyBPz0zYtYoMDQfYAFg","QxuZGiHF3jnatCUmI41FmA","1WaWdqLrgukIW7qulq6YyA","_3J0oVaaH92_lK2EFw9nVA","oMHdyK71d1vu8ZuSebOYhQ","7rD52PKYYUpAQDSruT8UJA","bxLquGyUzzdC3f39QJMmYw","FPTTiCzjDgBTzcanfKXsDw","1mE7ch1NkhGxRn_BBZNZ1g","VlzeNUSkepYtIgYCkrqRbg","_Fcc8TK1sFQwRMLFLiPk-Q","1t0EXtIOoxEp0wflOQUKYw","qCeYjXM6N03MTsfQF6LREg","rjTNSM-3jMQskDt7or05gA","CcDtQxeDYlRAfZMGwqMZjA","WSV-t7fuDkvZonTC-MHbPw","zrbf71B_uiRy0Je0giyy0A","p0wzC9-sC7hVl3z8vyf3AQ","FumYAtwmfAo1d0X3GouTHQ","gqETlVKT3LIAL59WBoPBpQ","B2b37HiD0aJ6z1ehJHbn7w","_tmAs95FomIea9WFlZ0tKA","6qG0UnftcA8vPKbee4Qykg","NRLKGDi4LFg3RM-XAAoN-g","08KuvUqdONvE2YE9OGKqWQ","tqH8GZ_YSaMWNX53yFDzGw","I9akYRLLIBS1E74IqvCJlQ","LJzes4GfuyV-yd1JlD5q_A","SnQ-N-4is1mEpwSAW5JBBQ","Im68PoWLtYHB7AcxGfoM_A","OWEQazt83KlNT8ff6NI8rA","CFzuVLy94kslBW9QVqDRQQ","IiX7lGoQQE3T4wg_1cx8Og","jQEQQKOmCe0oTia-6F6Pyw","S9w52Y8f_nfv8QXuHmXBCg","BV7lzWCXot_NQaQ5YS9z7Q","B9zrN6gHO-rEweAjIVR0Xw","fsuLbcnnIFWG5rzy--9nzQ","35Q2qySgp_AxgkCde5e4HA","iiruNMRBWMdxqRtaVIMPkA","wTJXfjD-KfETh0ZU3iQqqQ","3Wr0o6qZfbUoP7mkl0zPoQ","RkqQC9cvFa12pCWn2leGig","ZEP2jzQPbGnN9Fma1UHyxQ","5dfcKD_krgVx5Gsn-pJxnw","_LEpQoZASqir0Xt_tOjFlg","IdVxb81jCBrcDRXIWsWlCg","P4HCpfpFYWLyCnYIowTjLQ","JLI7EJuxx7RcPNk4OToexA","f58dfOEnJ5FGZxp06xzcPw","2bDntAuAGSu9zFjOi3iMjg","Z6V6XF2q8qX5DInYYw17tA","le6N-lnGZVa-pbF1E_FTvA","tuKE5oN8bfpskD2AK-Qxbg","c3ePjP1yvNH_RUHSEF0WdQ","w-1y9XaoreYJAJHWhSskNg","YI4U5Qew95gxkbs_RjO89g","JTcPfVn5_N8yBt81SMNAsg","md_yYBbMi17XvSIVALlmnw","aRzFeBf-hUCr4dkNQl-P3g","-7r5-GDmuXsgRhkBnN0nqA","YnPF-O9PSpWOeR_GgoNlsQ","q9yRUhtTnlxTJPhTMrMWCg","QuuehfcNexJTr0HL6pnI2A","JB-h3X2TIxBWkS5d8uL5hQ","M8aBK5z7dLNovpIuKrCOEQ","R14P3D93zp_HIpNRxFoH9g","YgeONC66RHk3D5SQ5LTfCw","DVqGHtZlrUdRXZkeyGve5g","VUXzKET78wCT7c3pNJUnBw","lrVVpyP-aBRmP1I1KUqXkw","KQWMdG-7bhx2kNBdovnTZQ","rgnLzeRSrEUsB_9F9sBxSQ","YQQU-aIXy2cCJNaiennlPA","m7gm3-LVknB_Fi1jlN4V8w","IbOkRQ67dtiDms7wzrSBsw","KxqgKI9TODZ3Z1_lPoTf2w","kaiz7lD3qoC0ZJzGKQcr5A","sRO-U8Kxd1tXJlENTqv89A","z55ycyxaqyb_r8xd74Mdmg","tFW5YcoXnKz8xRA-l3gRWA","8SlAYQ4DY9rnUus6dSeEDw","_VbBmuNcK8Yxy4s_pBD88Q","QmZwgd6z71fUwNJ2JjZqvQ","mOzYqVBmTCkw_eHX2MytFQ","5lZ6vYXgDWjYC2DfUfiLuw","fz_qCpZo6WbystRINrtB3A","DG4CznrJTyjhDHbYDs-45A","a3-znGameOY1scTqN8ZWXg","sNSdmLIkozspIA1ljCexLw","I_KlxsoiTnsj6cmNc6eQnw","RPKnhndXvWHukeZ2e8stYQ","3U55OyOqWhEwCXNFoamcwg","nKuZ0Jc6DmheebEjbwPVow","LXXAXCEiU4nCM8wScorQHQ","tcYS47Ijoi8vQ1oyApMrCw","vQSm6zHwrmB45OZRgONUlA","3LhbvsAT7RxRrDx7nTFyfw","vTvNlqeHk4orSa7sSZFV1A","vi9aRAN7_0l-xe4envUEGw","orzW5LR9bwaOws0aOXvgHg","QVMxEWOGuoAlJxPrJzML3A","DJFc6K9ryUMRig7EpCh1SQ","APJAMnqQTFmK3EGQdY4Iig","A0e-tQr8h6nZ7a9VzZMgCg","ggT0ynhCLlp0eAahXdq8ug","jZsabhZHuC0aBX88qP53pg","5UWkbSgFRIOdevprXJqQMQ","I_08L_M6ojnbSz9HsX9aIg","adDbg0aDtqp2M0x9oLycVQ","V7mWLjizmQchGC9MsFPO7g","0tX2BR7qE-IP5Ne6vLwy3A","mWBXYrZYqQfV29-kgCmi8Q","fuuzSe_xGqXLIw7Jxw9RjA","epqJjZou4WhvNHm3YI0yaw","cdDzHuzov-q9UHXI9Mlh8g","WQkrz00jNyQsaJadxL0h7Q","54NNpmmHGyas53lS-hqzJQ","0jQI7AktAB-m_cg54wY0aw","d_6t_yby2f7GSao35ehj2g","VECkMLeBCIOIwGhXOIRuRw","gKT1bL4Vg9HuqZeG6povMQ","2faHaK3FPhfzFvJZ5i3U9w","-3RrTaKWnK4urj-uQm-WCQ","23XfD5YrEG1UzOZrfkjgLg","4YsbILBLlYEMXPjTvdHqIg","AosVp_67irlM1MzpgURciw","UEYeGewAHsCLA-OAFxKJ5A","gjyFpVijSZC6PUqnu8N7BQ","N7qZEvs_Pa1X1wMfX6M_KQ","2Ho61yyEnWGrqmCfkEj1mw","9LJ6vlJCgDm9UlxIbhyDTQ","NleyIwEmt2KfauXtFbTotg","ZUl4lCYWPxaR7TO4Neaksg","XtXFiaWnws4xnTMJq09Z6g","oWWgM052VB6TfQy8xkktog","2NzXwHM9fQRwk9_1SF-9eQ","ZwCv1b_rmbH8vagNTXKRFg","Q_KmjsAxmXEccFBvrsKN_g","84PwXNDAOVQL412Ft6vj9g","e5bI0nEjKHM6xYRc1hb3vA","WGWXwg2w0yRVxH6KJ1iTJg","op34GXVaKm0qeX6yUaRJGA","RndMM5Urxfq6uEai8O5r5Q","12gxJgqwSy1igK9bkB5WTw","rRYX3q9gbY2SBkUtAXYudA","Bht_AEe9C-6rr-5sx7-8bA","V63CGQ96PTNlz0xu3SIMtA","sYkhl-syFQ7ed0U8AZfpMg","Xq9D4UfBW5DLwSb7YorRQQ","6t7QHGG827TO5hDMSGDzug","0p8H5orIBw7Ba-a4czpzhA","kxm7ViD2p6oxgau0iNiS-w","0zhKgVmSsCVoFUY54tDibw","ohN09D6g0N0jd6Jc8uQntA","4chDWs-NneRmm-07Nx-AMg","gEe6HdLG4Z5F5gjVkTs9VA","zLUnxFzwPN9A5ZP87SGaTw","y0HShkC69tyeSU-Ej4jxtw","xaSUhHGkBBAjolDEuIXgPQ","vq6sVhb8b7EOxUbNTCnfOQ","3X_rVEwLz4mnto10U-oz5Q","bLXi6BOXI5esl1xoN7EvoA","W2Ykx9-dUYNp1tC_Km4Bbw","nF8R1_vtuVntHLpUN3UoVg","uAjMYZ0O0RAwxj3a2A7o0A","C7SLHJ0GY_cnhNqDM2jSGw","ebU8qtpevZnLqhhPfaX81Q","RXjTCrjDGRRlZa4GCMz26Q","sa7a1egGMO0OzowySsF73w","jX5tkA-gcacOGCZ8oZFrDA","G3UQvnx2axEZ_GVF_adM-w","HI2j56tbcCIGJv5xa4-jOA","aZ0spgQ-Hfr3j8OLbtQ8kQ","aJwYBAIxsNKHnrlHnEaQnQ","cqc7y_8KQgZopip-w3K6nQ","snV8jGHnoVWBNJyRUBJYug","MQ9PTbD-EFRUxhg0R5kjUw","5XeAKGGfH7q--cLN_lEJHQ","B_8DCETx7Wln1x9W2P7dLQ","TOPYl1iLjl2PRZA5m-6kiA","1WRP-fgtTrsBJ-HMifskqw","5_q-fa1Kdu7FWTyf1uVg0w","YZvXTxzycSpl0thbZbA62Q","bzP1utyRGu6ywPric5UmGg","kiBxQwgpaZ0HpILQE7Fevw","BgyCo15G_229xfSmNtPtXg","3IBqRg-FEdWq76orVrj-9g","7W_8BUSIx0xe0jwd3e0bIw","47S_Pz6gYMGYffTYKk_W5g","_e9wgMUWkkx_vrFt8Ym6SA","RheZUFyesPne28fwAtCVCw","cdDMyyoOUpJif9MwmLV61g","RCxVuW6VvrynfUAacGTiYg","rRmH0Shfb8hj_Tk0zFEOLg","Ea1zCmp6aZMXcIDOT7-7cA","5x-Xv-78fQ1-GAFFRX4sfg","atfGEO5rudh92GJbQ7GRcg","doLdEB3JJHmRMeNks-F_9w","hwCthMrt77pywJA7Q6T_9Q","VXua65ANlPYKtEBSmGp6CQ","cC8CA5khThM31VaCZRw7ZQ","atnFVYafrD79Zdsh8AWphQ","rw1OFTgmUHaBLK5EdftUIA","eYzNsTc9BXKIPP7FXx5kjg","i_N21-BF8Lj3ejHEldeWqA","WABk1j4RVf3TZMUSj_lnMw","bUOQz09aRLhDVV5Lg35o6w","SckGC6L6WimyM1JuwYEazw","RMWbG4ep_Zewr5pha0_nHQ","ekkrn8-splkvfLSeQBC2cw","QptaeWyVZICXodBFkvdLww","oUcSEppn7vWLWBNOghx9JA","AUSMuLQ8xBREb8WpanLz1Q","JkdZsw_ASWWPYIsA2W5fsQ","7xRhic2Jm9VnM9dZ1F-KJw","iPTU21Sdija7LxJ7vfwSng","CYgWv0-ru5qujLQscQgo4g","WStrQ_E3PJ3zGhJZXELN6A","nRAt8fJnvu10g4QK3e0VUA","SNnX5GqowAAXr22C3_kHnw","zzRe5dyYkWb6weQS4FdSQQ","JO8KgtiNJBM8FzcoPxKB9Q","fREIiIPMg6i9GR_ywHbUnQ","KbFb1n-RZd5HOn2q1qOD1A","8gg2BB7T0NOtjFXK7ROQ5Q","SZ-w-jLaSJocRtAQB2qDIA","a75FjNCtzBvpETX_Ur3N4w","EBOKlLXepUQImS8wV4068A","76ept0_vA0XbmKg8hO2udQ","rY7qwLnR-TPlkUYWN5rJew","VqhpCGRniGVfsfrQN_VnwA","NOU1Ht1hns0_aF8Zc_6O_Q","pdoNdba03NXOdhaDIFkKcg","35ww51JXCkobhdf6GhvEhw","1K4zYEVDxUtacLGdZU2nWw","zP9Bvpsm76lWrAgKAt5QaQ","pOe5JXmJVwzjtyJlhP6dVA","O-ZPOGlws9LznmNrSeniyg","c3bAq3DdF-sAugGJUMJXfQ","c8zOgLyDNaOZ4BHrnZyrqw","VCNHBlQSI4Qq71ifHDbYXw","NaxmyldPOv16inSmB3Y0xw","ybrkPt8Xy7o7ccyp0ZoWVw","o-FCuE8JQKDdHTaR6D_Sxg","Zk6ymf4JwJzc_qabW8RzBg","r38bIMzm5wWNq19mISncDA","0msAbcZIxbd0SNScpNaDkg","8V0qsdynqPesYpHrL725UQ","EmlrdmsvznKMVrafcFMzbg","D1_25rfl7k6vhTJc11OPoQ","bvMxonNAnFLYYyvpFAMfkQ","gvrYwDnpCncvXYklisyCew","VhpRKw2w_x3foU0x2k5EFw"]


PUNC = re.compile('[%s]' % re.escape(string.punctuation))
WORD = re.compile(r"[\w']+")
STOP = re.compile(r'\d+|[^\x00-\x7F]+|\b(' + r'|'.join(stopwords) + r')\b\s*')
PS = PorterStemmer()

class CityCleanAndJoinReviews(MRJob):
    
    def mapper(self, _, line):
        obj = json.loads(line)
        if obj["business_id"] in CITY_IDS:
            words = [PS.stem(w) for w in WORD.findall(STOP.sub('', PUNC.sub(' ', obj['text'].lower())))]
            yield obj['business_id'], ' '.join([word for word in words if word not in stopwords])

    def reducer(self, b_id, reviews):
        yield b_id, " ".join(reviews)

if __name__ == '__main__':
    CityCleanAndJoinReviews.run()
