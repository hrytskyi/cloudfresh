## Part 1: DevOps and DevSecOps

### 1.1. Setup a CI/CD Pipeline

#### Objective

Demonstrate the ability to set up a CI/CD pipeline.

#### Task

1.  **Create a simple web application using Python (Flask).**
2.  **Set up a CI/CD pipeline using GitHub Actions that:**
    -   Automatically runs tests on every push to the repository.
    -   Deploys the application container to Google Cloud Platform.

#### Steps

1.  **Create Flask Web Application**
    
    The web application is a simple Kanban board application. MongoDB Atlas free tier is used for storing data
![main page](https://photos.app.goo.gl/5mSA1WJQWBPvAHLc9)
![board page](https://photos.app.goo.gl/NS4Fq8hdP9LFkdZ59)

2.  **Set Up GitHub Actions CI/CD Pipeline**

first of all, we give our pipeline a name("CI/CD Pipeline" in our case) and command it to start when new changes is pushed to our branch "task1"
```
name: CI/CD Pipeline

on:
  push:
    branches:
      - task1


jobs:
```
Then, we define our first job "test". That job is meant to set up python with dependencies, defined in our app, and then run test simulations, also that we created. Even if our tests is not 100% successful we would anyway go to the next job.
```
  test:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      continue-on-error: true
      run: |
        pytest
```
The main job of that job😁 is to login to GCP, build container with our Flask web application and push it to Artifact Registry. After that, we automatically deploy our web app to Google Cloud Run
```
  deploy:
    needs: test
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1

    - name: Set up GCP authentication
      run: |
        echo "${{ secrets.GCP_SERVICE_ACCOUNT_KEY }}" | base64 --decode > ${HOME}/gcp-key.json
        gcloud auth activate-service-account --key-file=${HOME}/gcp-key.json
        gcloud config set project ${{ secrets.GCP_PROJECT_ID }}
        gcloud auth configure-docker ${{ secrets.GCP_REGION }}-docker.pkg.dev --quiet

    - name: Build and push Docker image
      run: |
        docker build -t ${{ secrets.GCP_REGION }}-docker.pkg.dev/${{ secrets.GCP_PROJECT_ID }}/cloudfresh-registry/kanban-board:latest .
        docker push ${{ secrets.GCP_REGION }}-docker.pkg.dev/${{ secrets.GCP_PROJECT_ID }}/cloudfresh-registry/kanban-board:latest

    - name: Deploy to GCP
      run: |
        gcloud run deploy kanban-board --image ${{ secrets.GCP_REGION }}-docker.pkg.dev/${{ secrets.GCP_PROJECT_ID }}/cloudfresh-registry/kanban-board:latest --platform managed --region ${{ secrets.GCP_REGION }} --allow-unauthenticated
```

### 1.2. Implement Basic Security Measures

#### Objective:
Demonstrate your understanding of DevSecOps.
#### Task:
Implement basic security measures in the application.
#### Steps:

1.  **Use Environment Variables to Manage Secrets:**
    
    -   Add secrets to GitHub repository secrets.
    -   Use these secrets in our CI/CD pipeline.
![GitHub Action secrets](https://photos.app.goo.gl/xmBwWx6ysYMqAjxn7)

2.  **Configure HTTPS for Secure Communication:**
    
    -   GCP Cloud Run automatically provides HTTPS for your services. No additional configuration needed.
![Cloud Run console](https://photos.app.goo.gl/6cfSzsMbNFrhAL6a6)

3.  **Perform Static Code Analysis using Codacy:**
    
    -   **Setup Codacy Integration:**
        
Our last pipeline job is static code analysis tool Codacy integration. I've chosen that tool over SonarQube for simplicity and cloud based infrastructure. There was no need to install any containers or programs for Codacy to work. That job is similar to our first job "test", but additionally it sends testing results to codacy for analysis
```
  codacy:
    runs-on: ubuntu-latest
    needs: test

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Run test with coverage
      continue-on-error: true
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pytest --cov=app --cov-report=xml

    - name: Upload coverage to Codacy
      uses: codacy/codacy-coverage-reporter-action@v1
      with:
        project-token: ${{ secrets.CODACY_PROJECT_TOKEN }}
        coverage-reports: coverage.xml
```

![Codacy](https://photos.app.goo.gl/8MQVs1RHtip7YbTE6)
 
