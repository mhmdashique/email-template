import os
import re

html_path = 'Suresh_Kumar_Studio_Notes_Newsletter/newsletter.html'
images_dir = 'Suresh_Kumar_Studio_Notes_Newsletter/images'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
print("Image sources in HTML:", srcs)

for s in srcs:
    fname = os.path.basename(s)
    p = os.path.join(images_dir, fname)
    assert os.path.exists(p), f"Missing image: {p}"
    print(f"Resolved: {s} -> {p}")

dir_files = os.listdir(images_dir)
print("Files in images folder:", dir_files)
for f in dir_files:
    assert any(f in s for s in srcs), f"Unused file in images/: {f}"
print("All image files resolve exactly with zero unused files!")

