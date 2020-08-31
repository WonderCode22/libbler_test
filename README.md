###### Server Run
 `flask run`
 
###### if run the server in development mode
`flask run --no-reload`

##
##### Commands For Test
- ###### create events for test
    `python run.py create_events -e/--event event string` \

        i.e : python run.py create_events -e I just won a lottery #update @all   

- ###### get events for test
    `python run.py get_events` 
     -  options: \
      **-c,  --category**: Get events by category \
      **-p,  --person**: Get events by person \
      **-a,  --amount**: Amount of events to retrieve
      
     If there is no option, it gets 10 events by time order.
     
        i.e : python run.py get_events --category warn --amount 5