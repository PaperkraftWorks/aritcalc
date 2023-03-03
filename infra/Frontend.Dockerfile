FROM node:alpine
RUN addgroup --g 1024 developer
RUN adduser -u 1024 -G developer -h /home/developer -D developer
WORKDIR /usr/bin/code
COPY frontend .
RUN npm install
