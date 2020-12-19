#!/bin/bash
python familycalendar.py >> log/error.log 2>> log/error.log
if [ $? -ne 0 ]; then
  echo "Error executant familycalendar.py"
fi
