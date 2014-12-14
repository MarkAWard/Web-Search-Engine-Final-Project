Web-Search-Engine-Final-Project
===============================

To Do:
-----
1. ~~Remove false attributes~~
2. Try QL for ranker
3. ~~Handle canada UK zip codes~~
4. Evaluation
  * Baseline, purely cosine similarity
  * Multiple rankers, comprehensive
  * Rank with category features and Title features
  * Rank with/without repetition of text 
5. Stemming
  * ~~Handle "goooooood"~~
  * ~~Handle accented characters~~
6. Category expansion. Medical -> Medical, Doctor etc
4. Query log
5. Front End
  * ~~Google Maps~~
  * ~~GPS~~
  * Autocomplete
  * Integrate similar businesses
  * Integrate users also liked
6. Similarities / Also Liked
  * ~~AZ, NYC, NJ, Boston, Amherst~~
  * Clean files ``` sed 's/"\|,\|\[\|\]//g' ```
  * Create index to store these
  * Query for business: return business, similars, and users also liked 
