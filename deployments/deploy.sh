
clone_repo() {
    echo -n     "Enter Github Username: "
    read username
    echo -n "Enter Github Password: "
    read -s password
    echo 
    cd /home/ec2-user
    git clone https://$username:$password@github.com/Praneethct/DatabaseProject2.git
}


install_docker() {
    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
}


docker rm -f databaseproject2_alexa || echo "container not found"
[ -d "/home/ec2-user/DatabaseProject2" ] || clone_repo
cd /home/ec2-user/DatabaseProject2 && git pull origin
[[ `docker -v` ]] || install_docker
docker build -t databaseflaskapp2_alexa app
docker run --name databaseproject_alexa -p 5000:5000 -d databaseflaskapp2_alexa
