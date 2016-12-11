# How to setup Pyspark on OSX (without Homebrew)

1.  [Download Apache Spark](http://spark.apache.org/downloads.html)
We recommend selecting "Pre-Built for Hadoop 2.7 and Later"

2.  Unzip spark-2.0.2-bin-hadoop2.7.tgz, you can do this by running 'gunzip ~/Downloads/spark-2.0.2-bin-hadoop2.7.tgz' in terminal

3.  Move Spark to somewhere in your PATH, we recommend /usr/local/Cellar, you can do this with the command 'mv ~/Downloads/spark-2.0.2-bin-hadoop2.7 /usr/local/Cellar'