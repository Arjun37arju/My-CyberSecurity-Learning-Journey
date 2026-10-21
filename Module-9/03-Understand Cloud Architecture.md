# Understand Cloud Architecture

## Contents
1. [Virtual Machines](#1-virtual-machines)
2. [Containers Awareness](#2-containers-awareness)
3. [Storage Architecture](#3-storage-architecture)
4. [Network Architecture](#4-network-architecture)
5. [Scalability Concepts](#5-scalability-concepts)

---

## 1. Virtual Machines

A **Virtual Machine (VM)** is a software-based computer that runs on a physical computer. It has its own operating system, CPU, memory, and storage.

### Key Concepts
- **Hypervisor:** Software that creates and manages virtual machines.
- **Guest OS:** The operating system installed inside a VM.
- **Isolation:** VMs can run separate operating systems and workloads.

### Benefits
- Run multiple virtual servers on one physical server.
- Allocate CPU, memory, and storage as needed.
- Host websites, applications, and databases.

**Example:** Running a Linux VM on a Windows computer.

---

## 2. Containers Awareness

A **container** is an isolated environment that packages an application with the dependencies it needs to run.

### Key Concepts
- **Docker:** Builds container images and runs containers.
- **Image:** A template used to create a container.
- **Container:** A running instance of an image.
- **Kubernetes:** Manages and orchestrates containers across machines.

### Containers vs. VMs
- VMs run a complete guest operating system.
- Containers share the host OS kernel and are generally lightweight.
- Containers help applications run consistently across environments.

**Example:** Packaging a website and its required libraries into a Docker container.

---

## 3. Storage Architecture

**Storage architecture** describes how data is stored, organized, accessed, and protected in the cloud.

### Types of Cloud Storage

| Type | Purpose | Example |
|---|---|---|
| Object storage | Images, videos, backups, and logs | Amazon S3 |
| Block storage | VM disks and database volumes | Amazon EBS |
| File storage | Shared files and folders | Amazon EFS |

### Important Concepts
- **Durability:** Protection against data loss.
- **Availability:** How readily data can be accessed.
- **Backup:** A copy used to recover data.
- **Encryption:** Protects data from unauthorized reading.
- **Lifecycle policies:** Automatically move or delete data based on rules.

**Remember:** Object = objects, Block = disk, File = folders.

---

## 4. Network Architecture

**Network architecture** describes how cloud resources connect and communicate securely.

### Key Components
- **VPC:** A logically isolated cloud network.
- **Subnet:** A smaller network range inside a VPC.
- **Routing:** Determines where network traffic goes.
- **Internet gateway:** Enables internet connectivity when routes and security rules permit.
- **Firewall / security rules:** Allow or block network traffic.
- **Load balancer:** Distributes requests across multiple servers.
- **DNS:** Converts domain names into IP addresses.
- **VPN:** Creates an encrypted connection over an untrusted network.

### Public and Private Subnets
- **Public subnet:** Has a route to an internet gateway.
- **Private subnet:** Typically has no direct route for inbound internet connections.

**Example:** A website is publicly accessible, while its database stays in a private subnet.

---

## 5. Scalability Concepts

**Scalability** is the ability to increase resources to handle more workload.

### Types of Scaling
- **Vertical scaling (Scale Up):** Increase the CPU or RAM of one server.
- **Horizontal scaling (Scale Out):** Add more servers or application instances.
- **Auto-scaling:** Automatically adjusts resources based on demand or predefined rules.
- **Elasticity:** Resources expand when demand increases and shrink when demand decreases.
- **Load balancing:** Distributes incoming requests across servers.

### Benefits
- Handle increased traffic.
- Improve application performance.
- Support availability and workload distribution.
- Reduce unnecessary resource usage through appropriate scaling.

**Example:** Automatically adding application servers when website traffic increases.

---

## Summary

Cloud architecture combines computing, containers, storage, networking, and scalability to build reliable and efficient cloud applications.
