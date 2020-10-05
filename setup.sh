#!/bin/sh
# make a python virtual environment if it doesn't exist yet
if [ ! -d "env" ]; then
	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.txt
	deactivate
fi

# add line to automatically use virtual environment for python viles
for script in *.py
do
	line=$(head -n 1 $script)
	SHEBANG="#!"
	if [ ${line:0:2} != $SHEBANG ]; then
		(echo "#! $PWD/env/bin/python3" && cat $script) > temp && mv temp $script
	fi
done

# give run permissions
chmod +x send_email.py
chmod +x launcher.py
