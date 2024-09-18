# Guide

In this step-by-step guide, you will install the Elasticsearch, Logstash, and Kibana services (ELK Stack) on Ubuntu Linux Server 22.04. The ELK tenant will be accessed through a baseline NGINX web server accessible through a publicly routed domain of your choosing. You will also enable and configure basic authentication (username and password) to lock access.

# Elasticsearch

*Source: https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elastic-stack-on-ubuntu-22-04#prerequisites*

### Step 1

Download Elasticsearch GPG Public Key and add it into APT.

`curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch |sudo gpg --dearmor -o /usr/share/keyrings/elastic.gpg`

`echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list`

### Step 2

Update APT's packages and install `elasticsearch`.

`sudo apt update`

`sudo apt install elasticsearch`

### Step 3

Change the `network.host:` to `localhost` in `/etc/elasticsearch/elasticsearch.yml` to bind the elasticsearch service to all interfaces.

💡 The `elasticsearch.yml` file provides configuration options for your cluster, node, paths, memory, network, discovery, and gateway. Most of these options are preconfigured. To edit the configuration, go to: `sudo nano /etc/elasticsearch/elasticsearch.yml`.

## Start Elasticsearch

`sudo systemctl start elasticsearch`: Start Elasticsearch service.  
`sudo systemctl enable elasticsearch`: Enable Elasticsearch to start up every time your server boots.  
`curl -X GET "localhost:9200"`: Query status of Elasticsearch.

# Kibana

It is recommended to install Kibana before Logstash.

👉 Ensure the Elastic package source in the previous step is added to the APT repository.

#### Step 1

Install Kibana with `sudo apt install kibana`.

#### Step 2

Enable the Kibana service to start up on boot. `sudo systemctl enable kibana`

### Step 3

Start Kibana service service `systemctl start kibana`.

💡 The `kibana.yml` file provides configuration options for Kibana. To edit the configuration file, go to: `/etc/kibana/kibana.yml`.

# Domain Name

In order to publicly access the ELK tenant, a domain name needs to be used.

I choose to use Cloudflare as my domain name registrar and management.

You must add your VPS public IP address as an `A` record to your root-level domain.

# NGINX

The NGINX engine can be used as a webserver, proxy, and load balancer. Download NGINX to serve the ELK stack tenant.

#### Step 1

Download NGINX with `sudo apt install nginx`.

#### Step 2

Create a server block file for your custom domain: `sudo nano /etc/nginx/sites-available/your_domain`.

#### Step 3

In the server block file, add the following to your configuration file, customize the `server_name` to your domain name.

```
server {

    server_name tde101.win www.tde101.win;

    location / {
        proxy_pass http://localhost:5601;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

}

```

#### Step 4

Enable the new configuration by creating a symbolic link (shortcut) to the `site-enabled` directory to point your configuration file.

`sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/your_domain`.

Run `sudo nginx -t` to ensure the configuration is okay. Move one when you see `syntax is ok` in the output.

#### Step 5

Reload the `nginx` service with `sudo systemctl reload nginx`.

#### Step 6

In order for traffic to connect to the web server, the uncomplicated firewall (UFW) should be enabled.

`sudo enable ufw`.

`sudo ufw allow 22` (❗ Make sure to add port 22 to not lock yourself out!)

Use the `Nginx Full` profile to allow both HTTP and HTTPS traffic through the firewall.

`sudo ufw allow 'Nginx Full'`

Kibana is now accessible through the domain or public IP address of your Elastic Stack server. You can check the status of Kibana by going to `http://your_domain/status`.

❗ Right now this environment is opened up to the Internet! Do not add log files or sensitive information. Follow the "Setup Basic Authentication on Elastic-Kibana" to set up a username and password.

# Logstash

#### Step 1

Install logstash with `sudo apt install logstash`.

💡 Logstash's configuration files reside in the `/etc/logstash/conf.d` directory.

# Set up Basic Authentication on Elastic-Kibana

Setting up basic authentication through minimal security (`xpack.security.enabled`). This setting enables commercial access to security features in Elastic. It allows you to lock down the ELK tenant with authentication and authorization. While also enabling "Fleet Management", where you can install the Elastic agent on your hosts (`xpack.security.authc.api_key.enabled`).

Enabling `xpack.security.enabled` also required users to authenticate before they can access Kibana. The authentication in Kibana integrates with Elasticsearch’s security, meaning Kibana users are authenticated against Elasticsearch's user database or external identity providers.

Resource:

- https://www.elastic.co/guide/en/elasticsearch/reference/current/security-minimal-setup.html

#### Step 1

Go to `/etc/elasticsearch/elasticsearch.yml`. Add the following lines at the very bottom on the configuration file.

```
# Enables the security features provided by the X-Pack Plugin, which is a set of commerical features included
# in Elasticsearch.
xpack.security.enabled: true

# Used to enable SSL/TLS.
xpack.security.transport.ssl.enabled: true

# This setting ensures that your node does not inadvertently connect to other clusters that might be running
# on your network.
discovery.type: single-node

# Must enable for "Fleet Management" feature.
xpack.security.authc.api_key.enabled: true
```

#### Step 2

To communicate with your cluster, you must configure a password for the default system accounts of `elastic` and `kibana_system`.

Navigate to `sudo /usr/share/elasticsearch/bin/elasticsearch-setup-passwords interactive`. Follow the prompts to set passwords for the build-in users. I used the same password for every single account, probably not a great idea in a production environment, but this is a lab sandbox.

#### Step 3

Next, configure the `kibana_system` account. This account is not meant for individual users and does not have permission to log in to Kibana from a browser. Instead, the `elastic` user will be used.

Add the `elasticsearch.username` setting to the `/etc/kibana/kibana.yml` file at the very end.

```
# This account performs background tasks and is not meant for individual use.
elasticsearch.username: "kibana_system"
```

#### Step 4

Create a new Kibana keystore with `sudo /usr/share/kibana/bin/kibana-keystore create`.

Add the `kibana_system` user to the Kibana keystore with `/usr/share/kibana/bin/kibana-keystore add elasticsearch.password`.

Restart the Kibana with `sudo systemctl restart kibana`.