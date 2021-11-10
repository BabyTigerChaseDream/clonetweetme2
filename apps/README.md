# Jplus
# Instruction on 
https://www.youtube.com/watch?v=W5Ov0H7E_o4&list=PLOLrQ9Pn6cazCfL7v4CdaykNoWMQymM_C&index=1

# Part-1
1. install python virtual env
2. activate virtual env 
3. dump pip freeze to requirements.txt
4. Refer commands in Dockerfile

7. Port already in use: kill it :
   sudo lsof -t -i tcp:8000 | xargs kill -9
   
   https://stackoverflow.com/questions/20239232/django-server-error-port-is-already-in-use
