import subprocess
import re

def merge_pr(pr_number):
    subprocess.run(["git", "fetch", "origin", f"pull/{pr_number}/head:pr-{pr_number}"])
    subprocess.run(["git", "merge", f"pr-{pr_number}"])
    subprocess.run(["git", "push"])

def get_open_prs():
    output = subprocess.check_output(["git", "ls-remote", "--refs"]).decode()
    prs = re.findall(r"refs/pull/(\d+)/head", output)
    return prs

def merge_all_python_prs():
    open_prs = get_open_prs()
    python_prs = [pr for pr in open_prs if pr.endswith(".py")]

    for pr in python_prs:
        merge_pr(pr)

if __name__ == "__main__":
    merge_all_python_prs()
