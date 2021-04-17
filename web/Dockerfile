# этап сборки (build stage)
FROM node:14.15.0-alpine as build
WORKDIR /app
COPY package.json ./
RUN npm install
RUN ls -l
COPY . .
RUN npm run build

FROM nginx:stable-alpine as runtime
COPY --from=build /app/build /app
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
