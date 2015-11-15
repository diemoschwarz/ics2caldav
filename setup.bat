@echo off

setup.py register
setup.py bdist_wheel upload
setup.py sdist upload
