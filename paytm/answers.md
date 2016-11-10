
### Q1
Assumptions
- Bare minimum OS is installed/configured
- Root access is available via SSH

Overall solution is to use Chef
- bootstarp the nodes using knife
   - setting up and validate with Chef Server
   - install/configure/run chef-client
- configure/maintain the nodes using chef-client
  -  use chef-client daemon to keep the host compliant to defined configuration
- use Chef Server and/or ohai (on the node) to monitor the status of the nodes

### Q2

### Q3

### Q4

### Q5

### Q6

### Q7
