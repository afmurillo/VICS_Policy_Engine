#!/bin/bash

openstack keypair create --public-key ~/.ssh/id_rsa.pub $1-key

ips=(10.15.1.10 10.15.1.11 10.15.1.12 10.15.1.13 10.15.1.14 10.15.1.19 10.15.1.20)
names=(lit101 q101 q301 plant101 plc101 plc301 lit103)

openstack network create $1
openstack subnet create $1-subnet --network $1 --subnet-range 10.15.1.0/24

network_id=$(openstack network list | grep field | awk '{print $2}')
echo $network_id

for i in {0..5}
do
    openstack floating ip create public
done

openstack router create field-router
openstack router set field-router --external-gateway public
openstack router add subnet field-router field-subnet

for i in {0..5}
do
    nova boot --flavor cirros256 --image cirros-0.4.0-x86_64-disk --nic net-id=$network_id,v4-fixed-ip=${ips[i]} --key-name $1-key ${names[i]}
done

for i in {4..9}
do
    floating[$i-4]=$(openstack floating ip list | head -n $i | tail -n -1 | awk '{print $ 4}')
    echo ${floating[i]}
done

for i in {0..5}
do
    openstack server add floating ip ${names[i]} ${floating[i]}
done

