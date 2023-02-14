# Channels Api

## UML

![alt text](UML.JPG "Title")


## Endpoints 

### GET /api/group/<int:pk>  
Allow:  GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Example Response: 
```json
        {
            "id": 1,
            "name": "group1",
            "channels": [
                24,
                23
            ]
        }
```
### GET /api/group/
Allow:  GET, POST, HEAD, OPTIONS
Content-Type: application/json
Example Response :
```json
        [
            {
                "id": 1,
                "name": "group1",
                "channels": [
                    24,
                    23
                ]
            },
            {
                "id": 2,
                "name": "group2",
                "channels": [
                    25,
                    26
                ]
            }
        ]

```
### GET /api/channel/<int:pk>/
Allow:  GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Example Response:
```json
        {
            "id": 23,
            "title": "Movies",
            "picture_url": "https://w7.pngwing.com/pngs/327/703/png-transparent-cinema-film-moveis-logo-film-art-film-thumbnail.png",
            "is_parent": true,
            "parent_channel": null,
            "date_created": "2023-02-11T18:43:57.156882Z",
            "groups": [
                1,
                2
            ]
        }
```
### GET /api/channel/
Allow:  GET, POST, HEAD, OPTIONS
Content-Type: application/json
Example Response:
```json
    [
    {
        "id": 23,
        "title": "Movies",
        "picture_url": "https://w7.pngwing.com/pngs/327/703/png-transparent-cinema-film-moveis-logo-film-art-film-thumbnail.png",
        "is_parent": true,
        "parent_channel": null,
        "date_created": "2023-02-11T18:43:57.156882Z",
        "groups": [
            1,
            2
        ]
    },
    {
        "id": 24,
        "title": "Series",
        "picture_url": "https://e1.pngegg.com/pngimages/312/318/png-clipart-video-formats-icon-tv-series-thumbnail.png",
        "is_parent": true,
        "parent_channel": null,
        "date_created": "2023-02-11T18:45:00.730561Z",
        "groups": [
            1
        ]
    },
    ]
```
### GET /api/channel/### GET_rating/<int:pk>/
Allow: GET, HEAD, OPTIONS
Content-Type: application/json

Example Response:
```json
    {
    "channel": "Series",
    "rating": 8.5
    }
```

### GET /api/channel/export_ratings/
Allow: GET, HEAD, OPTIONS
Returns a CSV file with all the ratings of the channels
Example content of the CSV file:
    Channel Title,Average Rating
    Movies,9
    Vikings,9
    Action,9
    Series,8.5
    Better Call Saul,8

### GET /api/content_type/<int:pk>