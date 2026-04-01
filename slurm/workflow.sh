docker build -t ai-education -f docker/Dockerfile . 
docker tag ai-education controller-ip:5000/
ai-education 
docker push
controller-ip:5000/
ai-education
