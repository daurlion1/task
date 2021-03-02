Результат


### Получить список areas   
### ``/areas``
Method: GET
````
Request
{

}
Response
{
    "areas": [
        {
            "id": 1,
            "name": "areaname1",
            "description": "areadescription1",
            "points": [
                32,
                23
            ],
            "fill_type": "color",
            "color": "FFFFFF"
        },
        {
            "id": 2,
            "name": "areaname2",
            "description": "areadescription2",
            "points": [
                70,
                30
            ],
            "fill_type": "gradient",
            "color1": "FFFFFF",
            "color2": "000000",
            "angle": "45"
        },
        {
            "id": 5,
            "name": "name1",
            "description": "description1",
            "points": [
                42,
                35
            ],
            "fill_type": "gradient",
            "color1": "FFFFF",
            "color3": "000000",
            "angle": "45"
        }
    ]
}
````

### Апи для входных данных area , fill_type , attributes  
### ``/area``
Method: POST
````
Request
{
{
    "area":{
        "name":"name1",
        "description":"description1",
        "points":[42,35]
    },
    "fill_type":{
        "name":"gradient"
    },
    "attributes":[
        {
            "name":"color1",
            "value":"FFFFF"
        },
        {
            "name":"color3",
            "value":"000000"
        },
        {
            "name":"angle",
            "value":45
        }
    ]
}
}
Response
{
   "Successfully added"
}
````