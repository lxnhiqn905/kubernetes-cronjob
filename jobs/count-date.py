from pathlib import Path
from datetime import datetime
import os

print("=== Starting job: ", datetime.now())

target_file = "data/data_file" + datetime.now().strftime("%Y%m%d%H") + ".txt"
print("Directory Path:", Path().absolute())
print("Target file: ", target_file)	

current_count = 0

if Path(target_file).is_file():
    #open and read the file after the appending:
    fr = open(target_file, "r")
    file_content = fr.read(1000)
    print(target_file , "File content:", file_content)
    current_count = int(file_content.strip())
    fr.close()
else:
    print("File ", target_file, "not exist!")

#open and write the file with mode appending:
f = open(target_file, "w")
print(target_file , "Old content:", str(current_count))
current_count = int(current_count) + 1 
print(target_file , "New content:", str(current_count))
f.write(str(current_count))
f.close()

print("\nList file after execute job:")
for root, dirs, files in os.walk("./data"):
    for filename in files:
        print(filename)

print("=== Stopping job: ", datetime.now())
