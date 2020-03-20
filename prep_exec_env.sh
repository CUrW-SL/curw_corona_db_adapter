#!/usr/bin/env bash
echo `date`

echo "Changing into ~/curw_corona_db_adapter"
cd /home/uwcc-admin/curw_corona_db_adapter
echo "Inside `pwd`"


# If no venv (python3 virtual environment) exists, then create one.
if [ ! -d "venv" ]
then
    echo "Creating venv python3 virtual environment."
    virtualenv -p python3 venv
fi

# Activate venv.
echo "Activating venv python3 virtual environment."
source venv/bin/activate

# Install dependencies using pip.
if [ ! -f "db.log" ]
then
    pip install PyMySQL
    pip install Scrapy
    pip install DBUtils
    pip install requests
fi

# Deactivating virtual environment
echo "Deactivating virtual environment"
deactivate
