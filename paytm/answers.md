
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
- Nodes have at least a 1Gb NIC

Overall solution is based on DHCP/PXE/TFTP (razer-server: https://github.com/puppetlabs/razor-server)
- support for bare-metal and virtual nodes
- Able to support multiple distributions
- policy based provisioning
- ability to handoff to configuration management


Time for 1000 nodes: 1-2 weeks
Time for 10000 nodes: 5-6 weeks

Q3
-
Design Considerations
- Multi-thread support (parallel execution)
  - Asynchronous execution
- Support for passwordless authentication (e.g. SSH keys)
- Advanced logging
  - i.e. separate logs for standard and error output

### Q4

### Q5

### Q6

### Q7
