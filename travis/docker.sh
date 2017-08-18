#!/bin/bash

set -e

# Build docker image
sudo docker build --rm=true --file docker/backupper/Dockerfile --tag=gas1121/backupper:backupper-test .
sudo docker build --rm=true --file docker/scheduler/Dockerfile --tag=gas1121/backupper:scheduler-test .

# create tempory dir to store combined coverage data
mkdir -p coverage/backupper
mkdir -p coverage/scheduler
sudo chown -R travis:travis coverage

# start target service for testing
sudo docker-compose -f travis/docker-compose.test.yml up -d

# waiting 10 secs
sleep 10

# run tests
sudo docker-compose -f travis/docker-compose.test.yml exec backupper ./run_tests.sh
sudo docker-compose -f travis/docker-compose.test.yml exec scheduler ./run_tests.sh
# get coverage data from container
sudo docker cp $(sudo docker-compose -f travis/docker-compose.test.yml ps -q backupper):/app/.coverage coverage/backupper
sudo docker cp $(sudo docker-compose -f travis/docker-compose.test.yml ps -q scheduler):/app/.coverage coverage/scheduler
# change path in coverage data
sudo sed -i 's#/app#'"$PWD"'/backupper#g' coverage/backupper/.coverage
sudo sed -i 's#/app#'"$PWD"'/scheduler#g' coverage/scheduler/.coverage
# combine coverage data
pip install coverage coveralls
cd coverage && coverage combine backupper/.coverage scheduler/.coverage
sudo mv .coverage ..
cd ..
sudo chown travis:travis .coverage
# send coverage report
coveralls

# spin down compose
sudo docker-compose -f travis/docker-compose.test.yml down

# remove 'test' images
sudo docker rmi gas1121/backupper:backupper-test
sudo docker rmi gas1121/backupper:scheduler-test
