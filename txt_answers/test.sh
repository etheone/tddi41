#!/bin/bash
dotfiles=0
while read line
do
if [ "${line:0:1}" = "." ]
then
:
else
dotfiles=$((dotfiles + 1))
fi
done <<EOF
`ls -la`
EOF
