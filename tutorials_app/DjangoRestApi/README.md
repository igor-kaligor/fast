
# Tutorial API




## Requirements

- Python 3.7+
- SQLITE
- Django Rest Framework


## Documentação da API

#### Retorna todos os itens

```http
  GET /api/tutorials
```


#### Insere um novo item
```http
  POST /api/tutorials
```
```json
{
    "title": "Django Rest Framework Tut#3",
    "description": "Tut#3 Description",
    "published": false,
    "liveDate": "2020-12-12T00:00:00Z",
    "attendancelist": "pot alco2 hbas"
}
```


#### Deleta todos os items
```http
  DELETE /api/tutorials
```

#### Retorna um item

```http
  GET /api/tutorials/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |



#### Altera um item
```http
  PUT /api/tutorials/${id}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

```json
{
    "title": "Django Rest Framework Tut#3",
    "description": "Tut#3 Description",
    "published": false,
    "liveDate": "2020-12-12T00:00:00Z",
    "attendancelist": "pot alco2 hbas"
}
```


#### Deleta um item
```http
  DELETE /api/tutorials/${id}
```

#### Retorna todos os itens publicados

```http
  GET /api/tutorials/published
```
## Instalação


Para instalar esse projeto rode

```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install requirements.txt
  python manage.py migrate
```








## Deploy

Para fazer o deploy desse projeto rode

```bash
  python manage.py runserver 8080
```

