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
