import os

print("Megabit Media Converter v2")

convert_path="/home/megabitco/convert"
local_path=os.path.join(convert_path,"local")
tvshow_path=os.path.join(convert_path,"TV Shows")
movie_path=os.path.join(convert_path, "Movies")

# TV Conversion
for SHOW in os.listdir(tvshow_path):
  print(SHOW)