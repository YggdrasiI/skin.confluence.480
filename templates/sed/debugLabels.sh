#!/bin/bash
#
# Replace all labels with its line number to find their sources.

# go into templates...
cd ..

for FILE in $(ls *.xml) ; do
echo "Handle $FILE"
cat "${FILE}" | \
  sed -e '/<label>/{=; s/<label>\([^<]*\)<\/label>/|\1|/}' | \
  sed -e '/^[1-9]/{ N; s/\n//; s/^\([0-9]*\)\(.*\)|\([^|]*\)|/\2<label>\1,'${FILE}'<\/label>/}' \
  > "../tmp/${FILE}"

done

# Parse them
cd ..
./parseTemplates.py -f -t "tmp/"
