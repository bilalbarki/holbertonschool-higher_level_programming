#!/bin/bash

#configuration start
id="40"
url="http://173.246.108.142/level0.php"
votes=1024
#configuration end

count=1
while [ $count -le $votes ]
do
    curl --request POST $url --data-urlencode "id=$id" --data-urlencode "holdthedoor=Submit" --silent > /dev/null
    echo "Vote $count has been submitted"
    ((count++))
done

