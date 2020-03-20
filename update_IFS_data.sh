#!/usr/bin/env bash

cd /home/uwcc-admin/curw_corona_db_adapter/corona_data
echo "Inside `pwd`"

scrapy crawl ifs

FILE_MODIFIED_TIME=$(date -r /home/uwcc-admin/curw_corona_db_adapter/IFS.csv +%s)
CURRENT=$(date +%s)

DIFF=$(((CURRENT-FILE_MODIFIED_TIME)/60))
echo $DIFF

if [ $DIFF -lt 7 ]
then
  echo "File Updated!!!"
  cd ..
  echo "Inside `pwd`"


  # Update corona data
  echo "Update corona data ...."
  ./db_utils/update_corona_data.py >> corona_update.log 2>&1
fi





