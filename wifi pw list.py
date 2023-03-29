import subprocess

command = "netsh wlan show profiles"
output = subprocess.check_output(command, shell=True)
profiles = [i.split(":")[1][1:-1] for i in output.decode('utf-8').split("\n") if "All User Profile" in i]

for profile in profiles:
    command = f"netsh wlan show profile {profile} key=clear"
    output = subprocess.check_output(command, shell=True)
    output = output.decode('utf-8').split('\n')
    results = {}
    for line in output:
        if "User name" in line:
            results['User name'] = line.split(':')[1].strip()
        elif "Key Content" in line:
            results['Password'] = line.split(':')[1].strip()
    if results:
        print("-" * 50)
        print(f"Profile: {profile}")
        if 'User name' in results:
            print(f"User name: {results['User name']}")
        if 'Password' in results:
            print(f"Password: {results['Password']}")
