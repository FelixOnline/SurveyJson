from __future__ import with_statement
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def commit():
	#	migrate('website')
	local('pip freeze > '+BASE_DIR+'/requirements.txt')
	local('git add --interactive && git commit')


def test(app=None):
	if app:
		pass
	else:
		local('python '+BASE_DIR+'/stoic_web/manage.py test stoic_web')

def migrate(app_name):
	with settings(warn_only=True):
		result=	local('python '+BASE_DIR+'/stoic_web/manage.py schemamigration '+app_name+' --auto')
	if result.failed and not confirm("The migration of '"+app_name+"' has failed. Would you like to continue anyway?"):
		abort("Aborting process")
def collectstatic():
	local('python '+BASE_DIR+'/stoic_web/manage.py collectstatic')
	
def runserver():
	test()
	collectstatic()
	local('python '+BASE_DIR+'/stoic_web/manage.py runserver 0.0.0.0:8000')
