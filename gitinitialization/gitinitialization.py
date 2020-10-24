import sys
import os
from github import Github

path = input("Enter repo name: ")

username = ""
password = ""

def create():
  foldername = str(path)
  user = Github(username, password).get_user()
  repo = user.create_repo(foldername)
  print("Succesfully created repository {}".format(foldername))

if __name__ == "__main__":
  create
