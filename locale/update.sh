#!/bin/bash

SRCPATH=..
LOCALEPATH=$SRCPATH/locale

function updatePOT {

  TMPFILE=/tmp/tmp_pofiles.familycalendar.tmp

  find $SRCPATH/ -name *.py >> $TMPFILE

  xgettext --default-domain=familycalendar --files-from=$TMPFILE --output=$LOCALEPATH/familycalendar.pot --from-code=UTF-8 --language=Python

  rm -f $TMPFILE

}

function updatePO {

  LANG=$1
  SOURCEFILENAME=$LOCALEPATH/familycalendar.pot
  DESTFILENAME=$LOCALEPATH/$LANG/LC_MESSAGES/familycalendar.po

  if [ ! -f $DESTFILENAME ]; then
    msginit --input=$SOURCEFILENAME --output=$DESTFILENAME --locale=$LANG.UTF-8 --no-translator
  else
    msgmerge --update $DESTFILENAME $SOURCEFILENAME
  fi

}

updatePOT

updatePO es_ES
updatePO ca_ES
