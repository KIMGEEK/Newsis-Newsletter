FROM node:latest as build-stage

WORKDIR /docker/Newsis-Newsletter/WEB/Front-end

COPY package*.json .

COPY . .

RUN npm install

RUN npm install --save axios
RUN npm run build

FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build-stage /docker/Newsis-Newsletter/WEB/Front-end/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
