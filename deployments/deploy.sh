
clone_repo() {
    echo -n     "Enter Github Username: "
    read username
    echo -n "Enter Github Password: "
    read -s password
    echo 
    git clone https://$username:$password@github.com/Praneethct/DataBaseProject.git
}


install_docker() {
    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
}


docker rm -f databaseproject
[ -d "DataBaseProject" ] ||clone_repo
[ docker -v ] || install_docker
docker build -t databaseflaskapp ../app
docker run --name databaseproject -p 80:80 -d databaseflaskapp
