import os

#  # create file (remove comment to create 100 files )
# for i in range(1,101):
#   open(f"png/file{i}.txt","x")
  

  # rename file
for i in range(0,100):
   os.rename(f"png/file{i+1}.txt",f"png/{i+1}.png")
  
  
#   # delete file (remove comment to delete all files)
# for i in range(0,100):
#    os.remove(f"png/{i+1}.png")
  