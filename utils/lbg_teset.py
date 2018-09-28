import os

images_path=r"E:\git_track\MBMD\model\mouse"
for root, dirs, files in os.walk(images_path): # 遍历统计
      for tfile in files:
          if tfile.endswith(".jpg"):
            print(tfile)