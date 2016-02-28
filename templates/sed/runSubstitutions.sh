#!/bin/bash

FILES=$(ls ../*.xml)

# Default set of scripts. Could be overwritten by input args.
SCRIPTS=("undefined.sed" )
test $# -le 0 || SCRIPTS=($@)

IFS_BACKUP=$IFS
IFS=$(echo -en "\n\b")

for SCRIPT in "${SCRIPTS[@]}" ; do
  echo "Run $SCRIPT"
  for FILE in ${FILES} ; do
    #echo sed -i -f "$SCRIPT" "$FILE"
    sed -i -f "$SCRIPT" "$FILE"
  done
done


IFS=$IFS_BACKUP
