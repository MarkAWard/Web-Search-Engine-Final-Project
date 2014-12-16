package edu.nyu.cs.cs2580;

import com.google.common.collect.HashBiMap;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Vector;

import edu.nyu.cs.cs2580.IndexerInvertedCompressed.Tuple;
import edu.nyu.cs.cs2580.QueryHandler.CgiArguments;
import edu.nyu.cs.cs2580.SearchEngine.Options;

/**
 * @CS2580: Implement this class for HW3 based on your {@code RankerFavorite}
 *          from HW2. The new Ranker should now combine both term features and
 *          the document-level features including the PageRank and the NumViews.
 */
public class RankerComprehensive extends Ranker {

	private ReadCorpus Cleaner = new ReadCorpus();
	public HashBiMap<String, Integer> dictionary = null;

	public RankerComprehensive(Options options, CgiArguments arguments,
			Indexer indexer) {
		super(options, arguments, indexer);
		System.out.println("Using Ranker: " + this.getClass().getSimpleName());
		dictionary = indexer.getDict();
	}

	@Override
	public Vector<ScoredDocument> runQuery(Query query, int numResults,
			double latitude, double longitude, Boolean findsim) {

		Vector<ScoredDocument> all = new Vector<ScoredDocument>();

		QueryPhrase qp = new QueryPhrase(query._raw);
		qp.processQuery();

		for(String term : query._tokens) {
			if(!dictionary.containsKey(term))
				query._tokens.remove(term);
		}
		if (query._tokens.size() == 0) {
			return NoResults();
		}	

		Document i = _indexer.nextDoc(query, -1);
		Double pos;
		int j;

		while (i != null) {

			if (qp.phrase.size() > 0) {

				for (j = 0; j < qp.phrase.size(); j++) {
					pos = _indexer.NextPhrase(qp.phrase.get(j), i._docid, -1);
					// if (pos != Double.POSITIVE_INFINITY)
					// System.out.println( "Position: " + pos+ " Docid: " +
					// i._docid + " Docname: " + i.getTitle() );
					if (pos == Double.POSITIVE_INFINITY)
						break;
				}

				if (j == qp.phrase.size()) {
					ScoredDocument s_doc = scoreDocument(query, i, findsim);
					if (s_doc.get_score() != 0.0)
						all.add(s_doc);

				}
			} else {
				// System.out.println( " Docid: " + i._docid + " Docname: " +
				// i.getTitle() );
				ScoredDocument s_doc = scoreDocument(query, i, findsim);
				if (s_doc.get_score() != 0.0)
					all.add(s_doc);
			}

			i = _indexer.nextDoc(query, i._docid);
		}

		// sort all return results
		Collections.sort(all, Collections.reverseOrder());

		// keep top 100 most relevent
		if (all.size() > 100)
			all.subList(100, all.size()).clear();

		// multiply in reciprocal distance
		rerank(all, latitude, longitude, findsim);
		Collections.sort(all, Collections.reverseOrder());

		System.out.println("--------");
		// Collections.sort(all, Collections.reverseOrder());
		System.out.println("Printing from Ranker Comprehensive.java");
		System.out
				.println("Sorting based on cosine, title, categories, and distance");
		System.out.println("Number of Reviews of Top Docs retrieved");
		for (int j2 = 0; j2 < all.size() && j2 < numResults * 2; ++j2) {
			ScoredDocument d = all.get(j2);
			System.out.println(" Doc: " + d.get_doc().getTitle() + " MILES: "
					+ d.get_distance() + " COSINE: " + d.get_cosine()
					+ " TITLE: " + d.get_title() + " CATEGORY: "
					+ d.get_category() + " SCORE: " + d.get_score());
		}

		// Collections.sort(all, Collections.reverseOrder());

		// System.out.println("--------------");
		// System.out.println("Sorting on reviews+stars+location, Using top 100 documents instead of 50 (Used in Ass3)");
		// System.out.println("Number of Reviews for the sorted set");

		// for (int j3 = 0; j3 < all.size() && j3 < numResults; ++j3)
		// {
		// ScoredDocument d = all.get(j3);
		// System.out.println(" Doc " + d.get_doc().getTitle() + " Reviews "
		// +d.get_doc().get_num_Reviews());
		// }

		if (findsim) {
			int all_size = all.size();
			for (int k = 0; k < all_size; k++) {
				Vector<Tuple<Double, Integer>> sim_docs = _indexer
						.get_similardoc(all.get(k).get_doc()._docid);
				if (sim_docs != null) {
					for (int l = 0; l < sim_docs.size() && l < 10; l++) {
						Document d;
						d = _indexer.getDoc(sim_docs.get(l).getSecond());
						all.add(scoreDocument(query, d, findsim));
					}
				} else {
					all.remove(k);
				}
			}

		}

		Vector<ScoredDocument> results = new Vector<ScoredDocument>();
		for (int j1 = 0; j1 < all.size() && j1 < numResults; ++j1)
			results.add(all.get(j1));

		if (results.size() == 0) {
			return NoResults();
		} else {
			return results;
		}
	}

	private ScoredDocument scoreDocument(Query query, Document document,
			Boolean findsim) {
		double title_score = runquery_title(query, document);

		if (title_score == 1.0 && findsim) {
			double score = (_options._titw * title_score);
			ScoredDocument sdoc = new ScoredDocument(document, score);
			sdoc.set_title(title_score);
			return sdoc;
		}

		else if (!findsim) {
			double cosine_score = runquery_cosine(query, document);
			double category_score = runquery_categories(query, document);

			double score = (_options._titw * title_score + _options._cosw
					* cosine_score + _options._catw * category_score);
			ScoredDocument sdoc = new ScoredDocument(document, score);

			sdoc.set_title(title_score);
			sdoc.set_cosine(cosine_score);
			sdoc.set_category(category_score);

			return sdoc;
		}

		return new ScoredDocument(document, 0.0);
	}

	private double runquery_title(Query query, Document doc) {
		String title = doc.getTitle();
		try {
			title = Cleaner.cleanAndStem(title);
		} catch (IOException e) {
			System.err.println("Could not clean query: " + e.getMessage());
		}

		// Vector<String> titleTokens = new Vector<String>(
		// Arrays.asList(title.split(" ")) );
		// double size = (double) query._tokens.size();
		// titleTokens.retainAll(query._tokens);
		// double score = titleTokens.size() / size;

		Vector<String> queryTokens = new Vector<String>();
		queryTokens.addAll(query._tokens);
		Vector<String> titleTokens = new Vector<String>(Arrays.asList(title
				.split(" ")));
		double size = (double) titleTokens.size();
		queryTokens.retainAll(titleTokens);
		double score = queryTokens.size() / size;

		return score;
	}

	private double runquery_categories(Query query, Document doc) {
		double score = 0.0;
		Vector<String> categories = doc.get_categories();
		Vector<String> cat_tokens = null;
		for (String cats : categories) {
			try {
				cats = Cleaner.cleanAndStem(cats);
			} catch (IOException e) {
				System.err.println("Could not clean query: " + e.getMessage());
			}
			cat_tokens = new Vector<String>(Arrays.asList(cats.split(" ")));
			cat_tokens.retainAll(query._tokens);
			score += cat_tokens.size();
		}
		cat_tokens = null;
		return score;
	}

	private double runquery_cosine(Query query, Document doc) {
		double score = 0.0;

		if (_options._indexerType.equals("inverted-doconly")) {
			for (String queryToken : query._tokens) {
				int idx = ((IndexerInvertedDoconly) _indexer)
						.getTerm(queryToken);
				if (idx >= 0)
					score += ((DocumentIndexed) doc).getTFIDF(idx);
			}
		} else {
			// total number of docs, from indexer
			int num_docs = _indexer.numDocs();
			for (String queryToken : query._tokens) {

				// number of occurrences of this term, from postings list
				int tf = _indexer.documentTermFrequency(queryToken,
						Integer.toString(doc._docid));
				// number of docs word is in, from indexer
				int df = _indexer.corpusDocFrequencyByTerm(queryToken);

				double idf = (1 + Math.log((double) num_docs / df)
						/ Math.log(2));
				score += tf * idf;

				// System.out.println(queryToken + ' ' + tf + ' ' + df + ' ' +
				// idf + ' ' + score);
			}
			score = Math.log(score);
		}
		return score;
	}

	// private double runquery_distance(Document doc, double latitude, double
	// longitude) {
	// return distance(doc.get_lati(), doc.get_longi(), latitude, longitude);
	// }

	private void rerank(Vector<ScoredDocument> orig_ranks, double latitude,
			double longitude, Boolean _nearmes) {

		// ArrayList<Tuple<ScoredDocument, Double>> locs_tuples = new
		// ArrayList<Tuple<ScoredDocument, Double>>();

		// rerank the top 50 documents
		for (int i = 0; i < orig_ranks.size(); i++) {
			ScoredDocument sdoc = orig_ranks.get(i);
			double distance = distance(sdoc.get_doc().get_lati(), sdoc
					.get_doc().get_longi(), latitude, longitude);
			sdoc.set_distance(distance);
			sdoc.updateScore(1.0 / distance);
			// locs_tuples.add(new Tuple<ScoredDocument, Double>(sdoc,
			// distance));
		}

	}


	// calculate haversine distance in miles
	private double distance(double lat1, double lon1, double lat2, double lon2) {
		double R = 3959; // In miles
		double dLat = Math.toRadians(lat2 - lat1);
		double dLon = Math.toRadians(lon2 - lon1);
		lat1 = Math.toRadians(lat1);
		lat2 = Math.toRadians(lat2);

		double a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.sin(dLon / 2)
				* Math.sin(dLon / 2) * Math.cos(lat1) * Math.cos(lat2);
		double c = 2 * Math.asin(Math.sqrt(a));
		return R * c;
	}

	private Vector<ScoredDocument> NoResults() {
		Vector<ScoredDocument> none = new Vector<ScoredDocument>();
		none.add(new ScoredDocument());
		return none;
	}

}
