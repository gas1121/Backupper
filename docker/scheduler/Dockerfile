FROM library/python:3.6

ARG USE_MIRROR=0

# mirror setting

# use ustc mirrors if needed
COPY docker/set_mirror.sh /tmp/
RUN chmod +x /tmp/set_mirror.sh
RUN /tmp/set_mirror.sh $USE_MIRROR

# install docker
RUN apt-get update && apt-get install -y \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common \
     && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
     && apt-key fingerprint 0EBFCD88 \
     && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian \
     $(lsb_release -cs) stable" \
     && apt-get update && apt-get install -y docker-ce

# install requirements
RUN mkdir -p /app
RUN mkdir -p /sync
COPY scheduler /app
COPY docker/run_tests.sh /app
RUN chmod +x /app/run_tests.sh
WORKDIR /app
RUN pip install -r requirements.txt

CMD python run.py
