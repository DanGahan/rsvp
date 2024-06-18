# rsvp

## Clean Deployment using compose file
```docker rm -f rsvp-frontend-1 rsvp-backend-1 rsvp-db-1  && docker rmi rsvp-frontend rsvp-backend rsvp-db && docker-compose up```

## Curl API Calls

### rsvp POST

```curl -X POST http://127.0.0.1:5555/rsvp -H "Content-Type: application/json" -d '{"name":"John","attending":"Yes","vegetarian":"Yes","wine":"white","plus_one":"yes","plus_one_name":"Jane","plus_one_vegitarian":"No ","plus_one_wine":"red","song_suggestion":"Song name"}'```

### rsvp GET

```curl http://127.0.0.1:5555/rsvps```

### Evening rsvp POST

```curl -X POST http://127.0.0.1:5555/evening_rsvp -H "Content-Type: application/json" -d '{"name":"John","attending":"Yes","plus_one":"yes","plus_one_name":"Jane"}'```

### Evening rsvp GET

```curl http://127.0.0.1:5555/evening_rsvps```

### DB Commands

```docker exec -it --user postgres rsvp-db-1  psql```
