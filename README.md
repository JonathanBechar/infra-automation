# Infra Automation project

### A simulated AWS EC2 provisioning tool built with python and bash

This project simulates the creation of EC2 instances, and post-provisioning configuration (nginx install).  
All infrastructure data is stored locally in a JSON file.

## How to install

In the command line:  
git clone https://github.com/JonathanBechar/infra-automation

## How it works

1. User chooses whether to list the existing instances or to create a new one using the CLI (create / list. Default is create)
2. User provides basic instance details via CLI
3. The system enriches the data with the following:
    - InstanceId
    - VpcId
    - PublicIpAddress
    - State
4. Pydantic validates the full data of the instance
5. Data is stored in "configs/instances.json"
6. Logs are sent to "logs/provisioning.log"
7. The system simulates the running of a bash script that installs nginx

## Virtual Environment

It is recommended to run this project inside a virtual environment. 

### Activate Environment:  

In the command line:  
Mac/Linux - $ source .venv/bin/activate
Windows - $ .venv\scripts\activate

### Install Dependencies:

In the Command line:  
(.venv) $ pip install -r requirements.txt

### Deactivate Environment

In the command line:  
(.venv) $ deactivate

## Usage

1. Enter infra-automation directory
2. In the command line:  
    - (.venv) $ python infra_simulation.py list -> lists the existing instances
    - (.venv) $ python infra-automation create -> enables input for instance creation

