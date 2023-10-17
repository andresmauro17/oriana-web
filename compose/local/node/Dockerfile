# importa la imagen node
FROM node:18.18

# copie el package json en usr/src
COPY ["./vue-project/package.json", "/usr/src"]

RUN mkdir /usr/src/vue-project
RUN mv /usr/src/package.json /usr/src/vue-project


# haga un cd /usr/src
WORKDIR /usr/src/vue-project

# instale las dependencioa
# RUN pwd
RUN npm install

