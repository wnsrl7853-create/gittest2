FROM nginx:alpine
COPY web/ /usr/share/nginx/html/
# 컨테이너 포트 80
EXPOSE 80
