import re

with open('deliverables/newsletter.html', 'r', encoding='utf-8') as f:
    html = f.read()

size = len(html.encode('utf-8'))
scripts = len(re.findall(r'<script', html, re.I))
events = len(re.findall(r' on\w+=', html, re.I))
stylesheets = len(re.findall(r'rel=[\'"]stylesheet[\'"]', html, re.I))
grids = len(re.findall(r'display\s*:\s*grid', html, re.I))
flexes = len(re.findall(r'display\s*:\s*flex', html, re.I))
imgs = re.findall(r'<img[^>]*>', html, re.I)
imgs_no_alt = [img for img in imgs if 'alt=' not in img]
roles = len(re.findall(r'role=[\'"]presentation[\'"]', html, re.I))
tables = len(re.findall(r'<table', html, re.I))
ref_mentions = len(re.findall(r'(desktop_1440|mobile_375)', html, re.I))

print(f"File size: {size} bytes ({size/1024:.2f} KB)")
print(f"script tags: {scripts}")
print(f"event handlers: {events}")
print(f"stylesheets: {stylesheets}")
print(f"display grid: {grids}")
print(f"display flex: {flexes}")
print(f"total imgs: {len(imgs)}")
print(f"imgs without alt: {len(imgs_no_alt)}")
print(f"total tables: {tables}")
print(f"tables with role presentation: {roles}")
print(f"Design reference PNGs referenced: {ref_mentions}")
