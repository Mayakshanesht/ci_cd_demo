# CI/CD Demo with Github, Jenkins, Docker and Kubernetes 

This repository demonstrates setting up a Continuous Integration and Continuous Deployment (CI/CD) pipeline using Jenkins and deploying a service to Kubernetes. The application is exposed on a Kubernetes service and can be accessed locally via port forwarding.

## Prerequisites

- **Jenkins** installed
- **Docker** installed and Dockerhub account credentials added to the jenkins
- **Kubernetes** cluster up and running using the k3s 
- **kubectl** installed and configured

## Steps to Set Up the Project

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/Mayakshanesht/ci_cd_demo.git
cd ci_cd_demo
```

### 2. Install Jenkins

If you don’t have Jenkins installed, follow the [Jenkins installation guide](https://www.jenkins.io/doc/book/installing/). Once Jenkins is up and running:

- Go to `http://localhost:8080` and complete the initial setup.
- Install necessary plugins as prompted.

### 3. Create Jenkins Pipeline

1. **Create a New Pipeline Job**:
    - Go to Jenkins dashboard (`http://localhost:8080`).
    - Click on **New Item**, enter a name (e.g., `ci_cd_demo_pipeline`), select **Pipeline**, and click **OK**.

2. **Configure Pipeline**:
    - In the job configuration, under the **Pipeline** section, choose **Pipeline script from SCM**.
    - Set **SCM** to **Git** and enter the repository URL: `https://github.com/Mayakshanesht/ci_cd_demo.git`.

3. **Add Pipeline Script**:
    - Set the **Script Path** to `Jenkinsfile` or wherever your pipeline script resides.

4. **Save** the pipeline job.

### 4. Run the Jenkins Job

1. Go to the newly created pipeline job in Jenkins.
2. Click on **Build Now** to trigger the pipeline.
3. Monitor the build process. The pipeline should include stages for building, testing, and deploying the service.

### 5. Port Forwarding with Kubernetes

Once the pipeline has deployed the application to Kubernetes, you need to forward a port from the Kubernetes service to your local machine:

```bash
sudo kubectl port-forward service/calculator-service 5002:5002
```

This command will forward the Kubernetes service `calculator-service` on port `5002` to your local machine on port `5002`.

### 6. Access the Web Application

Once the port forwarding is set up, open a web browser and visit the following URL:

```bash
http://localhost:5002/
```

You should see the application running in your browser:

![Webpage Screenshot](https://github.com/user-attachments/assets/59682606-3020-4a07-a393-876f6dc19ec5)

### 7. Answer Section

Once everything is set up and working, the application will display:

![Answer Screenshot](https://github.com/user-attachments/assets/ed838dcb-1a44-4d7a-9f85-d91c014b903d)

## Troubleshooting

- **Jenkins Build Failures**: Check the Jenkins job logs for detailed error messages.
- **Port Forwarding Issues**: Ensure that the service name (`calculator-service`) is correct and that the Kubernetes cluster is healthy.
- **Access Denied in Webpage**: Ensure that port forwarding is working and the correct port is being forwarded.

## Cleanup

To clean up the environment, stop port forwarding with `CTRL+C` and stop Jenkins using:

```bash
sudo systemctl stop jenkins
```

---

