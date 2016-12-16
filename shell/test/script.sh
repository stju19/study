#!/bin/bash

file=cfg.conf
key=abc
value=test
sed -i "s@^[[:space:]]*#[[:space:]]*$key[[:space:]]*=[[:space:]]*.*@$key=$value@" $file