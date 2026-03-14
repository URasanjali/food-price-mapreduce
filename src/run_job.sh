#!/bin/bash
# ============================================================
# run_job.sh — Submits MapReduce job to Hadoop via Streaming
# ============================================================

INPUT_DIR="hdfs:///food_prices/input"
OUTPUT_DIR="hdfs:///food_prices/output"
DATASET="$HOME/food-price-mapreduce/data/wfp_market_food_prices.csv"

echo "=== Step 1: Upload dataset to HDFS ==="
hdfs dfs -mkdir -p $INPUT_DIR
hdfs dfs -put $DATASET $INPUT_DIR/
echo "Dataset uploaded."

echo "=== Step 2: Remove old output (if any) ==="
hdfs dfs -rm -r -f $OUTPUT_DIR

echo "=== Step 3: Run MapReduce Streaming Job ==="
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files src/mapper.py,src/reducer.py \
  -mapper  "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -input   $INPUT_DIR \
  -output  $OUTPUT_DIR

echo "=== Step 4: Show output sample ==="
echo "--- First 20 results ---"
hdfs dfs -cat $OUTPUT_DIR/part-00000 | head -20

echo "=== Step 5: Download full output ==="
mkdir -p output
hdfs dfs -get $OUTPUT_DIR/part-00000 output/results.tsv
echo "Results saved to output/results.tsv"
