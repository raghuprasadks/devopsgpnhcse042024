docker build -t my-flask-app-aws .
docker run -p 5000:5000 my-flask-app-aws
docker login
docker tag my-flask-app-aws:latest raghuprasadkonandur/my-flask-app-aws:latest
docker push raghuprasadkonandur/my-flask-app-aws:latest