def test_with_client(client):
    response = client.get('/api/v1/')
    assert response.status_code == 200
