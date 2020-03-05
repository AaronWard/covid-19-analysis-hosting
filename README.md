# covid-19-analysis-hosting
This is a flask app that will spark off the covidify package everyday. It will using [kaffeine](https://kaffeine.herokuapp.com/) to ping the server every 30 minutes to keep it awake (#FreeHosting), and a cron job will be set up in order to run the job every day. 

APSecheduler uses cron-like arguments to run [covidify](https://github.com/AaronWard/covid-19-analysis) every hour and save the images in the static folder

From there, the image urls can be used in the readme for covidify and keep updated reports without having to manually updating the repository every day. 