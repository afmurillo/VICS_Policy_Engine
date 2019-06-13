# Definition of roles
role:owner(create, delete, modify, show)
role:operator(modify,show)
# Definition of VICFS
sensors: lit101, lit201, ph201, fit201 
actuators: p101, mv101, p201 
plcs: plc101, plc201 
network: field(sensors, actuators, plcs) 
scada:scada_1 
historian:historian_1 
network: supervisory(scada, historian)
#Virtual ICS definition
virtual_ics(supervisory, field)
#Definition of users permissions
operator_blue:owner(virtual_ics)
operator_red:operator(supervisory)
