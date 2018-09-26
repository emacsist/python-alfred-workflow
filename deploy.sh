#!/usr/bin/env bash

DST_DIR="/Users/emacsist/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/user.workflow.D9907291-6A25-47C7-ACD5-4E5380300EE9"

cp douban/douban-book.py "${DST_DIR}"/book.py
cp douban/douban-movie.py "${DST_DIR}"/movie.py
cp -R img "${DST_DIR}"/