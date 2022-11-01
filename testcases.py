# from app import app


# def test_welcome():
#   client = app.test_client()
#   url = '/'
#   response = client.get(url)
#   assert response.get_data() == b'Welcome'

# def test_welcome2():
#   client = app.test_client()
#   url = '/'
#   response = client.get(url)
#   assert response.status_code == 200 


# def test_post():
#     client = app.test_client()
#     url = '/postw/'
#     response = client.get(url)
#     assert response.status_code==405  

# def test_put():
#     client = app.test_client()
#     url = '/putw/'
#     response = client.get(url)
#     assert response.status_code==404

# def test_del():
#     client = app.test_client()
#     url = '/putw/d'
#     response = client.get(url)
#     assert response.status_code==405        