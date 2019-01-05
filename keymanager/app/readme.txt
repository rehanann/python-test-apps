Data Structure:

password conf file:-

is_conf = [{
    "company_name" : "name",
    "nodes" : [
            {
            "app_name" : "jenkins",
            "ipaddress" : "10.0.0.1",
            "sub_dom_name" : "www.example.com",
            "allowes_user" : [
                {
                    "username" : "username",
                    "hash" : "if hash match with is_valid"
                },
                {
                    "username" : "username",
                    "hash" : "if hash match with is_valid"
                }
            ],
            "pass_conf" : {
                "keyname" : "name",
                "keypass" : "password"
            }
            "created_time" : "date and time"
        }
    ]
}]


in_keys = {
      "project_name" : "name",
      "initilize_time" : "duration of config data init",
      "created_time" : "date and time",
      "parent_dom" : "domain_name", 
      "nodes" : [
        {
            "app_name" : "name",
            "domain_name" : "www.example.com",
            "ipaddr" : "10.0.0.1",
            "user" : [
                {
                    "username" : "name",
                    "password" : true
                },
                {
                    "username" : "name",
                    "password" : true
                }
            ],
            "keys_bundle" : [
                {
                    "key_name" : "name",
                    "key_value" : "hash"
                    "cr_time" : "date time",
                    "mod_time" : "date time"
                },
                {
                    "key_name" : "name",
                    "key_value" : "hash"
                    "cr_time" : "date time",
                    "mod_time" : "date time"
                }
            ]
        }
        "create_time" : "date and time"
        ]
    }


user authentication file
primary key hash password map between is_conf and is_valid json.

is_valid = {

}






####################
Commands Readme:-
A. argparse

1. init config : 
app.py -i init --project="required" --domainname="optional" 

defaults: 
data in file
configuration created timer
configuration created date and time

required = project name

optional = domain name



2. json.




3. datetime




4. timer

####################