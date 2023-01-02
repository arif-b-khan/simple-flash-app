import subprocess

print("Starting code deploy")
repoPath= 'https://github.com/arif-b-khan/simple-flash-app.git'
ot = subprocess.Popen(['git', 'clone', str(repoPath), 'src'])
(out, error) = ot.communicate()
print("Source code pulled")

print("Output: {}".format(out))
print("Error: {}".format(error))