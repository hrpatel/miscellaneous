# This script shows you the steps for signing virtualbox kernel modules with 
# your own keys. This will allow you to use virtualbox with secureboot enabled

# Make a key to sign the module
openssl req -new -x509 -newkey rsa:2048 -keyout MOK.priv -outform DER -out MOK.der -nodes -days 36500 -subj "/CN=Descriptive name/"

# Sign the module with the newly generated key
for mod in vboxdrv vboxpci vboxnetadp; do
    sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 ./MOK.priv ./MOK.der $(modinfo -n ${mod})
done

# Import the key into the system
sudo mokutil --import MOK.der

# Reboot
echo "Reboot and run the following..."

echo "
# Load the modules
for mod in vboxdrv vboxpci vboxnetadp; do
    modprobe \${mod}
done

# Restart virtualbox
systemctl restart virtualbox.service
"

exit 0 

