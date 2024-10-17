# Install Windows 11 VM

A Windows 11 workstation with Atomic Red Team installed will simulate a "vulnerable user". By using Atomic Red Team, we can simulate various activity, which will generate logs. These logs can be used to write detection logic.

Use the following guide to provision a baseline Window 11 VM using VirtualBox. 

Choose Windows Enterprise Edition or Windows Pro for the best simulation of a business or enterprise workstation.

Guide: https://kfocus.org/wf/vbox-w11.html

### Vagrant via `VagrantFile` (IaC)
Vagrant is an open-source tool that simplifies the creation and management of virtualized development environments using configurable, reproducible, and portable workflows. Leveraging Vagrant via `VagrantFile`, the baseline Windows 11 instance can be provisioned. You will still need to disable Windows Defender, download your browser of choice, and Atomic Red Team.

Vagrant offers native support for VirtualBox, Hyper-V, and Docker.

Download Vagrant by following instruction in [Hashicorp Install Vagrant](https://developer.hashicorp.com/vagrant/tutorials/getting-started/getting-started-install?ajs_aid=dbd5115c-b144-49e3-bfc0-ca68e872595d&product_intent=vagrant).

Located in `/Configuration-Management-Files` --> Misc will be a file titled `Vagrantfile`. 

Follow the comments in the Vagrant file, you can customize hostname, password, VM name, etc.

Use the following commands to provision and destroy the VM provisioned by Vagrant.
- `vagrant init`: Initialize a new, blank `Vagrantfile` (if needed).
- `vagrant up [--debug]`: Used to provision new VM.
- `vagrant destroy`: Destroy VM.
- `vagrant resume`: Resume deployment if error or manual intervention happens.
- `--debug`: Use this flag for verbose stdout. Best used for error handling.

#### Vagrant Boxes
Vagrant leverages "Vagrant Boxes". These are base images for an environment or OS. HashiCorp provides support official boxes or Vagrant Cloud can be used. In the Vagrant File, I am using a custom box to deploy a baseline Windows 11 23H2 Enterprise edition. The HashiCorp supported boxes are not Windows, so I had to use a custom one by `gusztavvargadr` (thanks to ChatGPT). These boxes appear to be updated on a frequent basis.

#### Windows Subsystem For Linux (WSL)
*Source: https://dev.to/sfpear/vagrant-and-virtualbox-on-windows-11-and-wsl2-395p*

I am using WSL Ubuntu 22.04 as my main interface for this project (I don't want to use Windows...). If you are using something similar, follow the above source to change a few configuration options. Specifically...

```
export VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"
export PATH="$PATH:/mnt/c/Program Files/Oracle/VirtualBox"

export VAGRANT_WSL_WINDOWS_ACCESS_USER_HOME_PATH="/mnt/c/<path-to-folder-where-Vagrantfile-is>"
```

Add this line to your Vagrantfile to be able to have a project in your ubuntu file system:

config.vm.synced_folder '.', '/vagrant', disabled: true


# Configure Detection Generator

## Disable Windows Defender

In order to simulate malicious behavior without interruption, Windows Defender should be disabled. Windows Defender can be disabled through the Windows Security Settings, Group Policy Editor, and Command Line.

### Step 1 - Disable Powershell Script Prevention

Enter the following command, run Powershell as an Administrator.

`Set-ExecutionPolicy Bypass -Scope CurrentUser`
- Bypass the current execution policy in Powershell.

### Step 2 - Disable Virus Protection

![6472628b468b4b4ee7920ad1a0470a09.png](:/7f3f73d3e26e42a2ad654d4f8f14f910)

### Step 3 - Disable Realtime Monitoring

Enter the following commad, run Powershell as Administartor.

`Set-MpPreference -DisableRealtimeMonitoring $true`

### Step 4 - Disable Windows Defender Permanently

Windows Key + R -> `gepedit.msc`

Browse the following path: `Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus`, Double-lcik "Turn off Microsoft Defender Antivirus" policy, choose enable on radio button -> Apply.

### ❗ Permanently Disable Windows Defender
Because it's Microsoft, Windows Defender does not actually turn off the entire time.

To disable permanently, follow this guide: https://lazyadmin.nl/win-11/turn-off-windows-defender-windows-11-permanently/ 

# Atomic Red Team
*Source: https://aashishsec.medium.com/atomic-red-team-installation-2698b7bdc73b*
*Source: https://medium.com/mii-cybersec/microsoft-defender-for-endpoint-article-series-simulate-attack-with-atomic-red-team-e932a8a17271*
*Source: https://github.com/redcanaryco/invoke-atomicredteam/wiki/Installing-Invoke-AtomicRedTeam*

Atomic Red Team is an open-source project designed to test detection and response capabilities. It provides a small library of self-contained test ("atomics") that map directly to the MITRE ATT&CK framework. 

By using a selection of tests (T Codes), you choose the specific adversary technique you want to simulate. The tests are provided through the command-line. After executing the tests, you can review the logs and alerts generated by your security tools.

#### Sample Execution of Test

`Invoke-AtomicTest T1003.001`
- T1003.001: Simulates lateral movement using the `lssase.exe` process and Mimikatz.

## Download
*For Windows Environments*

💡
- Atomic Red Team comes bundled with the `Invoke-AtomicTest` powershell utility, which just installs the module. 
- The actual Atomic Tests are contained in the Atomics folder. Install the Atomics folder under the AtomicRedTeam folder for consistency.

### Step 1

Create new folder for AtomicRedTeam to be installed.
- ex. `C:\AtomicRedTeam\`

Exclude the file from Windows Defender AV scans.

`Add-MpPreference -ExclusionPath C:\AtomicRedTeam\`

### Step 2

Install Atomic Red Team with "[Invoke AotmicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam/wiki/Installing-Invoke-AtomicRedTeam)". 

Supply the command to install the Atomic Red Team module.

`Install-Module -Name invoke-atomicredteam,powershell-yaml -Scope CurrentUser`
- Download AtomicRedTeam Execution using PowerShell Gallery.

`IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1' -UseBasicParsing);
- Download AtomicRedTeam Execution without using PowerShell Gallery.

`Install-AtomicRedTeam -getAtomics -Force`
- Install the execution framework.
- The Atomic folder (`-getAtomics`) where the test definitions are contained.
