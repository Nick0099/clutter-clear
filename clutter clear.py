import os
i=1
for file in os.listdir("clutter"):
  if file.endswith(".png"):  
    print(f"{file}")
    os.rename(f"clutter/{file}",f"clutter/{i}.png")
    
    i=i+1
# for i in range(1,100):
#    open (f"clutter/sfhjsakaefj{i}.png","x")
