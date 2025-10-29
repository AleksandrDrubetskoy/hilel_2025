import csv

file1 = 'r-m-c.csv'
file2 = 'random-michaels.csv'

output_file = 'result_Drubetskoy.csv'

# Read data from both files
data = []
for file in [file1, file2]:
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                data.append(tuple(row))

# Removing duplicates
unique_data = list(set(data))

# Writing result
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(unique_data)

print(f"Done! The result is saved in a file: {output_file}")
print(f"There were {len(data)} rows, after cleaning there were left {len(unique_data)}.")
