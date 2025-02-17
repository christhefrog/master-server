import subprocess

submodule_update_command = "git submodule update --remote --merge"
submodule_pull_command = "git submodule foreach --recursive git pull"

subprocess.run(submodule_update_command, shell=True, check=True)
subprocess.run(submodule_pull_command, shell=True, check=True)

status_result = subprocess.run("git status --porcelain", shell=True, check=True, stdout=subprocess.PIPE)

if status_result.stdout:
    subprocess.run("git add .", shell=True, check=True)
    subprocess.run("git commit -m 'Update submodules'", shell=True, check=True)
    subprocess.run("git push", shell=True, check=True)
    print("Submodules updated! ✅")
else:
    print("Submodules up-to-date. 👍")
