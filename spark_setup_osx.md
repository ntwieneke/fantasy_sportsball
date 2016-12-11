# How to setup Pyspark on OSX (without Homebrew)

1.  [Download Apache Spark](http://spark.apache.org/downloads.html)
We recommend selecting "Pre-Built for Hadoop 2.7 and Later"

2.  Download and Install Java

3.  Unzip spark-2.0.2-bin-hadoop2.7.tgz, you can do this by running `gunzip ~/Downloads/spark-2.0.2-bin-hadoop2.7.tgz` in terminal

4.  Move Spark to somewhere in your PATH, we recommend /usr/local/Cellar, you can do this with the command `mv ~/Downloads/spark-2.0.2-bin-hadoop2.7 /usr/local/Cellar`

5.  Test The spark shell, you can do this by simply running `/usr/local/Cellar/spark-2.0.2-bin-hadoop2.7/bin/pyspark ` in terminal

6.  Bashrc, `nano ~/.bashrc`, then add the following lines:

```
export SPARK_HOME=/usr/local/Cellar/spark-2.0.2-bin-hadoop2.7
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
export PATH="$SPARK_HOME/bin:$PATH"
```

To apply these changes, then run `source ~/.bashrc` in Terminal