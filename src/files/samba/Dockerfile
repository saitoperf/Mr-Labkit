FROM ubuntu
# FROM samba
COPY ./smb.conf /etc/samba/
COPY ./start.sh /work/
RUN apt-get update && \
    apt-get install -y samba  && \
    mkdir -p /home/lab/ && \
    chown -R nobody:nogroup /home/lab/ && \
    chmod -R 777 /home/lab/

ENTRYPOINT ["/work/start.sh"]