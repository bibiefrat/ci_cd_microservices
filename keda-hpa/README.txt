in our keda example:
1) we query the MySql DB for requested value (SELECT CEIL(COUNT(*) / 2) FROM task_instance WHERE state='running' OR state='queued')
2) tha value we get is devided by the number of pods (if we get 7 for examle and we have 2 pods - that mean thcurrent value is 7/2=3.5)
3) our deisred value is "queryValue"=5 - this is the number we aspire to - so currently we have 3.5/5
4) if we insert values to table such that the [(query value)/(num of pods)] / 5  > 1  --> we add another pod so we remain our threshold as 5.
5) in order to connect with mysql client to the server --> invoke another client pod in same namespace:
   kubectl run mysql-client -n default --image=mysql:5.7 -it --rm --restart=Never --  mysql -h mysql -u root  -ppassword