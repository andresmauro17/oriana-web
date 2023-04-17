# importa la imagen ubuntu version 10
FROM node:14

# copie el package json en usr/src
COPY ["app-ui/package.json", "/usr/src/"]

# haga un cd /usr/src
WORKDIR /usr/src

# instale las dependencioa
RUN npm install

# copie el package json en usr/src
COPY ["./app-ui", "/usr/src/"]

# exponga el puerto 3000
# EXPOSE 3000

# defino el comando por defecto que se ejecuta cuando le de run al contenedor
# CMD ["npx","nodemon", "index.js"]
