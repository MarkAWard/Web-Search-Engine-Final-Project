package edu.nyu.cs.cs2580;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Vector;
import java.util.Comparator;

import edu.nyu.cs.cs2580.QueryHandler.CgiArguments;
import edu.nyu.cs.cs2580.SearchEngine.Options;
import edu.nyu.cs.cs2580.IndexerInvertedCompressed.Tuple;

/**
 * @CS2580: Implement this class for HW3 based on your {@code RankerFavorite}
 * from HW2. The new Ranker should now combine both term features and the
 * document-level features including the PageRank and the NumViews. 
 */
public class RankerComprehensive extends Ranker {

	public RankerComprehensive(Options options,
		CgiArguments arguments, Indexer indexer) {
		super(options, arguments, indexer);
		System.out.println("Using Ranker: " + this.getClass().getSimpleName());
	}

	@Override
	public Vector<ScoredDocument> runQuery(Query query, int numResults, double latitude, double longitude) {

		Vector<ScoredDocument> all = new Vector<ScoredDocument>();


		QueryPhrase qp=new QueryPhrase(query._raw);
		qp.processQuery();


		Document i = _indexer.nextDoc(query, -1);	    
		Double pos;
		int j;

		while(i != null) {

			if(qp.phrase.size()>0) {

				for(j=0;j<qp.phrase.size();j++) {
					pos=_indexer.NextPhrase(qp.phrase.get(j), i._docid, -1);
				//if (pos != Double.POSITIVE_INFINITY)
	  				//System.out.println( "Position: " + pos+ " Docid: " + i._docid + " Docname: " + i.getTitle() );
					if(pos==Double.POSITIVE_INFINITY)
						break;
				}

				if(j==qp.phrase.size())
					all.add(scoreDocument(query, i, latitude, longitude));
			}
			else {
	  		//System.out.println(  " Docid: " + i._docid + " Docname: " + i.getTitle() );	
				all.add(scoreDocument(query, i, latitude, longitude));	
			}

			i = _indexer.nextDoc(query,i._docid);
		}

		// sort all return results
		Collections.sort(all, Collections.reverseOrder());

		System.out.println("--------");
	//Collections.sort(all, Collections.reverseOrder());
		System.out.println("Printing from Ranker Comprehensive.java");
		System.out.println("Sorting based on cosine, title, categories, and distance");
		System.out.println("Number of Reviews of Top Docs retrieved");
		for (int j2 = 0; j2 < all.size() && j2 < numResults*2; ++j2)
		{
			ScoredDocument d  = all.get(j2);
			System.out.println(" Doc: " + d.get_doc().getTitle() + " Distance: " + d.get_distance() + " Score: " + d.get_score());
		}



		// rerank(all, latitude, longitude);
		// Collections.sort(all, Collections.reverseOrder());


		// System.out.println("--------------");
		// System.out.println("Sorting on reviews+stars+location, Using top 100 documents instead of 50 (Used in Ass3)");
		// System.out.println("Number of Reviews for the sorted set");

		// for (int j3 = 0; j3 < all.size() && j3 < numResults; ++j3)
		// {
		// 	ScoredDocument d  = all.get(j3);
		// 	System.out.println(" Doc " + d.get_doc().getTitle() + " Reviews " +d.get_doc().get_num_Reviews());
		// }

		Vector<ScoredDocument> results = new Vector<ScoredDocument>();    
		for (int j1 = 0; j1 < all.size() && j1 < numResults; ++j1)
			results.add(all.get(j1));

		return results;
	}


	private ScoredDocument scoreDocument(Query query, Document document, double latitude, double longitude) {
		double distance_score = runquery_distance(document, latitude, longitude);
		if (distance_score > 100.0) return new ScoredDocument(document, (25.0 / distance_score), distance_score);

		double title_score = runquery_title(query, document);
		double cosine_score = runquery_cosine(query, document);
		double category_score = runquery_categories(query, document);

		// inflate score if within 25 miles else decrease score
		double score = (title_score + cosine_score + category_score) * (25.0 / distance_score);
		return new ScoredDocument(document, score, distance_score);
	}

	private double runquery_title(Query query, Document doc) {
		String title = doc.getTitle();
		Vector<String> titleTokens = new Vector<String>( Arrays.asList(title.split(" ")) );    
		double size = (double) query._tokens.size();
		titleTokens.retainAll(query._tokens); 
		double score = titleTokens.size() / size;

		return score;
	}


	private double runquery_categories(Query query, Document doc) {
		double score = 0.0;
		double size = (double) query._tokens.size();
		Vector<String> categories = doc.get_categories();
		Vector<String> cat_tokens = null;
		for(String cats : categories) {
			cat_tokens = new Vector<String>(Arrays.asList(cats.split(" ")));
			cat_tokens.retainAll(query._tokens);
			score += cat_tokens.size();
		}
		cat_tokens = null;
		return score/size;
	}

	private double runquery_cosine(Query query, Document doc) {
		double score = 0.0;

		if (_options._indexerType.equals("inverted-doconly")) {
			for (String queryToken : query._tokens) {
				int idx = ((IndexerInvertedDoconly) _indexer).getTerm(queryToken);
				if (idx >= 0 ) 
					score += ((DocumentIndexed) doc).getTFIDF(idx);
			}
		} else {
		// total number of docs, from indexer
			int num_docs = _indexer.numDocs();
			for (String queryToken : query._tokens){

		    // number of occurrences of this term, from postings list
				int tf = _indexer.documentTermFrequency(queryToken, Integer.toString(doc._docid) );
		    // number of docs word is in, from indexer
				int df = _indexer.corpusDocFrequencyByTerm(queryToken);

				double idf = ( 1 + Math.log( (double) num_docs/df ) / Math.log(2) );
				score += tf * idf;

		   // System.out.println(queryToken + ' ' + tf + ' ' + df + ' ' + idf + ' ' + score);
			}
			score = Math.log(score);
		}   
		return score;
	}


	private double runquery_distance(Document doc, double latitude, double longitude) {
		return distance(doc.get_lati(), doc.get_longi(), latitude, longitude);
	}


	private void rerank(Vector<ScoredDocument> orig_ranks, double latitudes, double longitudes) {

		ArrayList<Tuple<ScoredDocument, Double>> numviews_tuples = new ArrayList<Tuple<ScoredDocument, Double>>();
		ArrayList<Tuple<ScoredDocument, Double>> stars_tuples = new ArrayList<Tuple<ScoredDocument, Double>>();
		ArrayList<Tuple<ScoredDocument, Double>> locs_tuples = new ArrayList<Tuple<ScoredDocument, Double>>();
    // rerank the top 50 documents
		for (int i = 0; i < orig_ranks.size(); i++) {
			ScoredDocument sdoc = orig_ranks.get(i);
			stars_tuples.add(new Tuple<ScoredDocument, Double>(sdoc, sdoc.get_doc().get_stars()));
			numviews_tuples.add(new Tuple<ScoredDocument, Double>(sdoc, (double) sdoc.get_doc().get_num_Reviews()));
			locs_tuples.add(new Tuple<ScoredDocument, Double>(sdoc, (double) sdoc.get_doc().get_lati()));
		}

		Comparator< Tuple<ScoredDocument, Double>> comparator = new Comparator<Tuple<ScoredDocument, Double>>() {
			public int compare(Tuple<ScoredDocument, Double>tupleA, Tuple<ScoredDocument, Double> tupleB) {
        // tupleB then tuple A to do descending order
				return tupleB.getSecond().compareTo(tupleA.getSecond());
			}
		};
		Collections.sort(numviews_tuples, comparator);

		for (int i = 0; i < numviews_tuples.size(); i++) {
			ScoredDocument sdoc2 = numviews_tuples.get(i).getFirst();
			ScoredDocument sdoc1 = stars_tuples.get(i).getFirst();
			ScoredDocument sdoc3 = locs_tuples.get(i).getFirst();
			double score, lats, longs;
			double score1, s, locs;
			if (isBetween(i, 0, 9)){
				score = 1;
			} else if (isBetween(i, 10,19)) {
				score = 0.8;
			} else if (isBetween(i, 20,29)) {
				score = 0.6;
			} else if (isBetween(i, 30,39)) {
				score = 0.4;        
			} else if (isBetween(i, 40, 49)) {
				score = 0.2;
			} else {
				score = 0.1;
			}

			lats = locs_tuples.get(i).getFirst().get_doc().get_lati();
			longs = locs_tuples.get(i).getFirst().get_doc().get_longi();

			double latDiff = lats - latitudes;
			double longDiff = longs - longitudes;
			double latSqr = Math.pow(latDiff,2);
			double longSqr = Math.pow(longDiff,2);

			locs = -1 * Math.sqrt(latSqr + longSqr);


      //System.out.println(locs); 
			s = stars_tuples.get(i).getSecond();
			sdoc1.updateScore(s);
			sdoc2.updateScore(score);
			sdoc3.updateScore(locs);
		}


	}

	private boolean isBetween(int x, int lower, int upper) {
		return lower <= x && x <= upper;
	}

	
	private double isThere(String s, Vector<String> C)
	{   Vector<String> catTokens = new Vector<String>();
		double val = 0;
		for (int j = 0; j < C.size(); j++)
		{
			String c = C.get(j);
			catTokens = (Vector <String>) ( Arrays.asList(c.toLowerCase().split(" ")) );
			if (catTokens.contains(s.toLowerCase()))
			{
				val = 1;
			}
		}
		return val;
	}
	

	// calculate haversine distance in miles
    private double distance(double lat1, double lon1, double lat2, double lon2) {
    	double R = 3959; // In miles
        double dLat = Math.toRadians(lat2 - lat1);
        double dLon = Math.toRadians(lon2 - lon1);
        lat1 = Math.toRadians(lat1);
        lat2 = Math.toRadians(lat2);
 
        double a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.sin(dLon / 2) * Math.sin(dLon / 2) * Math.cos(lat1) * Math.cos(lat2);
        double c = 2 * Math.asin(Math.sqrt(a));
        return R * c;
    }


}

