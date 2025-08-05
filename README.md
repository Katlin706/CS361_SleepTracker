# CS361_SleepTracker

Created as a part of CS361 - Software Engineering I </br>
Oregon State University  </br>
Summer 2025 </br>

# Communication Contract 

<ol>
  <li>How to <strong>REQUEST</strong> data from the microservice: </li>
    <ul>
    <li>To add a sleep log, send a string in the following format: 
'{"date":"YYYY-MM-DD", "duration": int}'. Replace YYYY-MM-DD and int with the proper values of your date of sleep 
duration of sleep. Note that the data within the single quotes must be valid json. 
    </li>
<li> To request the last X days of sleep logs and the average duration of sleep, 
send a string in the following format: '{"days_requested": int}'. Replace int 
with your desired number of days. Note that the data within the single quotes must be valid json</li>
<li> To request that all your sleep logs get cleared/deleted, send the following sting: 
"confirm delete_all sleep entries". This does NOT need to be valid JSON 
</li>
<li>
To request that the program QUIT and close connection with the socket, send the following string: "Q". This does
NOT need to be valid JSON.</li>
    </ul>
<li>How to <strong>RECEIVE</strong> data from the microservice:</li>
<ul>
<li> When attempting to add a sleep log, the expected response will be a string in the following format: 
'{"status":"success"}' or '{"status":"failure"}'. This will be sent as a string but will be valid json inside the 
single quotes.
</li>
<li>When requesting sleep data from the past X days, the expected response will be sent as a string in the following 
format: '{ "sleep_data": [ {"date":"2025-07-25", "duration": 7.5}, {"date":"2025-07-26", "duration": 8}], "average":7.75}.'
This is will be sent as a string but will be valid JSON within the single quotes. The number 
of list items will flex based on the number of days requested. 
</li>
<li>When attempting to delete all sleep data, the expected response will be a string in the following format: 
'{"status":"success"}' or '{"status":"failure"}'. This will be sent as a string but will be valid json inside the 
single quotes. </li>
<li> When attempting to Quit and close the connection, no data will be sent in response.</li>
</ul>
<li>UML Sequence Diagram:</li>
</ol>


