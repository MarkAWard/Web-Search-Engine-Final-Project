package edu.nyu.cs.cs2580;

import java.io.Serializable;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashSet;
import java.util.Set;
import java.util.Vector;

/**
 * The basic implementation of a Document. Only the most basic information are
 * maintained in this class. Subclass should implement additional information
 * for display or ranking, such as snippet, term vectors, anchors, etc.
 * 
 * In HW1: instructors provide {@link DocumentFull}.
 * 
 * In HW2: students must implement the more efficient {@link DocumentIndexed}.
 * 
 * In HW3: students must incorporate the PageRank and NumViews based on corpus
 * and log analyses.
 * 
 * @author fdiaz
 * @author congyu
 */
class Document implements Serializable {
	private static final long serialVersionUID = -539495106357836976L;

	/**
	 * A simple checker to see if a given document is present in our corpus.
	 * This is provided for illustration only.
	 */
	public static class HeuristicDocumentChecker {
		private static MessageDigest MD = null;

		private Set<BigInteger> _docsInCorpus = null;

		public HeuristicDocumentChecker() throws NoSuchAlgorithmException {
			if (MD == null) {
				MD = MessageDigest.getInstance("MD5");
			}
			_docsInCorpus = new HashSet<BigInteger>();
		}

		public void addDoc(String name) {
			if (MD != null) {
				_docsInCorpus.add(new BigInteger(MD.digest(name.getBytes())));
			}
		}

		public int getNumDocs() {
			return _docsInCorpus.size();
		}

		public boolean checkDoc(String name) {
			if (MD == null) {
				return false;
			}
			return _docsInCorpus.contains(new BigInteger(MD.digest(name
					.getBytes())));
		}
	}

	public int _docid;

	// Basic information for display
	private String _title = "";
	private String _url = "";

	// Basic information for ranking
	private Double _pageRank = 0.0;
	private int _numViews = 0;

	private String _business_id = "";
	private Double _lati = 0.0;
	private Double _longi = 0.0;
	private String _address = "";
	private Double _stars = 0.0;
	private String _zip = "";
	private String _city = "";
	private Vector<String> _categories = new Vector<String>();
	private Integer _num_Reviews=0;

	public Document(int docid) {
		_docid = docid;
	}

	public String getTitle() {
		return _title;
	}

	public void setTitle(String title) {
		this._title = title;
	}

	public String getUrl() {
		return _url;
	}

	public void setUrl(String url) {
		this._url = url;
	}

	public Double getPageRank() {
		return _pageRank;
	}

	public void setPageRank(Double pageRank) {
		this._pageRank = pageRank;
	}

	public int getNumViews() {
		return _numViews;
	}

	public void setNumViews(int numViews) {
		this._numViews = numViews;
	}

	public String get_business_id() {
		return _business_id;
	}

	public void set_business_id(String _business_id) {
		this._business_id = _business_id;
	}

	public Double get_lati() {
		return _lati;
	}

	public void set_lati(Double _lati) {
		this._lati = _lati;
	}

	public Double get_longi() {
		return _longi;
	}

	public void set_longi(Double _longi) {
		this._longi = _longi;
	}

	public String get_address() {
		return _address;
	}

	public void set_address(String _address) {
		this._address = _address;
	}

	public Double get_stars() {
		return _stars;
	}

	public void set_stars(Double _stars) {
		this._stars = _stars;
	}

	public String get_zip() {
		return _zip;
	}

	public void set_zip(String _zip) {
		this._zip = _zip;
	}

	public Vector<String> get_categories() {
		return _categories;
	}

	public void set_categories(Vector<String> _categories) {
		this._categories = _categories;
	}

	public String getCity() {
		return _city;
	}

	public void setCity(String city) {
		this._city = city;
	}

	public Integer get_num_Reviews() {
		return _num_Reviews;
	}

	public void set_num_Reviews(Integer _num_Reviews) {
		this._num_Reviews = _num_Reviews;
	}

}
