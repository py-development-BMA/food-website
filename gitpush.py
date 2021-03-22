import os
import time
f = open("git_save_info.txt", "r")
users_branch = f.read()
f.close()
if users_branch == "":
	f1 = open('git_save_info.txt', 'w')
	wtw = input('Input your branch name: ')
	f1.write(wtw)
	f1.close()
	users_branch = wtw
else:
	pass
reponame = 'food-website'
message = input('Input your comment: ')
os.system('git add --all')
os.system('git commit -a -m "{0}"'.format(message))
time.sleep(1)
print('SYNC.')
time.sleep(1)
os.system('git push -u origin {0}'.format(users_branch))
print("SUCCESS!")
