#!/bin/bash

fn="`date +%Y-%m-%d`-weekly-link-roundup.md"

cat >$fn <<EOH
---
layout: post
title: Weekly link roundup
---
EOH

python twitter-digest.py >> $fn