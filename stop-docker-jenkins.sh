docker stop $(docker ps | grep jenkinsci | awk '{print $1}')
