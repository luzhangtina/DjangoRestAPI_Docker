FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=nonintercative

# Install toolkits, apache2 and libapache2-mod-wsgi-py3
RUN apt-get update
RUN apt-get install -y apt-utils vim curl wget unzip apache2 apache2-utils libapache2-mod-wsgi-py3 alien stunnel

# Install oracle client and libaio1
RUN wget https://download.oracle.com/otn_software/linux/instantclient/19800/oracle-instantclient19.8-basic-19.8.0.0.0-1.x86_64.rpm && \
    alien -i oracle-instantclient19.8-basic-19.8.0.0.0-1.x86_64.rpm && \
    apt-get install -y libaio1

ENV LD_LIBRARY_PATH="/usr/lib/oracle/19.8/client64/lib:${LD_LIBRARY_PATH}"

# Install python3 and pip3
RUN apt-get install -y python3
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN ln /usr/bin/pip3 /usr/bin/pip

# Upgrade pip
RUN pip install --upgrade pip

# Ensure that the python output is sent straight to terminal without buffered
ENV PYTHONUNBUFFERED 1

# Install python libraries
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
RUN rm -f /requirements.txt

# Copy our project code to /var/www/micApiApp
RUN mkdir /var/www/micApiApp
COPY ./src/ /var/www/micApiApp/

# Set up apache2 configuration
RUN rm -f /etc/apache2/sites-available/000-default.conf
RUN rm -f /etc/apache2/sites-enabled/000-default.conf
ADD ./api_server.conf /etc/apache2/sites-available/api_server.conf
RUN a2ensite api_server
# RUN a2enmod ssl
# RUN a2enmod rewrite

# Expose container port 80
EXPOSE 80

# Start apache2 server when the container starts
CMD ["/bin/bash", "/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
