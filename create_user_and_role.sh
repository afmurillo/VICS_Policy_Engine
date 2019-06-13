# Params: project name, user name, role name, user password
# Get the domain ID
openstack project list | grep $1 |head -n 1 | awk '{print $2}'
openstack user create --project $1 --password $4 $2
openstack role create $3
user_id=$(openstack user list | grep $2 | awk '{print $2}')
role_id=$(openstack role list | grep $3 | awk '{print $2}')
project_id=$(openstack project list | grep $1 | head -n 1 | awk '{print $2}')

openstack role add --user $2 --project $1 $3
