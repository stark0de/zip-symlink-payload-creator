# zip-symlink-payload-creator
This is a simple tool to create ZIP payloads using a provided wordlist for the symlink attack (present in some file upload vulnerabilities)

```
usage: zip-symlink.py [-h] -f FILE [-g GET]

ZIP symlink payload generator

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Creates the ZIP payloads based on a wordlist
  -g GET, --get GET     Introduce the link filename to get the file to which it corresponds
  
```
