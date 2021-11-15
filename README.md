# CRUD-NoSQL-REST

### ![POST] CREATE POST

```
/api/create-post
```

#### Body

```json
{
  "title": "Sprint 1",
  "author": "Diogo",
  "tags": ["Python", "Flask"],
  "content": "Python é a melhor linguagem para desenvolvimento"
}
```

#### Response

```json
{
  "_id": 6,
  "author": "Diogo",
  "content": "Python é a melhor linguagem para desenvolvimento",
  "created_at": "Mon, 08 Nov 2021 19:14:16 GMT",
  "tags": [
    "Python",
    "Flask"
  ],
  "title": "Sprint 1"
}
```

<br>
<br>

### ![GET] GET ALL POSTS

```
/api/get-posts
```

#### Response

```json
[
  {
    "_id": "5",
    "author": "Lucas",
    "content": "Python",
    "created_at": "Mon, 08 Nov 2021 19:14:16 GMT",
    "tags": [
      "Python",
      "Flask"
    ],
    "title": "Sprint 1",
    "updated_at": "Mon, 08 Nov 2021 19:59:08 GMT"
  },
  {
    "_id": "6",
    "author": "Diogo",
    "content": "Python é a melhor linguagem para desenvolvimento",
    "created_at": "Mon, 08 Nov 2021 19:14:16 GMT",
    "tags": [
      "Python",
      "Flask"
    ],
    "title": "Sprint 1"
  }
]
```

<br>
<br>

### ![GET] GET POST BY ID

```
/api/get-post/<int:id>
```

#### Response

```json
{
  "_id": 6,
  "author": "Diogo",
  "content": "Python é a melhor linguagem para desenvolvimento",
  "created_at": "Mon, 08 Nov 2021 19:14:16 GMT",
  "tags": [
    "Python",
    "Flask"
  ],
  "title": "Linguagens de programação"
}
```

<br>
<br>

### ![PATCH] UPDATE POST BY ID

```
/api/update-post/<int:id>
```

#### Body

```json
{
	"author": "José",
	"content": "Javascript é a melhor linguagem para desenvolvimento"
}
```

#### Response

```json
{
  "_id": 6,
  "author": "José",
  "content": "Javascript é a melhor linguagem para desenvolvimento",
  "created_at": "Mon, 08 Nov 2021 19:14:16 GMT",
  "tags": [
    "Python",
    "Flask"
  ],
  "title": "Sprint 1"
}
```

<br>
<br>

---

### ![DELETE] DELETE POST BY ID

```
/api/delete-post/<int:id>
```

#### Response

```json
{
  "_id": 5,
  "author": "Lucas",
  "content": "Python",
  "created_at": "Mon, 08 Nov 2021 19:14:16 GMT",
  "tags": [
    "Python",
    "Flask"
  ],
  "title": "Sprint 1",
  "updated_at": "Mon, 08 Nov 2021 19:59:08 GMT"
}
```

<br>
<br>
