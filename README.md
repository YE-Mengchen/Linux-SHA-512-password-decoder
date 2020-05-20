This project is aim at decode SHA-512 password in linux /etc/shadow file.
The project should be run in this way:
First install passlib library:
pip3 install passlib
Then create a file contain the ciphertext you wish to decode, the ciphertext should in this format:
root: $6$9w5Td6lg$bgpsy3olsq9WwWvS5Sst2W3ZiJpuCGDY.4w4MRk3ob/i85fl38RH15wzVoomff9isV1 PzdcXmixzhnMVhMxbvO:15775:0:99999:7:::
Please note: the password is hashed with SHA-512 iff the first number after the first "$" sign is 6. If not, the password is hashed with another hash function, such as $1 is hashed by MD5 and this project cannot decode them. If I have time I will write them in the future.

Then run the run.py in this way:
python3 run.py ciphertextfile [mode]
In my project you can choose three mode to decode:
mode 1 is checking 100k password,
mode 2 is 1m,
mode 3 is 10m.
the default mode is 2.
sample:
python3 test.py 1
