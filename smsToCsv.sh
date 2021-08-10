#!/bin/bash
PASSWORD="1"
rm -Rf apps backup.tar backs messages.csv
java -jar ./bin/abe.jar unpack backup.ab backup.tar $PASSWORD
tar xvf backup.tar
mkdir -p backs
find ./apps -type f | grep backup | while read f; do
	cp $f backs/
done
rm -Rf apps
find ./backs -type f | grep backup | while read f; do
	java -jar ./bin/sms_restore.jar "$f" > "$f".json
done
python3 ./bin/jsonToCsv.py backs/*.json
#ssconvert messages.csv messages.xlsx
