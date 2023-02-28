# Instructions

Clone this repository, create a new branch and start the exercise

## Details
Create a Django REST API 

### Models
- **User** Either extending the django's native user or starting from scratch. Include fields:
    - Phone number
    - City
    - last login
- **Pet** Thinking there will only be dogs.
    - Date of Birth
    - Gender
    - Weight
    - Breed
    - deceased date

Constrain: Pets can have multiple owners.

Create endpoints for
- CRUD operations for users
- CRUD operations for pets
- Given the user, retrieve pets associated with him
- Associate a pet to a user


### API responses
- When retrieving pet/pets, include both it's date of birth and current age


### Suggestions
- Using REST Framework is expected
- Could use any kind of DB

### Extra Points
- Using JWT authentication
- Handle permissions so only users with clearance can delete other users
- Include photo profiles for users and/or pets. Could use [min.io](https://min.io/), S3 or any other Cloud Service
- If photo is included, make sure there's only 1 photo per user un the cloud (deleting proccess after the update of the image)
- Dockerfile & docker-compose
