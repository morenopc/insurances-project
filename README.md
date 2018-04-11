# Insurances Project

Product Development Project

## Model Classes Relationship Diagram

![models class](https://github.com/morenopc/insurances-project/raw/master/media/img/2018-02-BriteCore-entity-relationship-diagram.jpg "Model Classes Relationship Diagram")

## Issue

To work mostly with property-based insurance, the data model is pretty rigid. The data model assumes that all risks are properties and have addresses. This makes it difficult to work with different forms of insurance like Automobile Policies, Cyber Liability Coverage (protection against hacking), or Prize Insurance (if someone gets a $1 million hole-in-one prize at a golf tournament, the golf course doesn't pay it, they have an insurance policy to cover them).

## Approach

A solution that allows insurers to define their own custom data model for their risks. There should be no database tables called automobiles, houses, or prizes. Instead, insurers should be able to create their own risk types and attach as many different fields as they would like.

Fields are bits of data like first name, age, zip code, model, serial number, Coverage A limit, or prize dollar amount. Basically any data the carrier would want to collect about the risk. Fields can also be of different types, like text, date, number, currency, and so forth.

### Backend

Django REST API

### Frontend

Vue.js

### Server (less)

AWS Lambda using Zappa

## Local Environment

```
ubuntu 17.04 (4.10.0-42-generic)
python 2.7.13
docker version 17.12.0-ce, build c97c6d6
```

## Docker Environment

```
Amazon Linux AMI 2017.03
```

## Virtual Environment

```
pip 9.0.1
virtualenv 15.1.0
python 2.7.12
django 1.11.10
zappa 0.45.1
```

## Install Docker CE

```
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    Software-properties-common
```

Add Docker’s official GPG key:
```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Verify that the key fingerprint is 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88.
$ sudo apt-key fingerprint 0EBFCD88
pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22
```

Use the following command to set up the stable repository (for the amd64 architecture):
```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

$ sudo apt-get update
$ sudo apt-get install docker-ce
```

## Zappa
Fix permission denied issue
```
sudo usermod -a -G docker $USER
```

For Python 2.7 projects
```
$ docker pull lambci/lambda:build-python2.7
```

```
$ vi ~/.aws/credentials

[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key

[zappa]
aws_access_key_id = <aws_access_key_id>
aws_secret_access_key = <aws_secret_access_key>
```

```
$ alias zappashell2='docker run -ti -e AWS_PROFILE=zappa -v $(pwd):/var/task -v ~/.aws/:/root/.aws  --rm lambci/lambda:build-python2.7 bash'
alias zappashell2 >> ~/.bashrc
```

Dockerfile:
```
FROM lambci/lambda:build-python2.7

MAINTAINER "Moreno Cunha" <moreno.pinheiro@gmail.com>

WORKDIR /var/task

# Fancy prompt to remind you are in zappashell
RUN echo 'export PS1="\[\e[36m\]zappashell>\[\e[m\] "' >> /root/.bashrc

# Additional RUN commands here
# RUN yum clean all && \
#    yum -y install <stuff>

CMD ["bash"]
```

### Build django zappa
```
$ docker build -t django-zappa .

$ zappashell
zappashell> virtualenv env
New python executable in /var/task/env/bin/python
Installing setuptools, pip, wheel...done.
zappashell> source env/bin/activate

$ django-admin startproject insurances .
```

## Status
```
(venv) zappashell> zappa status dev
Status for task-dev: 
    Lambda Versions:      3
    Lambda Name:          task-dev
    Lambda ARN:           arn:aws:lambda:us-east-1:469551400186:function:task-dev
    Lambda Role ARN:      arn:aws:iam::469551400186:role/task-dev-ZappaLambdaExecutionRole
    Lambda Handler:       handler.lambda_handler
    Lambda Code Size:     11250825
    Lambda Version:       $LATEST
    Lambda Last Modified: 2018-02-07T02:12:28.361+0000
    Lambda Memory Size:   512
    Lambda Timeout:       30
    Lambda Runtime:       python2.7
    Lambda VPC ID:        None
    Invocations (24h):    0
    Errors (24h):         0
    Error Rate (24h):     Error calculating
    API Gateway URL:      https://owduy09pr0.execute-api.us-east-1.amazonaws.com/dev
    Domain URL:           None Supplied
    Num. Event Rules:     1
    Event Rule ARN:       arn:aws:events:us-east-1:469551400186:rule/task-dev-zappa-keep-warm-handler.keep_warm_callback
    Event Rule Name:      task-dev-zappa-keep-warm-handler.keep_warm_callback
    Event Rule State:     Enabled
    Event Rule Schedule:  rate(4 minutes)
```

### Run server
```
(venv) zappashell> python manage.py runserver
```
