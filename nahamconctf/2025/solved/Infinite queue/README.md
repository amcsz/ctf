get the token using ```localStorage.getItem("queue_token")```

go to https://jwt.io/

change the timestamp to a small number, and use ```localStorage.setItem()``` to set the new token

it will give an error, inspect it and extract the secret, then paste into jwt.io

set the new jwt token again, and this time it should give the flag.