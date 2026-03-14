# Global Food Price Analysis Using MapReduce

*University:* University of Ruhuna, Faculty of Engineering
*Module:* EE7222/EC7204 - Cloud Computing
*Assignment:* Large-Scale Data Analysis Using MapReduce
*Team Members:*
- Member 1: [Name] - [Index Number]
- Member 2: [Name] - [Index Number]
- Member 3: [Name] - [Index Number]

---

## Dataset
- *Source:* Kaggle - WFP Global Food Prices
- *Link:* https://www.kaggle.com/datasets/jboysen/global-food-prices
- *File:* wfp_market_food_prices.csv
- *Size:* 84MB | 743,915 records

---

## Project Structure

food-price-mapreduce/
├── src/
│   ├── mapper.py        
│   ├── reducer.py       
│   └── run_job.sh       
├── data/
│   └── wfp_market_food_prices.csv
├── output/
│   ├── results.tsv      
│   └── job_log.txt      
└── README.md


---


## Steps to Run

### Step 1 — Start SSH
bash
sudo service ssh start


### Step 2 — Start Hadoop
bash
start-dfs.sh
start-yarn.sh


### Step 3 — Verify Hadoop is Running
bash
jps

Expected output:

NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager


### Step 4 — Go to Project Folder
bash
cd ~/food-price-mapreduce


### Step 5 — Verify Dataset is There
bash
ls -lh data/

Expected output:

wfp_market_food_prices.csv  84M


### Step 6 — Test Locally First
bash
head -1000 data/wfp_market_food_prices.csv | \
python3 src/mapper.py | sort | \
python3 src/reducer.py | head -20

Expected output:

Afghanistan     Bread   2014    51.22   45.34   55.60   24
Afghanistan     Bread   2015    52.75   50.00   65.25   20
...


### Step 7 — Clear Old HDFS Data
bash
hdfs dfs -rm -r -f hdfs:///food_prices/output
hdfs dfs -rm -r -f hdfs:///food_prices/input
rm -f output/results.tsv


### Step 8 — Run Full MapReduce Job
bash
bash src/run_job.sh 2>&1 | tee output/job_log.txt

Wait until you see:

map 100% reduce 100%
Job completed successfully


### Step 9 — Download Results from HDFS
bash
hdfs dfs -get hdfs:///food_prices/output/part-00000 output/results.tsv


### Step 10 — View Results
bash
cat output/results.tsv | head -30

Expected output:

Afghanistan   Bread             2014   42.84   29.40   55.60   96
Afghanistan   Fuel (diesel)     2015   43.96   35.50   55.75   96
Sri Lanka     Rice (long grain) 2017   88.21   79.67   96.50   80


### Step 11 — Analyze Results
bash
# Total number of results
wc -l output/results.tsv

# Most expensive commodities globally
sort -t$'\t' -k4 -rn output/results.tsv | head -10

# Cheapest commodities globally
sort -t$'\t' -k4 -n output/results.tsv | head -10

# Filter by specific country
grep "^Sri Lanka" output/results.tsv


### Step 12 — Stop Hadoop When Done
bash
stop-all.sh


---

## Output Format

Country | Commodity | Year | AvgPrice | MinPrice | MaxPrice | Count


## Execution Results

| Metric              | Value     |
|---------------------|-----------|
| Input file size     | 84 MB     |
| Records processed   | 743,913   |
| Output records      | 7,066     |
| Map tasks           | 2         |
| Reduce tasks        | 1         |
| Processing time     | ~30 secs  |
| Failed tasks        | 0         |
| Shuffle errors      | 0         |

---

## GitHub Repository
https://github.com/URasanjali/food-price-mapreduce
