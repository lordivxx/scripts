nohup docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home -v /etc/timezone:/etc/timezone -v /etc/localtime:/etc/localtime jenkinsci/blueocean &

