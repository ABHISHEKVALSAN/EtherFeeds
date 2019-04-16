System specifications
=====================

Linux Ubuntu 18.04.2 LTS

Tool specifications
===================

python3.6


Procedure
=========

Set up a python virtual environment named mysiteEnv, you want to install
virtualenv package via pip for this action

$ virtualenv mysiteEnv

Activate the environment

$ source mysiteEnv/bin/activate

Verify that the environment is activated by checking passing command

$ which python3

This should show something like /home/.../EtherFeeds/mysiteEnv/bin/pythno3

Now lets have to install some python3 packages

$ pip3 install -r requirements.txt

Now lets deploy our solidity contract contract

$ sh reset.sh

This also make sure that appropriate migrations are being made to the db.sqlite3

Lets run the app locally

$ python3 manage.py runserver

If the port is busy, then run python3 manage.py runserver [4-digit-port-number]
