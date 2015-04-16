import zlib
import os

hashes = set()
for fil in os.listdir('scraped-html/players'):
    has = zlib.crc32(bytes(fil[:-5], 'UTF-8'))
    if has in hashes:
        print('FUCKING ALERT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        input()
    hashes.add(has)
    print('{} hash -> {}'.format(fil[:-5], has))
