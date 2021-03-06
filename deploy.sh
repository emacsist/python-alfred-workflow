#!/usr/bin/env bash

DST_DIR="/Users/emacsist/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/user.workflow.D9907291-6A25-47C7-ACD5-4E5380300EE9"

cp douban/douban-book.py "${DST_DIR}"/book.py
cp douban/douban-movie.py "${DST_DIR}"/movie.py
cp -R img "${DST_DIR}"/


WEIBO_DST_DIR="/Users/emacsist/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/user.workflow.9CBF9071-1DFF-46EE-956E-C5AFA06B3655"
cp weibo/*.py "${WEIBO_DST_DIR}"/
cp -R img "${WEIBO_DST_DIR}"/

# money
cp money/interest_rate.py "/Users/emacsist/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/user.workflow.A509D1B5-0FDD-4388-9CA1-F346DEEA5850/"
mkdir -p "/Users/emacsist/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/user.workflow.A509D1B5-0FDD-4388-9CA1-F346DEEA5850/img/"
cp -R img/money.png "/Users/emacsist/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/user.workflow.A509D1B5-0FDD-4388-9CA1-F346DEEA5850/img/"