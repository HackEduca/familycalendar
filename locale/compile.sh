#!/bin/bash
SRCPATH=..
LOCALEPATH=$SRCPATH/locale

function compilePO {

  LANG=$1
  DESTPATH=$LOCALEPATH/$LANG/LC_MESSAGES

  msgfmt $DESTPATH/familycalendar.po --output-file=$DESTPATH/familycalendar.mo

  rm -f $LOCALEPATH/familycalendar.po~
  rm -f $LOCALEPATH/$LANG/familycalendar.po~
  rm -f $LOCALEPATH/$LANG/LC_MESSAGES/familycalendar.po~

}

compilePO es_ES
compilePO ca_ES
