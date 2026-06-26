import os
from collections import defaultdict

base = 'nabh_documents'
cats = defaultdict(list)

for cat in os.listdir(base):
    cat_path = os.path.join(base, cat)
    if os.path.isdir(cat_path):
        for f in os.listdir(cat_path):
            fpath = os.path.join(cat_path, f)
            size = os.path.getsize(fpath)
            cats[cat].append({'name': f, 'size_kb': round(size/1024, 1)})

print('\n===== NABH DOCUMENT INTELLIGENCE REPORT =====\n')
total = 0
for cat, files in sorted(cats.items()):
    print(f'[{cat.upper()}] - {len(files)} files')
    for f in sorted(files, key=lambda x: -x['size_kb'])[:5]:
        print(f'  {f["size_kb"]:>8} KB  {f["name"]}')
    if len(files) > 5:
        print(f'  ... and {len(files)-5} more')
    total += len(files)
    print()

print(f'TOTAL: {total} documents')
print('=============================================')