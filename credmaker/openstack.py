#!/usr/bin/env python3

outfile = open('admin.rc', 'a')

print('What is the oa_auth_url?')
osauth = input()
print('export os_auth_url=' + osauth, file=outfile)

print('export os_identity_api_version=3', file=outfile)

print('What is the os_project_name?')
osproj = input()
print('export os_project_name=' + osproj, file=outfile)

print('What is the os_project_domain_name?')
osprojdom = input()
print('export os_project_domain_name=' + osprojdom, file=outfile)

print('What is the os_username?')
osuser = input()
print('export os_username=' + osuser, file=outfile)

print('What is the os_user_domain_name?')
osuserdom = input()
print('export os_user_domain_name=' + osuserdom, file=outfile)

print('What is the os_password?')
ospass = input()
print('export os_password=' + ospass, file=outfile)

outfile.close()

