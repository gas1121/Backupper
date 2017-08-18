# Backupper
Back up your data with docker.

## Usage
+ in data folder, copy **data.txt.example** and rename to **data.txt**
+ add new line to data.txt with syntax `folder_or_volume_name=folder`, where **folder_or_volume_name** is folder or named volume you want to backup, folder is the name of folder in container, which should not be conflict with each other
+ run **docker-compose run backupper bash**, in container run **bypy info** to authorize **bypy**, then exit
+ run **docker compose up -d scheduler** to start scheduler, and it will backup every week
