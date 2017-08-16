#!/bin/bash
nosetests -v --with-coverage --cover-erase
if [ $? -eq 1 ]; then
    echo "unit tests failed"
    exit 1
fi
