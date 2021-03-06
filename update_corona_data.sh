#!/usr/bin/env bash

cd /home/uwcc-admin/curw_corona_db_adapter/
echo "Inside `pwd`"
source venv/bin/activate
cd corona_data
scrapy crawl ifs

FILE_MODIFIED_TIME=$(date -r /home/uwcc-admin/curw_corona_db_adapter/corona_data/IFS_patient.csv +%s)
CURRENT=$(date +%s)

DIFF=$(((CURRENT-FILE_MODIFIED_TIME)/60))
echo $DIFF

if [ $DIFF -lt 7 ]
then
  echo "File Updated!!!"
  cd ..
  echo "Inside `pwd`"


  # Update corona data
  echo "Update from covidsl.com data ...."
  ./update_covidsl_data.py >> covidsl_update.log 2>&1
fi

echo "Update from hpb data ...."
./update_hpb_data.py >> hpb_update.log 2>&1




