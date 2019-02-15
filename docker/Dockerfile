FROM python

USER root

LABEL maintainer="mihai.ghidoveanu@gmail.com"

WORKDIR root

COPY ./Requirements.txt /root/

CMD /bin/bash

RUN apt-get -yqq update && \
    apt-get install -yqq screen tmux python python-dev python-pip python-virtualenv && \
    apt-get clean && \
    # install python requirements
    pip install --trusted-host pypi.python.org -r Requirements.txt && \
    # remove temporary files
    rm -rf /var/lib/apt/lists/# && \
    rm -rf /tmp/# && \
    rm -f /root/Requirements.txt 




