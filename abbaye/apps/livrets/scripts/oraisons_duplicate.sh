#!/bin/bash

#  Ce script duplique toutes les oraisons indiquées dans le find
#+ en remplaçant le nom du fichier par la référence voulue,
#+ et en vidant le fichier.

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$SCRIPT_DIR/../static/livrets/data/oraisons"
find . -type f -name 'cm_16_*' | sort | while read
do
	f=`echo "$REPLY"`
	fn=`echo "$REPLY" | sed 's/cm_16_/misericorde_/g'`
    echo "$fn"
    #cp "$f" "$fn"
    #echo "" > "$fn"
done

exit

