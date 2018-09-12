FROM alpine:latest
LABEL MAINTAINER='Evan Fagerberg <github.com/efagerberg'
ARG ROOT_PASSWORD=root

RUN apk update && \
    apk add openssh bash && \
    mkdir /var/run/sshd && \
    echo "root:${ROOT_PASSWORD}" | chpasswd && \
    sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
    ssh-keygen -A && \
    rm -rf /var/cache/apk/* /tmp/*

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e"]