package edu.nyu.cs.cs2580;

import org.json.simple.JSONObject;

class ScoredDocument implements Comparable<ScoredDocument> {
	private Document _doc;
	private double _score;
	private double _distance;

	private double _cosine;
	private double _title;
	private double _category;


	public ScoredDocument(Document doc, double score) {
		set_doc(doc);
		_score = score;
	}

	public ScoredDocument(){
		Document fake = new Document(-1);
		fake.setTitle("NO RESULTS");
		fake.set_lati(0.0);
		fake.set_longi(0.0);
		fake.set_stars(0.0);
		fake.set_address("");
		fake.setCity("");
		fake.setUrl("#");
		fake.set_num_Reviews(0);
		_score = 0.0;
	}

	public String asTextResult() {
		StringBuffer buf = new StringBuffer();
		buf.append(get_doc()._docid).append("\t");
		buf.append(get_doc().getTitle()).append("\t");
		buf.append(_score).append("\t");
		buf.append(get_doc().getPageRank()).append("\t");
		buf.append(get_doc().getNumViews()).append("\t");
		return buf.toString();
	}

	@SuppressWarnings("unchecked")
	public JSONObject asJSON() {
		JSONObject json_buf = new JSONObject();

		json_buf.put("name", get_doc().getTitle());
		json_buf.put("lat", get_doc().get_lati());
		json_buf.put("long", get_doc().get_longi());
		json_buf.put("star", get_doc().get_stars());
		json_buf.put("address", get_doc().get_address());
		json_buf.put("city", get_doc().getCity());
		json_buf.put("url", get_doc().getUrl());
		json_buf.put("num_reviews", get_doc().get_num_Reviews());
		return json_buf;
	}

	/**
	 * @CS2580: Student should implement {@code asHtmlResult} for final project.
	 */
	public String asHtmlResult() {
		return "";
	}

	@Override
	public int compareTo(ScoredDocument o) {
		if (this._score == o._score) {
			return 0;
		}
		return (this._score > o._score) ? 1 : -1;
	}

	public void set_doc(Document _doc) {
		this._doc = _doc;
	}
	public Document get_doc() {
		return _doc;
	}

	public void updateScore(double additional) {
		_score *= additional;
	}
	public double get_score() {
		return _score;
	}

	public void set_distance(double distance) {
		this._distance = distance;
	}
	public double get_distance() {
		return _distance;
	}

	public void set_cosine(double cosine) {
		this._cosine = cosine;
	}
	public double get_cosine() {
		return _cosine;
	}

	public void set_title(double title) {
		this._title = title;
	}
	public double get_title() {
		return _title;
	}

	public void set_category(double category) {
		this._category = category;
	}
	public double get_category() {
		return _category;
	}
}
