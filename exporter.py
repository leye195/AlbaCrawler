import csv
def save_to_file(filename,jobs):
  file = open(f"{filename}.csv",mode="w")
  #csv 활용, csv.writer(file)
  writer = csv.writer(file)
  writer.writerow(["place","title", "time", "pay", "date","link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return