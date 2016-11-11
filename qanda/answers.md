
_This repo is public so I didn't repeat the questions here._

Q1
-
Assumptions
- Bare minimum OS is installed/configured
- Root access is available via SSH

Overall solution is to use Chef
- bootstarp the nodes using knife
   - setting up and validate with Chef Server
   - install/configure/run chef-client
- configure/maintain the nodes using chef-client
  -  use chef-client daemon to keep the host compliant to defined configuration
- use Chef Server and/or ohai (on the node) to monitor and report the status of the nodes

Q2
-
Assumptions
- Physical networking is setup/connected
- Nodes have at least a 1 Gb NIC
- DHCP/TFTP/PXE is setup, configured and validated

Overall solution is based on DHCP/PXE/TFTP (razer-server: https://github.com/puppetlabs/razor-server)
- support for bare-metal and virtual nodes
- Able to support multiple distributions
- policy based provisioning
- supports handoff to configuration management

Time for 1000 nodes: 1-2 weeks, 10000 nodes: 5-6 weeks

Q3
-
Design Considerations
- Multi-thread support (parallel execution)
  - Asynchronous execution
- Support for passwordless authentication (e.g. SSH keys)
- Advanced logging
  - i.e. separate logs for standard and error output

Q4
-
Possible Solutions
- Manage user accounts, keys, security hardening with configuration management (e.g. Chef)
- Install/configure single sign-on with existing identity solution (e.g. using sssd with LDAP/Active Directory)


---
**_Please note that I don't have hands-on experience with Hadoop/HDFS (Namenode HA), Hive or Yarn. I researched those technologies to answer the questions below._**

Q5
-
Zookeepr or ZKFC failure will result in a failure to trigger a failover. Initiate a manual failure to restore HA then you can investigate and correct any issues with Zookeeper or ZKFC. 

Q6
-
User Joe will get a permission error trying to execute the select statement since he is not authorized to access the underlying storage layer. 

Q7
-
It is possible to limit queue capacity that any single user can consume by setting the 'user-limit-factor' or 'user-limit' to a value less than 1. E.g. a value of 0.5 would restrict 'Joe' from using resources beyond half of the queue capacity allowing others to utilize the queue.
