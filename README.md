# Backupper
Back up your data with a single docker container.

## Usage
+ copy **docker-compose.dev.yml** and rename to **docker-compose.yml**
+ add folder and docker named volume you want to backup to service **backupper**'s volume and make sure folder in container is in **/backup**
+ run **docker-compose run backupper bash**, in container run **bypy info** to authorize **bypy**, then exit
+ now you can either run **backupper** service or add it as a cron job
