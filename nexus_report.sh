#!/bin/bash
passw=phani@557

help(){
    echo """    The way you executed script is wrong
    The script options are count, hosted and proxy
    Example to run script are ./nexus_report.sh count """
    exit 130
}
if [ "$1" = "count" ]
then
    curl -s -u admin:${passw} -X 'GET' 'http://44.206.237.64:8081/service/rest/v1/repositorySettings' -H 'accept: application/json' | jq .[].name | wc -l
elif [ "$1" = "hosted" ]
then
    echo "Hosted Repo Name(s)"
    curl -s -u admin:${passw} -X 'GET' 'http://44.206.237.64:8081/service/rest/v1/repositorySettings' -H 'accept: application/json' | jq ' .[] | select ( .type == "hosted" ) | .name' | sed 's/"//g'
elif [ "$1" = "proxy" ]
then
    echo "Proxy Repo Name(s) , Proxy Repo URL(s)"
    curl -s -u admin:${passw} -X 'GET' 'http://44.206.237.64:8081/service/rest/v1/repositorySettings' -H 'accept: application/json' | jq ' .[] | select ( .type == "proxy" ) | .name + " , " + .url' | sed 's/"//g'
elif [[ "$1" = "admin" && "$2" = "mrc" ]]
then 
    echo "PLEASE ENTER MAVEN REPO NAME"
    read repo
    sed -i 's/reponame/$repo/g' post.json
    curl -s -u admin:${passw} -d @post.json -X 'POST' 'http://44.206.237.64:8081/service/rest/v1/repositories/maven/hosted' -H 'accept: application/json'
    if [ $? -eq 0 ]
    then
        echo "Repo creation successful"
    else
        echo "Repo creation failed"
    fi
    sed -i 's/$repo/reponame/g' post.json
else
    help
fi
