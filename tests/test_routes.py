import faker

fake = faker.Faker()

def test_create_todo(client):
    payload = {
        'title': fake.sentence(nb_words=2),
        'description': fake.paragraph(nb_sentences=2),
        'completed': fake.boolean(),
    }
    response = client.post('/api/todos', json=payload)

    assert response.status_code == 201
    assert response.json == {
        'id': 1,
        'title': payload['title'],
        'description': payload['description'],
        'completed': payload['completed'],
    }

def test_update_todo(client, todo):
    payload = {
        'title': fake.sentence(nb_words=2),
        'description': fake.paragraph(nb_sentences=2),
        'completed': fake.boolean(),
    }
    response = client.put(f'/api/todos/{todo.id}', json=payload)
    assert response.status_code == 200
    assert response.json == {
        'id': todo.id,
        'title': payload['title'],
        'description': payload['description'],
        'completed': payload['completed'],
    }

def test_patch_todo(client, todo):
    payload = {
        'title': fake.sentence(),
    }
    response = client.patch(f'/api/todos/{todo.id}', json=payload)
    assert response.status_code == 200
    assert response.json['title'] == payload['title']

def test_delete_todo(client, todo):
    response = client.delete(f'/api/todos/{todo.id}')
    assert response.status_code == 204

def test_list_todos(client, todo):
    response = client.get('/api/todos')
    assert response.status_code == 200
    assert response.json == [
        {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed,
        }
    ]
