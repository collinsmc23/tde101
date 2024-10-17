# General Overview / Notes

Elasitcsearch is an open-source RESTful, distributed search and analytics engine built on Apache Lucene. Commonly used for data anlaytics, full-text search, security intelligence (yay security!), business analytics, and operational intelligence.

Elastic Index: A collection of documents in Elasticsearch. An index is the fundamental data storage unit where Elasticsearch stores and organizes data for search and analytics. Think of an Elasticsearch index as a place where information is searchable. 

Elastic Mappings: An index has a schema known as a "mapping" which defines the structure of the documents, including the field names and data types (text, date, number).
- Elasticsearch is schema-less, meaning it will automatically map and create a schema based off of the data. It's best practice to explicitly define a schema if you know it.

Shards and Replicas (Self-hosted): Indices are divided into smaller units called shards to distribute data across nodes in a cluster. Shards improve scalability and performance. Replicas are copies of shards for data redundancy and high availability.
- 💡 Elastic and AWS provide cloud-hosted solutions.

Data Stream: Stores time series, append-only data which are used to store the data backing an index. Data streams provide automatic, out-of-the-box optimized data rollover strategy to remain well-balanced across shards and indexes (as opposed to creating indexes manually each time).

Index Pattern: Used for Discover to query for an index. An index pattern is the some name as the original index name.

# Commands
To interface with the Elasticsearch cluster, using the RESTful API can streamline and optimize creation of various Elastic artifacts (indexes). 

Kibana provides a useful interface under Management -> Dev Tools.

Here are some useful commands.

`PUT /my_index_name`: Create an index.

`GET _cat/indices?v`: List index names and their basic information.

`GET my_index_name/_search`: Query an index.

`DELETE my_index`

```
PUT /my_index_name?pretty
{
    "settings" : {
        "number_of_shards" : 2,
        "number_of_replicas" : 1
    },
    "mappings" : {
        "properties" : {
            "tags" : { "type" : "keyword" },
            "updated_at" : { "type" : "date" }
        }
    }
}
```
- Issue settings for mappings and replicas.

# Guides

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

<img src=":/bb06dc4d0a45460e9d151f973ba6506c" alt="27dc0bb29e470fa0d20d800af8802c44.png" width="493" height="772" class="jop-noMdConv">

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