
#!/bin/bash
ifconfig eth0 down && sleep 180 && ifconfig eth0 up && sleep 20
echo "networ_normal"