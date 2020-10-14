# Help with SSH and related commands

## How to SSH
1. First you need your username on the ssh server ``username``

2. Then you need the address of the server, for this exam 1 it is ``exam1.hacking.fans``

3. Then you put them together ``username@exam1.hacking.fans``

4. After entering you ssh passphrase you should be logged in

## How to transfer files
### SCP
Similar to ssh, you need your username and the address of the server ``username@exam1.hacking.fans``

#### Sending files to server
1. Create a file ``my_file.txt``

2. Send file to your directory on the server ``scp my_file.txt username@exam1.hacking.fans:/home/username/``

#### Sending mulitple files to server
1. Create files ``my_file.txt`` and ``my_file2.txt``

2. Send files to your directory on the server ``scp my_file.txt my_file2.txt username@exam1.hacking.fans:/home/username/``

#### Send all in your directory to server
1. Send all files to your directory on the server ``scp * username@exam1.hacking.fans:/home/username/``

2. Or send all files recursively to the server ``scp -r * username@exam1.hacking.fans:/home/username/``

#### Receiving files from server
1. File on the server ``server_file.txt``

2. What you want the file to be saved as ``my_copy.txt``

3. Tell the server to send you the file and save it on your machine ``scp username@exam1.hacking.fans:/home/username/server_file.txt my_copy.txt``

### SFTP
Creates an interactive file transfer shell

`` sftp username@exam1.hacking.fans``

#### Quick list of commands
help: ``?`` or ``help``

Present Working Directory, server: ``pwd`` local: ``lpwd``

Listing Files, server: ``ls`` or ``dir`` local: ``lls``

Uploading file: ``put my_file.txt``

Uploading Multiple Files: ``mput *.txt``

Download file: ``get server_file.txt``

Download multiple files: ``mget *.txt``

Switching Directories, server ``cd`` local ``lcd``

Creating Directories, server ``mkdir dir`` local ``lmkdir dir``

Leave while keeping the connection open: ``!`` then return to the server with ``exit``

Close the connection: ``exit`` or ``quit``
