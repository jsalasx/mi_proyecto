# Tareas Backend
## URL DE PRUEBAS
```bash
https://k8s-nstodole-webnginx-69400ae802-1980802023.us-east-2.elb.amazonaws.com/
```

## Tecnologias utilizadas:

### Python, Djangorestframework, Django, Docker, Kubernetes, AWS, EKS

Se realizó la aplicación para registro de usuarios y el crud de tareas.

Escalabilidad Vertical (Pods) Kubernetes

Para grandes volumenes de datos se realizo con un balanceador de carga, con 4 instancias (pods) de la misma aplicacion teniendo un rendimiento de 80 tareas ingresadas a la base de datos por segundo 80 T/s

En una prueba de estres con APACHE JMETER de 2000 peticiones la aplicacion no tuvo caidas y respondio bien en 25s de ejecucion.

Se adjunto fotografia de la interfas de Apache JMeter
![jmeter todo legal](https://github.com/jsalasx/mi_proyecto/assets/102547359/b6fb7187-74d2-4cb3-a9dc-af99b8a8aa0c)

## Despliegue

## Construir la imagen

```bash
docker build -t todolegal_back  .
```

# Logearse en AWS
```bash
aws configure
```

## Crear un Cluster de EKS

Se puede hacer desde la consola de AWS
```bash
https://us-east-2.console.aws.amazon.com/eks/home?region=us-east-2#/home
```
## Aprovisionar con un Nodo

Se puede hacer desde la consola de AWS ( Dentro de Cluster creado Pestaña Informática - Grupo de Nodos )

## Crear un Elastic Container Registry

Se puede hacer desde la consola de AWS
```bash
https://us-east-2.console.aws.amazon.com/ecr/get-started?region=us-east-2
```

## Crear politicas y roles

Descargar este archivo y copiarlo a la raiz del proyecto.
```
https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.7.1/docs/install/iam_policy.json
```
Ejecutar este comando
```bash
eksctl utils associate-iam-oidc-provider --cluster my-cluster --approve
```
Ejecutar este comando
```bash
aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam_policy.json
```
Ejecutar este comando
```bash
eksctl create iamserviceaccount --cluster=todolegal-2 --namespace=kube-system --name=aws-load-balancer-controller  --role-name AmazonEKSLoadBalancerControllerRole --attach-policy-arn=arn:aws:iam::961883253387:policy/AWSLoadBalancerControllerIAMPolicy --approve
```
## Crear un Balanceador de Carga
Añadir el repositorio 
```bash
helm repo add eks https://aws.github.io/eks-charts
```
Actualizar el repostirio
```bash
helm repo update eks
```
```bash
helm install aws-load-balancer-controller eks/aws-load-balancer-controller --set clusterName=your-cluster-name --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller --namespace kube-system
```

## Generar un certificado con un dominio (Si se desea usar HTTPS) AWS Certificate Manager (ACM)

Solicitar un certificado y configurar los CNAME del proveedor de dominio
### Demora en 15 y 20 minutos en reconocer el dominio

## Logearse en Elastic Container Registro (ECR)

```bash
aws ecr get-login-password --region my-region | docker login --username AWS --password-stdin my-id.dkr.ecr.my-region.amazonaws.com/my-registry
```

## Subir la imagen a Elastic Container Registry

```bash
docker tag todolegal_back my-id.dkr.ecr.my-region.amazonaws.com/my-registry:latest
```
```bash
docker push my-id.dkr.ecr.my-region.amazonaws.com/my-registry:latest
```

# Despliege en Elastic Kubernetes Service (EKS)
```bash
aws eks --region my-region update-kubeconfig --name my-cluster
```
## Namespace
```bash
kubectl apply -f namespace.yaml
```
## Deployment
```bash
kubectl apply -f deployment.yaml
```
## Service
```bash
kubectl apply -f service.yaml
```
## Ingress
```bash
kubectl apply -f ingress.yaml
```
