# ViExams - A centralised question bank platform for college students

## Official repo for ViExams

# API Docs:
## Routes:
- `GET /api/papers?course=null&limit=5` Fetch random papers on specific course
    - Error Handling: 
        1. 404 Not Found - Course not found error
- `POST /api/upload` **Request-Body: multipart/form-data** Upload a paper
    - Error Handling:
        1. 422 Unprocessable Entity - Invalid Image Format / Non-parseable Image Uploaded
