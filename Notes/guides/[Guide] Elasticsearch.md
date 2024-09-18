# General Overview / Notes


# Guide
# Fleet Server
## Install Fleet Server
*Sources: https://www.elastic.co/guide/en/fleet/7.17/add-a-fleet-server.html*

Fleet server allows you to deploy, manage, and maintain your Elastic agents as they are deployed to various hosts. 

Fleet server operates and listens on port `8220` by default. 

The communication path between a system with an Elastic agent, Fleet server, and ELK Tenant uses the following by default:

`Host ---> Fleet-Server:8220 --> Elasticsearch:9200`

💡 The Fleet server is installed and run as an Elastic agent. Fleet server and elastic agents can not run on the same system. This guide assume Fleet server will be installed on the ELK tenant.

### Step 1

Download the Elastic agent in the home folder, extract the contents.

`curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-7.17.23-linux-x86_64.tar.gz`

`tar -xvf elastic-agent-7.17.23-linux-x86_64.tar.gz`.

### Step 2

Navigate to Management ➡ Fleet ➡ Agent.

Walk through each of the steps, make sure to add the public IP address of your server / VPS.

💡 Use `http` for Fleet server.

<img src=":/bb06dc4d0a45460e9d151f973ba6506c" alt="27dc0bb29e470fa0d20d800af8802c44.png" width="493" height="772">

### Step 3

Navigate back to ELK server, use the following command generated from the instructions above to install Fleet Server.

### Step 4

Inside 

## Edit Fleet Server Configuration
Hosts need to contact a publicly routable public IP address with:
- Fleet Server listening on port 8220.  
- Elasticsearch listening on port 9200.

Perform the following steps.

### Step 1

Navigate to Management ➡ Fleet ➡ Fleet settings.

Add ELK tenant public IP address with `http` and the default ports.

![5aae4e1bb7970e8ce354859bcf515d62.png](:/0da19c7f930a4cc093ba4eb18a232aa1)

### Step 2

SSH into ELK tenant. 

Allow port `8220` and `9200` with uncomplicated firewall.

`ufw allow 8220 9200`.

# Ingest Data

### Step 1

Log into host where the agent will be installed.

### Step 2
*Follow Agent Wizard.*

Go to "Add Agent".  

Choose agent policy (default policy). 

### Step 3

Download Elastic Agent based on OS type.
- https://www.elastic.co/downloads/past-releases/elastic-agent-7-17-23 

`curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-7.17.23-linux-x86_64.tar.gz`

Unzip: `tar -xvf elastic-agent-7.17.23-linux-x86_64.tar.gz`

### Step 4 

Make sure you are in the directory where the agent is installed. 

`cd ../elastic-agent-7.17.23-linux-x86_64`

Use the supplied install command with `http` as the fleet server, enrollment token, and `--insecure` to install the agent.

`sudo ./elastic-agent install --url=http://{public-ip-address}:8220 --enrollment token={token} --insecure`

Ensure `elastic-agent.service` is running.

`systemctl status elastic-agent.service`.

### Step 5

Navigate to ELK tenant. 

You should see a new host with the host name. Click the host name.

![e0054f771d6046113d98abfc2ebfe452.png](:/599d7cd411e94b6e840e33a89d5d9bce)

Go to Logs to ensure logs are being ingested.

![8874d7d476b08da1bb298ff89e00dff1.png](:/44de284f63d54d8f9fac0208c7b97f4e)

# Commands

`/usr/share/elasticsearch/bin/elasticsearch --version`: View current version of Elasticsearch.