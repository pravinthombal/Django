# myapp/tests.py
# import pytest
# from rest_framework import status
# from rest_framework.test import APIClient
# from .models import Book

# @pytest.mark.django_db
# def test_create_book():
#     client = APIClient()
#     response = client.post('/api/books/', {
#         'title': 'Test Book',
#         'author': 'Test Author',
#         'published_date': '2024-01-01'
#     })
#     assert response.status_code == status.HTTP_201_CREATED
#     assert Book.objects.count() == 1
#     assert Book.objects.get().title == 'Test Book'

# @pytest.mark.django_db
# def test_read_book():
#     client = APIClient()
#     book = Book.objects.create(title='Test Book', author='Test Author', published_date='2024-01-01')
#     response = client.get(f'/api/books/{book.id}/')
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['title'] == 'Test Book'

# @pytest.mark.django_db
# def test_update_book():
#     client = APIClient()
#     book = Book.objects.create(title='Test Book', author='Test Author', published_date='2024-01-01')
#     response = client.put(f'/api/books/{book.id}/', {
#         'title': 'Updated Book',
#         'author': 'Updated Author',
#         'published_date': '2024-01-01'
#     })
#     assert response.status_code == status.HTTP_200_OK
#     assert Book.objects.get(id=book.id).title == 'Updated Book'

# @pytest.mark.django_db
# def test_delete_book():
#     client = APIClient()
#     book = Book.objects.create(title='Test Book', author='Test Author', published_date='2024-01-01')
#     response = client.delete(f'/api/books/{book.id}/')
#     assert response.status_code == status.HTTP_204_NO_CONTENT
#     assert Book.objects.count() == 0







import pytest
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

@pytest.fixture
def api_client():
    """Fixture to provide an instance of APIClient."""
    return APIClient()

@pytest.fixture
def sample_book(db):
    """Fixture to create a sample book instance."""
    return Book.objects.create(
        title='Test Book',
        author='Test Author',
        published_date='2024-01-01'
    )

@pytest.mark.django_db
def test_create_book(api_client):
    """Test for creating a new book."""
    response = api_client.post('/api/books/', {
        'title': 'Test Book',
        'author': 'Test Author',
        'published_date': '2024-01-01'
    })
    # print('***********',Book.objects.get(),'***********')
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.count() == 1
    assert Book.objects.get().title == 'Test Book'

@pytest.mark.django_db
def test_read_book(api_client, sample_book):
    """Test for retrieving an existing book."""
    response = api_client.get(f'/api/books/{sample_book.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Test Book'

@pytest.mark.django_db
def test_update_book(api_client, sample_book):
    """Test for updating an existing book."""
    response = api_client.put(f'/api/books/{sample_book.id}/', {
        'title': 'Updated Book',
        'author': 'Updated Author',
        'published_date': '2024-01-01'
    })
    assert response.status_code == status.HTTP_200_OK
    assert Book.objects.get(id=sample_book.id).title == 'Updated Book'

@pytest.mark.django_db
def test_delete_book(api_client, sample_book):
    """Test for deleting an existing book."""
    response = api_client.delete(f'/api/books/{sample_book.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Book.objects.count() == 0