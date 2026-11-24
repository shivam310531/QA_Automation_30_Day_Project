Day 27 – Kubernetes Basics for QA

1. Cluster, Node and Pod

- Cluster: Complete Kubernetes environment.
- Node: Machine on which Pods run.
- Pod: Smallest deployable unit in Kubernetes. It contains one or more containers.

Hierarchy:

Cluster → Node → Pod → Container

2. Deployment and Service

- Deployment: Manages Pods and maintains the desired number of replicas.
- Service: Provides stable network access to Pods, even when Pod IPs change.

Example: "replicas = 3" means Kubernetes tries to maintain 3 Pods.

3. kubectl Basics

"kubectl" is the command-line tool used to interact with Kubernetes.

Commands practiced:

kubectl get nodes
kubectl get pods -A
kubectl get pods
kubectl get namespaces
kubectl get pods -n kube-system
kubectl get pods -n kube-system -o wide

4. Inspect Pods and Logs

kubectl get deployments
kubectl get pods
kubectl logs deployment/qa-test-app
kubectl describe deployment qa-test-app

- "get pods": Checks Pod status.
- "logs": Reads container logs.
- "describe": Shows detailed resource information and events.

5. Kubernetes Test Workload Demo

Created a Deployment using Nginx:

kubectl create deployment qa-test-app --image=nginx

Verified Deployment:

kubectl get deployments

Verified Pod:

kubectl get pods

Inspected logs:

kubectl logs deployment/qa-test-app

Inspected Deployment details:

kubectl describe deployment qa-test-app

Result: Deployment created successfully, one replica maintained, and Pod reached Running status.

6. Where QA Automation Fits

QA Automation can:

1. Verify Pods and Deployments.
2. Inspect application logs.
3. Execute API and smoke tests.
4. Validate application functionality after deployment.
5. Investigate failures using Kubernetes status and logs.

Important: Pod Running does not guarantee that the application is functioning correctly. Actual application and API testing are also required.

Day 27 Deliverable

- Kubernetes cluster created using Kind.
- Node status verified as Ready.
- Nginx test workload deployed.
- Pod status and logs inspected.
- QA Automation role understood.