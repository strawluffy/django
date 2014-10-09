#!/usr/bin/env python
#coding:utf8
from fabric.api import local
def prepare_deploy():
	local("./manage.py test my_app")
