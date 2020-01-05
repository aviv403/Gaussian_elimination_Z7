#!/bin/bash

temp_py_path="gauss.py"
py_path="gauss.py"
list=()
q="off"
r="off"
empty_flag="" # for '-z' command

# find path to .py file
for arg in "$@"; do
	if echo "$arg" | grep '\.py$' > /dev/null 2>&1 ; then
		temp_py_path=$arg; fi
done

# grep .in files from command-line and gets flags
for arg in "$@"; do
	if echo "$arg" | grep '\.in$' > /dev/null 2>&1; then
		list+=( $arg ); fi	
	if [ "$arg" = "-p" ]; then
		py_path=$temp_py_path; fi	
	if [ "$arg" = "-q" ]; then
		q="on"; fi	
	if [ "$arg" = "-r" ]; then
		r="on"; fi	
done

# if command-line list is empty(from *.in) then list is the path to all *.in
if [ -z $list ]; then
	list+=( '*.in' ); fi

# update empty_flag var
if [ "$r" = "on" ]; then
	empty_flag=""
else
	empty_flag="-z"
fi

# run .py file on each item in the list
for item in ${list[@]}; do
	if [ -f $item ]; then
		if [ "$q" = "on" ]; then #if -q flag
			if [ -z "$(python3 "$py_path" < $item)" ]; then
				echo "1"
				exit
			fi
		elif [ $empty_flag "$(python3 "$py_path" < $item)" ]; then
			echo "$(basename $item)"
		fi
	fi
done

#if -q flag and the program didnt find unexpected output
if [ "$q" = "on" ]; then
	echo "0"; fi




