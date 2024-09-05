<img src="https://github.com/collinsmc23/tde101/blob/main/images/TD101-Logo.jpg" alt="The Threat Detections Engineering Project 101(2).png" width="800" height="300">

# 🔒 The Threat Detection Engineering 101 Project (TDE101)

In an attempt to teach myself and transition into "Threat Detections Engineering" side of the industry, I have scoped a new project.

There are two goals of this project.

1.  To teach myself how to deploy and manage a "simulated" detections engineering infrastructure.
2.  Deploy default detections, build custom detections, and maintain detection lifecycles while collecting data from threat feeds, custom honeypots, and a simulated threat environment.

The overall goal is to expose myself to what a "day in the life" might look like as an associate apart of the detections engineering team. Leveraging virtualization, affordable VPS / cloud hosting, and open-source tools, I will build my detections engineering lab. Based on the online sources, newsletter, and anecdotal lessons, here's the "lab" topology have drafted.

## The TDE101 Lab Topology

<img src="https://github.com/collinsmc23/tde101/blob/main/images/The%20Threat%20Detections%20Engineering%20Project%20101%20Netork%20Toplogy.png" alt="The Threat Detections Engineering Project 101(2).png" width="751" height="662">

### TDE101 Breakdown

Starting from the personal workstation to my honeypot network. Here is an overview of the tools I will be using.

- **Personal Workstation:** Used to login, configure, manage, and interface with the detections engineering infrastructure. Write custom detections based on which threat feed source I am using.  
- **Managed + Custom Detections:** Deploy custom detections to and manage the version lifecycle in a GitHub repository. By leveraging Git and hosting with the ubiquity of GitHub, I can keep track of custom detection version lifecycles.  
- **Detections as Code (DaC) AI Refinement Incubator:** Leverage the power of LLMs to summarize and supply refinements to custom detections. A custom integration between GitHub and LLM model of choice will exist to provide better refinement on detection code.  
- **GitHub Actions:** CI/CD pipeline used to deploy custom and vendor-managed detections to Elasticsearch.  
- **Elasticsearch:** Acts as the centralized SIEM to monitor, query, and build alerts based on log sources.  
- **Logstash:** Data processing and transformation agent used to send logs from threat feed sources.  
- **File Beats or Elastic Agent:** Agent deployed to collect logs in monitor-only mode. May play around with threat prevention capabilities in the Elastic agent. 
- **NGINX**: Used as a web server to access the ELK tenant.  
- **Honeypot Network:** Collect basic threat telemetry from various sources (probably going to be mostly bots). I will use a Digital Ocean droplet with the Docker Engine setting on top to host the three types of honeypots.
- **T-Pot**: Leverage the various pre-built honeypots provided in the T-Pot repository.  
- **SSH_HONEYPY:** A custom honeypot used to collect SSH attempts and shell interactions through emulated shell. This is a "mini-project" within TDE101 to help me continue to keep up with my Python skills.  
- **RDP**: Will simulate a Jumpbox environment with Remote Desktop Protocol (RDP) enabled. Not sure if I am going to configure the environment to be opened or closed and collect username / password pairs.  
- **Isolated Detection Generator:** Leveraging Red Canary's Atomic Red Team for pre-deployed, mapped tests to the MITRE ATT&CK framework, common "red team" activity will be managed and deployed in a Windows 11 VM. I will leverage this system as both a means to test my custom detections before deployment and test on triggered alerts.  
- **Security Alert**: When a detection has been triggered, alerts will be sent to email and visualized with Kibana.

### Center on Infrastructure as Code (Configuration Management)

A part of the goal of TDE101 is to build a minimal reproducible detections environment, in case I want to deploy this infrastructure a year or any time in the future. My plan is to center the Elasticsearch, Logstash, and Kibana (ELK) and the Isolated Detections Generator as code. Not sure on the specifics of how I am going to to this yet. I will start with Terraform for infrastucture provisonment. Ansible will be used to configure the ELK stack. 

# TDE101 Project

This GitHub repository will be continually updated as I progress through this project. My configuration management files, custom detection rules, and notes will be uploaded under folders with their respective names. 

### Project Timeline
August 2024 - November 2024

# Threat Detection Engineering Skills

Threat Detection Engineering can be defined in many ways. A security practitioner's role definition is dependent on several variables, including maturity of the environment, the area of expertise, and sub-categories.

What is a threat?

In the context of security, a threat is "an activity, deliberate, or unintentional, with the potential to cause harm to user, system, or entity."

In order to prevent and defend against known and unknown threats, a detection needs to be implemented. You can't defend against what you do not know. From a high-level, "detections" are logical rules which can be implemented to identify, alert, and protect against a threat.

I like this definition. "Detection engineering transforms an idea on how to detect a specific condition or activity into a concrete description of how to detect it."

The Threat detection engineering specialty is often associated with security monitoring, which is a collection and analysis of events. Events rely on data generation. These events can be compartmentalized into activity and states categories.

- Activity: The "What" and "How". What actions are systems, users, and processes taking.
    - Example: Malware is dropped onto the file system.
- States: The "Where". A current or change in a state's previous, present, or future.
    - Example: The local user is apart of the admin group.

🚀 Skills of a Successful Detections Engineer:

- Fundamental understanding of network protocols, operating systems, and applications.
- Well-versed in the overall attack chain, from potential threat to data breach. (MITRE ATT&CK & D3FEND)
- Working knowledge and implementation of attack tactics, techniques, and procedures (TTPS).
- Capable of parsing the necessary detail when analyzing TTPs.
- Knowledgeable in deploying and maintaining the necessary infrastructure to host and match detection rules.
- Capable of quantifying the lifecycle management of rules.
- Always attempting to stay up-to-date on the latest attacks and security preventions.
- Investigative in the probing for and uncovering hidden details.
- Approach data from multiple points of views.
    - Example: If a detection engineer is attempting to figure out ways to detect LSASS process dumping attacks, how can one do this? 1) Detect the usage of well-known process dumpers. 2) Detect suspicious access requests to the lsass.exe process. 3) Detect access form a process that should have never accessed lsass.exe before.

Threat Detection Engineering should focus on the thought process, skill, and ingenuity to approach the "threats" and "detections" piece from a unique perspective rather than an actual tool.

# Sources

This project would not have been made possible without inspiration. Here's a work in progress list of resources, inspirations, and articles.

- One of the first, original whitepapers to go public for outlining "Detections as Code" environment and its associated princicples: https://blog.soteria.io/detectors-as-code-b33e63baa2f0
- The article that started my inspiration: https://medium.com/threatpunter/from-soup-to-nuts-building-a-detection-as-code-pipeline-28945015fc38
- Detections Engineering Weekly - Fantastic, weekly newsletter with great resources and tidbits of information: https://www.detectionengineering.net/