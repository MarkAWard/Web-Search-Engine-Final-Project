package edu.nyu.cs.cs2580;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.lang.StringBuilder;
import java.text.Normalizer;
import java.util.Scanner;
import java.util.regex.Pattern;


public class ReadCorpus {

    // for test corpus
	@SuppressWarnings("resource")
	public String createFileInput(String content) throws IOException {
		StringBuilder out = new StringBuilder();
		Scanner s = new Scanner(content).useDelimiter("\t");
		String title = s.next();
		String body = cleanAndStem(s.next());

		out.append(title);
		out.append('\t');
		out.append(body);
		out.append('\t');
		out.append(s.next());
		out.append('\t');
		out.append(title.replace(" ", "_"));

		s.close();
		return out.toString();
	}

    // for wiki text
	public String createFileInput(final File filename) throws IOException {
		StringBuilder out = new StringBuilder();
		StringBuilder body = new StringBuilder();
		StringBuilder url = new StringBuilder();

		String html = readFile(filename);
		Document doc = Jsoup.parse(html);

		out.append(filename.getName());
		out.append('\t');

		body.append( getTagText(doc, "h1"));
		out.append(' ');
		body.append( getTagText(doc, "h2"));
		out.append(' ');
		body.append( getTagText(doc, "p"));
		out.append(' ');
		out.append( cleanAndStem(body.toString()) );

		out.append('\t');
		out.append('0');

		url.append("en.wikipedia.org/wiki/");
		url.append(filename.getName());
		out.append('\t');
		out.append(url);

		return out.toString();
	}

	private String getTagText(Document html_doc, String tag) {
		StringBuilder sectionText = new StringBuilder();
		Elements tags = html_doc.getElementsByTag(tag);
		for (Element elem : tags) {
			sectionText.append(elem.text());
			sectionText.append(' ');
		} 
		return sectionText.toString();
	}


	private String readFile(File filename) throws IOException {
		BufferedReader reader = new BufferedReader(new FileReader(filename));
		StringBuilder everything = new StringBuilder();
		String line = null;
		while ((line = reader.readLine()) != null) {
			everything.append(line);
		}
		reader.close();
		return everything.toString();
	}    

	public String cleanAndStem(String body) throws IOException {

    	// remove accents from characters
		String nfdNormalizedString = Normalizer.normalize(body, Normalizer.Form.NFD); 
		Pattern pattern = Pattern.compile("\\p{InCombiningDiacriticalMarks}+");
		body = pattern.matcher(nfdNormalizedString).replaceAll("");

    	// remove a bunch of symbols
		String charsToDel = "`~!@#$%^&*()_-+=[]\\{}|;':\",./<>?";
		body = body.replaceAll("[" + Pattern.quote(charsToDel)  + "]", " ");

		// gooooood --> good
		body = body.replaceAll("([a-zA-Z])(\\1{2,})", "$1$1");

		StringBuilder out = new StringBuilder();
		char[] w = new char[501];
		Stemmer porter = new Stemmer();
		InputStream in = new ByteArrayInputStream( body.getBytes() );

		while(true) {
			int ch = in.read();
			if (Character.isLetter((char) ch)) {
				int j = 0;
				while(true) {
					ch = Character.toLowerCase((char) ch);
					w[j] = (char) ch;
					if (j < 500) j++;
					ch = in.read();
					if (!Character.isLetter((char) ch)) {
						for (int c = 0; c < j; c++) porter.add(w[c]);
						porter.stem();
						out.append(porter.toString());
						break;
					}
				}
			}
			if (ch < 0) break;
			out.append((char)ch);
		}
		return out.toString();
	}

}