JCC = javac
JVM = java
JFLAGS = -classpath "library/*"
INDEXFLAGS = -classpath "src:library/*" 
RUNFLAGS = -classpath "src:library/*" -Xmx3000m  -Xms2500m

.java.class:
	$(JCC) $(JFLAGS) $*.java

default:
	$(JCC) $(JFLAGS) src/edu/nyu/cs/cs2580/*.java

index:
	$(JVM) $(INDEXFLAGS) edu.nyu.cs.cs2580.SearchEngine --mode=index --options=conf/engine.conf

run:
	$(JVM) $(RUNFLAGS) edu.nyu.cs.cs2580.SearchEngine --mode=serve --port=25808 --options=conf/engine.conf 	  

clean:
	find . -name '*.class' -exec rm -rf {} \;
	find . -name '*~' -exec rm -rf {} \;




