# Backupper
[![Build Status](https://travis-ci.org/gas1121/Backupper.svg?branch=master)](https://travis-ci.org/gas1121/Backupper) [![Coverage Status](https://coveralls.io/repos/github/gas1121/Backupper/badge.svg?branch=master)](https://coveralls.io/github/gas1121/Backupper?branch=master) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gas1121/Backupper/master/LICENSE)

Back up your data with docker.

## Usage
+ in data folder, copy **data.txt.example** and rename to **data.txt**
+ add new line to data.txt with syntax `folder_or_volume_name=folder`, where **folder_or_volume_name** is folder or named volume you want to backup, folder is the name of folder in container, which should not be conflict with each other
+ run **docker-compose run backupper bash**, in container run **bypy info** to authorize **bypy**, then exit
+ run **docker compose up -d scheduler** to start scheduler, and it will backup every week
