
# Project Title

This project utilizes the Django Rest Framework to create an API USING APIView

The API endpoint can be found on this route /api [link](http://127.0.0.1:8000/api/)

### admin password:
- username: koa
- password: koa2023



## API Reference

#### Get all items

```http
  GET /api/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| null | `string` |Returns all records stored in the database|

#### Post item

```http
  POST /api/${id,points}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. must be unique|
| `points`      | `string` | should be of type string|



#### Output

Returns the id, points, and calculates and returns the smalest Eucledian Distance between two points


## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

runs 3 tests
1. Database insertion 
2. Database retrival
3. If id column is unique

![Image](static/post.png)
    
![Image](static/get.png)

