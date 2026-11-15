import sys
import pandas as pd

print("arguments", sys.argv)

df = pd.DataFrame({"DAY": [1, 2], "Passanger": [3, 4]})

print(df.head())

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")
