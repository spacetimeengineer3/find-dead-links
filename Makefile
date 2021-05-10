SHELL=/bin/bash
INSTALL_DIR = ~/bin
WRAPPER = ${INSTALL_DIR}/wrapper
PYTHON = ${INSTALL_DIR}/find-dead-links.py
ENV = ${INSTALL_DIR}/ENV

install: ${WRAPPER} ${PYTHON} ${ENV}

${WRAPPER}: wrapper
	cp wrapper ${INSTALL_DIR}
	chmod 700 ${INSTALL_DIR}/wrapper

${PYTHON}: find-dead-links.py
	cp find-dead-links.py ${INSTALL_DIR}
	chmod 700 ${INSTALL_DIR}/find-dead-links.py

${ENV}:
	python3 -m virtualenv ${ENV}
	source ${ENV}/bin/activate && pip install requirements.txt

