#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json
import os
import sys
from Instance import Instance
from urlparse import parse_qs

reserved_words = ['role','network']

roles =[]
groups = []
networks=[]
domains = []
rules = []

parsed_rules=[]

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("True")
		return

	def do_POST(self):
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data

		print self.headers
		post_data = self.rfile.read(content_length)
		#print "Path: ", str(self.path)

		request = (parse_qs(post_data))
		#print request
		auth = self.process_request(self.path, request, "POST")

		self.send_response(200)
		self.end_headers()
		self.wfile.write(auth)
		return

	def process_request(self, path, request, type):

		credentials =  json.loads(request["credentials"][0])
		#print "credentials"
		#print credentials

		target = json.loads(request["target"][0])
		#print target

		user = credentials.get("user_name")
		#print user

		role = credentials.get("roles")[0]
		#print role

		id = target.get("id")
		#print id

		attempted_operation = path.split("/")[1]
		attempted_operation_subtype = path.split("/")[2]
		#print "Subype: ", attempted_operation_subtype

		for i in range(len(parsed_rules)):
			if user == parsed_rules[i]["user"]:
				#print "found user"
				for j in range(len(parsed_rules[i]['permissions']['operations'])):
					if ((attempted_operation == "update") and (parsed_rules[i]['permissions']['operations'][j] == "delete" or parsed_rules[i]['permissions']['operations'][j] == "modify")):
						#The user can perform the operation, but gotta check if can perform on THAT resource
						#print "found operation"
						for k in range(len(parsed_rules[i]['permissions']['resources'])):
							print parsed_rules[i]['permissions']['resources'][k].__dict__
							print parsed_rules[i]['permissions']['resources'][k].id
							if id == parsed_rules[i]['permissions']['resources'][k].id:
								return "True"
							if parsed_rules[i]['permissions']['resources'][k].type == "network":
								for l in range(len(parsed_rules[i]['permissions']['resources'][k].members)):
									if id == parsed_rules[i]['permissions']['resources'][k].members[l].id:
										return "True"
		return "False"


def get_instances(members_names, instances_list):
	instances = []
	for i in range(len(members_names)):
		a_name = members_names[i]
                #an_id=os.popen("nova list | grep " + a_name + " | awk '{print $2}'").read().split("\n")[0]
		an_id = get_object_id(instances_list, a_name)
                instance = Instance(a_name, an_id)
                #print instance.__dict__
                instances.append(instance)

	return instances


def testing():
	network_list = os.popen("openstack network list").read().split("\n")
	for i in range(len(network_list)):
		print network_list[i]

	id = get_object_id(network_list, "field")
	print "field id ", id

	id = get_object_id(network_list, "supervisory")
	print "supervisory id ", id


def get_object_id(object_list, object_name):
        for i in range(len(object_list)):
                a_line=object_list[i].split(" ")
                if len(a_line) > 2:
			if a_line[3] == object_name:
				return a_line[1]



def parse_policy_file():

	network_list = os.popen("openstack network list").read().split("\n")
	instance_list = os.popen("nova list").read().split("\n")

	policy_file = open(sys.argv[1], 'r')
	#policy_file = open("high_policy.pl", 'r')
	lines = policy_file.readlines()

	for line in lines:

		if line[0]!="#":
			if line.split(":")[0]=="role":
				# We found a new role, add it to the list
				role_permissions = dict()
				role_permissions["name"] = line.split(":")[1].split("(")[0]
				operations_str = line.split(":")[1].split("(")[1].split(")")[0]
				role_permissions["operations"] = [x.strip() for x in operations_str.split(',')]
				roles.append(role_permissions)
			elif line.split(":")[0]=="network":
				# We found a new network, add it to the list
				name = line.split(":")[1].strip().split("(")[0].strip()

				#toDo: We should optimize this and only run openstack commands once

				#id=os.popen("openstack network list | grep " + name + " | awk '{print $2}'").read().split("\n")[0]
				id = get_object_id(network_list,name)
				print "network id ", id
				members_names = [x.strip() for x in line.split(":")[1].split("(")[1].split(")")[0].split(',')]
				members = get_instances(members_names, instance_list)
				instance = Instance(name, id, "network", members)
				print "NETWORK"
				print instance.__dict__
				networks.append(instance)
			else:
				#Everything else is considered an alias
				if line.find("(")== -1:
					# This is an alias used to group a set of entities
					group=dict()
					group["name"] = line.split(":")[0].strip()
					members_names = [x.strip() for x in line.split(":")[1].split(",")]
					group["members"] = get_instances(members_names, instance_list)
					groups.append(group)
				#This is either a domain or a role rule
				else:
					if line.find(":") == -1:
					# This is a domain
						domain=dict()
						domain["name"] = line.split("(")[0].strip()
						domain["members"] = [x.strip() for x in line.split("(")[1].split(")")[0].split(',')]
						domains.append(domain)
						print "DOMAIN"
						print domain
					else:
					# This is a role rule
						rule=dict()
						rule["name"] = line.split(":")[0].strip()
						rule["role"] = line.split(":")[1].split("(")[0].strip()
						rule["resource"] = []
						rule["resource"].append(line.split(":")[1].split("(")[1].split(")")[0].strip())
						rules.append(rule)
						print "RULES"
						print rule

	policy_file.close()

def extract_domains(a_domain):
	resources=[]
	print "processed domain"
	print a_domain
	for i in range(len(networks)):
		for j in range(len(a_domain['members'])):
			if a_domain['members'][j] == networks[i].name:
				resources.append(networks[i])
	return resources

def build_rules():
 	# This method should build a structure concerning the rules of each of the roles
	# A rule is a composition in which resources are grouped and over them operations are authorized
	#resource_list = []
	for i in range(len(rules)):
		rule=dict()
		rule['user']=rules[i]['name']
		rule['role']=rules[i]['role']
		rule['permissions']=dict()

		for j in range(len(roles)):
			if roles[j]['name'] == rule['role']:
				operations = roles[j]['operations']
		if operations:
			rule['permissions']['operations'] = operations

		resource_list=[]

		for j in range(len(domains)):
			if domains[j]['name'] in rules[i]['resource']:
				some_resources = extract_domains(domains[j])
				for k in range(len(some_resources)):
					resource_list.append(some_resources[k])
		if resource_list:
			rule['permissions']['resources']=resource_list
			for k in range(len(rule['permissions']['resources'])):
				print "resources"
				print rule['permissions']['resources'][k].__dict__

		else:
			for j in range(len(networks)):
				if networks[j].name in rules[i]['resource']:
					resource_list.append(networks[j])
			rule['permissions']['resources']=resource_list

                        for k in range(len(rule['permissions']['resources'])):
                                print "network resources"
                                print rule['permissions']['resources'][k].__dict__


		print "Rule"
		print rule
		parsed_rules.append(rule)


#testing()
parse_policy_file()
build_rules()

try:
	#Create a web server and define the handler to manage the incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started http server on port ' , PORT_NUMBER
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
