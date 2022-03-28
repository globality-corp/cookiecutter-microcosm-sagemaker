#  This file is auto generated with globality-build.
#  You should not make any changes to this file manually
#
#  See: http://github.com/globality-corp/globality-build
#
#  This Makefile is only in use for repositories managing their
#  dependencies with pip-compile.
#
#  See https://globality.atlassian.net/wiki/spaces/DEV/pages/1348273419/Managing+Python+dependencies
#  for notes on how to switch
#
PIP_COMPILE=pip-compile
PIP_COMPILE_FLAGS=--no-emit-index-url --generate-hashes
UPDATE_PACKAGE:=marquez

.PHONY: all update-all-deps sync-all-deps

all: requirements.txt requirements-build.txt


requirements.txt: setup.py
	${PIP_COMPILE} ${PIP_COMPILE_FLAGS} 


requirements-build.txt: requirements-build.in requirements.txt
	${PIP_COMPILE} requirements-build.in -o requirements-build.txt ${PIP_COMPILE_FLAGS}


update-all-deps:
	${PIP_COMPILE} -U ${PIP_COMPILE_FLAGS} 
	${PIP_COMPILE} -U requirements-build.in -o requirements-build.txt ${PIP_COMPILE_FLAGS}


update-package:
	${PIP_COMPILE} ${PIP_COMPILE_FLAGS} -P ${UPDATE_PACKAGE} 
	${PIP_COMPILE} requirements-build.in -o requirements-build.txt ${PIP_COMPILE_FLAGS} -P ${UPDATE_PACKAGE}


sync-all-deps:
	pip install pip-tools
	pip-sync requirements.txt requirements-*.txt --pip-args --no-deps
	pip install --no-deps -e .
