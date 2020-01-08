echo "Testing env with /bin/bash:" && echo

sudo docker run --rm -it -v `pwd`:/data spark bash -l
