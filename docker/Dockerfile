FROM library/python:3.6

ARG USE_MIRROR=0

# mirror setting

# use ustc mirrors if needed
COPY docker/set_mirror.sh /tmp/
RUN chmod +x /tmp/set_mirror.sh
RUN /tmp/set_mirror.sh $USE_MIRROR

# os setup
RUN apt-get update && apt-get install -y p7zip-full

# install requirements
RUN mkdir -p /app
RUN mkdir -p /sync
COPY backupper /app
COPY docker/run_tests.sh /app
RUN chmod +x /app/run_tests.sh
WORKDIR /app
RUN pip install -r requirements.txt

CMD python run.py
