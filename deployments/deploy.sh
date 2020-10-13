
clone_repo() {
    echo -n     "Enter Github Username: "
    read username
    echo -n "Enter Github Password: "
    read -s password
    echo 
    cd /home/ec2-user
    git clone https://$username:$password@github.com/Praneethct/DataBaseProject.git
}


install_docker() {
    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
}


docker rm -f databaseproject
[ -d "/home/ec2-user/DataBaseProject" ] || clone_repo
cd /home/ec2-user/DataBaseProject && git pull origin
[ docker -v ] || install_docker
docker build -t databaseflaskapp app
docker run --name databaseproject -p 80:80 -d databaseflaskapp
