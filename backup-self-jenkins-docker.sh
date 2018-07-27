cd /var/jenkins_home; tar -zcvf /home/Documents/jenkins-docker-backup/jenkins-docker.tar.gz --transform 's,^\.,/var/lib/docker/volumes/jenkins-data/_data/,' . 
