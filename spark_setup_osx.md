# How to setup Spark on OSX (without Homebrew)

This walkthrough is designed for beginners who may not have a lot of experience setting up cluster computing framework tools like Apache Spark.  

**Note** This walkthrough is targeted towards those who 

## Why should I use Spark?

In simple terms, Spark allows you to easily spread your large scale data jobs across multiple computers.  Spark is easy to use, and if you are familiar with Python, Pyspark is a great way to get started running parallelized jobs.

#### Pre-requistes:
+ Python
+ Pip

## Setup

1.  [Download Apache Spark](http://spark.apache.org/downloads.html)
We recommend selecting "Pre-Built for Hadoop 2.7 and Later" so that you skip the 'build' step.

2.  [Download and Install Java](http://www.oracle.com/technetwork/java/javase/downloads/index.html)

3.  You will also need py4j to allow Python to access Java objects (necessary to run Pyspark).  To install py4j, you can run `pip install py4j` in Terminal

3.  Unzip spark-2.0.2-bin-hadoop2.7.tgz, you can do this by running `gunzip ~/Downloads/spark-2.0.2-bin-hadoop2.7.tgz` in Terminal

4.  Move Spark to somewhere in your PATH, such as /usr/local/Cellar, you can do this with the command `mv ~/Downloads/spark-2.0.2-bin-hadoop2.7 /usr/local/Cellar`

5.  Now that you have the prebuilt Spark setup, make sure that the spark shell itself works.  To do this run `/usr/local/Cellar/spark-2.0.2-bin-hadoop2.7/bin/pyspark ` in Terminal

   If this is successful, you should see "Welcome to Pyspark"

   You now have Pyspark setup, but the next steps will be necessary to ensure that your python can import your Pyspark module.

   *Note* If this step failed, you may want to go back to step 1 and make sure that you downloaded a pre-built version of spark.

6.  Make sure that your .bashrc file is getting sourced.  To do so, exit your Pyspark session 'exit()', and run 'nano ~/.bash_profile'.  There make sure there is a `source ~/.bashrc` line at the end. Then edit your bashrc  `nano ~/.bashrc`, and add the following lines:

```
export SPARK_HOME=/usr/local/Cellar/spark-2.0.2-bin-hadoop2.7
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
export PATH="$SPARK_HOME/bin:$PATH"
```

## What these lines do:

The first line sets up a shortcut to your Spark directory that you setup in step 4.

The second line adds the python folder (within your spark folder) to your PYTHONPATH, which allows you to import pyspark.

The third line adds the bin folder which allows you to run spark commands from Terminal (which we will see in the next walkthrough when we run spark-submit).

After you have added the lines, you need a source your .bashrc files by running `source ~/.bashrc` in Terminal.  This executes the changes you made above.

Now to test, run 'python' in Terminal to launch python, and enter 'import pyspark' to make sure the library imports.  If it doesn't fail you are all set!