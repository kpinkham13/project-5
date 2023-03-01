Kyle Pinkham

kpinkham13@gmail.com

This application is used to calculate opening and closing times of checkpoints in an ACP Brevet bicycle race. It does this through the algorithm in acp_times.py which divides the checkpoint distance by a set maximum/minimum speed and shifts the start time based on the calculation. In order to run the application build and run a docker container, the Dockerfile is all set up. The web service is used by inputting a total distance, start time, and the various checkpoint distances then it automatically calculates the open and close time of the checkpoints. In this project I have added a Mongo database in order to store values by hitting the Submit button and fetch those values by clicking the Display button. It does this through AJAX interaction with my flask app which is connected to the database.
