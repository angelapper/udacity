# udacity
 hadoop jar /usr/hdp/2.3.0.0-2557/hadoop-mapreduce/hadoop-streaming.jar -mapper bystoremapper.py -reducer maxsalereducer.py -file bystoremapper.py -file maxsalereducer.py -input data/udacitypurchase -output joboutput/udacity/purchase/maxsalesv2
