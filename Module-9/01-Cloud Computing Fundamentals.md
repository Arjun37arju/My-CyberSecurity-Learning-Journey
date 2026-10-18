# Task 1 — Cloud Computing Fundamentals

## Contents

1. [What Is Cloud Computing?](#1-what-is-cloud-computing)
2. [Cloud Service Models](#2-cloud-service-models)
3. [Cloud Deployment Models](#3-cloud-deployment-models)
4. [Benefits of Cloud Computing](#4-benefits-of-cloud-computing)
5. [Enterprise Cloud Adoption](#5-enterprise-cloud-adoption)

---

## 1. What Is Cloud Computing?

**Cloud computing** means using computing resources such as servers, storage, databases, networking, and software over a network, usually the internet.

Instead of buying and maintaining physical servers, an organization can use resources provided by a cloud provider.

### Simple Example

Imagine saving a file using an online storage service.

```text
Your Computer
      ↓
Internet
      ↓
Cloud Provider
      ↓
File Stored in the Cloud
```

You can access the file from another device by signing in with the correct account and permissions.

### Common Cloud Resources

- **Compute:** Resources that run applications.
- **Storage:** Services that store files and data.
- **Databases:** Services that organize application data.
- **Networking:** Connections, routing, and network security.
- **Software:** Applications accessed over the internet.

### Key Characteristics

- **On-demand access:** Resources can be created when needed.
- **Network access:** Authorized users can access services over a network.
- **Resource pooling:** Providers share underlying infrastructure among customers while maintaining logical separation.
- **Scalability:** Resources can increase or decrease as needs change.
- **Measured usage:** Resource consumption can be tracked for billing and cost management.

### Traditional IT vs Cloud Computing

| Traditional IT                                          | Cloud Computing                                         |
| ------------------------------------------------------- | ------------------------------------------------------- |
| The organization buys physical servers.                 | The organization uses provider-supplied resources.      |
| Adding capacity may require new hardware.               | Capacity can often be increased more quickly.           |
| The organization maintains its physical infrastructure. | The provider manages the physical cloud infrastructure. |
| Large upfront hardware costs may be required.           | Costs often depend on usage or subscription.            |

### Cybersecurity Considerations

- Use strong passwords and multi-factor authentication (MFA).
- Give users only the permissions they need.
- Protect sensitive data.
- Keep systems and applications updated.
- Monitor activity and review security settings.

> **Remember:** Cloud computing changes how computing resources are provided and managed. It does not remove the need for security.

---

## 2. Cloud Service Models

Cloud service models explain **what the cloud provider manages and what the customer manages**.

The three main models are IaaS, PaaS, and SaaS.

### IaaS — Infrastructure as a Service

IaaS provides computing infrastructure, such as virtual machines, storage, and networking.

The customer typically manages the operating system inside a virtual machine, applications, and many security configurations.

**Example:** Running an Ubuntu virtual machine on a cloud service.

### Simple Flow

```text
Cloud Provider
      ↓
Physical Servers and Virtualization
      ↓
Virtual Machine
      ↓
Customer Manages OS and Applications
```

### Customer Responsibilities

- Update and patch the guest operating system.
- Configure firewalls and network access.
- Secure applications and data.
- Manage users and permissions.
- Monitor system activity.

**Security example:** If a company runs Ubuntu on a cloud virtual machine, it is generally responsible for patching that guest operating system.

> **IaaS = Rent the infrastructure and manage more of the software yourself.**

### PaaS — Platform as a Service

PaaS provides a platform for developing and running applications. The provider manages more of the underlying infrastructure and software platform.

**Example:** Deploying application code to a managed application platform.

### Simple Flow

```text
Cloud Provider
      ↓
Infrastructure and Platform
      ↓
Customer Application
      ↓
Customer Manages Code, Data and Access
```

### Customer Responsibilities

- Write secure application code.
- Protect sensitive data.
- Manage application settings and secrets.
- Configure user permissions.
- Monitor application behavior.

**Security example:** A managed platform may handle operating-system maintenance, but the customer must still protect application credentials and fix insecure code.

> **PaaS = The provider manages more of the platform while you focus on your application.**

### SaaS — Software as a Service

SaaS provides a complete application that users access through a browser or app.

**Example:** An online email or collaboration service.

### Simple Flow

```text
Cloud Provider
      ↓
Infrastructure
      ↓
Operating System and Platform
      ↓
Complete Application
      ↓
Customer Uses and Configures It
```

### Customer Responsibilities

- Manage user accounts.
- Enable MFA.
- Configure sharing permissions.
- Control access to sensitive information.
- Follow organizational data-protection policies.

**Security example:** A company using online email must prevent unauthorized access to employee accounts and confidential messages.

> **SaaS = Use a complete application managed by the provider, while securing your accounts and data.**

### Comparison of Cloud Service Models

| Feature          | IaaS                                       | PaaS                                    | SaaS                                      |
| ---------------- | ------------------------------------------ | --------------------------------------- | ----------------------------------------- |
| Main offering    | Infrastructure                             | Application platform                    | Complete application                      |
| Customer manages | OS, applications, data, access             | Application code, data, access          | Accounts, permissions, data use           |
| Provider manages | Physical infrastructure and virtualization | Infrastructure and much of the platform | Application and underlying platform       |
| Customer control | Highest of the three                       | Moderate                                | Usually lowest over underlying technology |
| Example          | Cloud virtual machine                      | Managed application platform            | Online email service                      |

### Shared Responsibility Model

Cloud security is a shared responsibility.

The provider protects the cloud infrastructure and services it operates. The customer protects the parts it controls, such as accounts, data, configurations, and applications.

The exact division depends on the service.

> **Remember:** IaaS gives you more infrastructure responsibility, PaaS manages more of the platform, and SaaS provides a complete application.

---

## 3. Cloud Deployment Models

Cloud deployment models describe **how a cloud environment is organized and who it is intended for**.

The four main models are public, private, hybrid, and community cloud.

### Public Cloud

A public cloud provides services to many customers through a cloud provider.

Customers share underlying infrastructure while their resources and data remain logically separated.

**Example:** A company hosts its website using a public cloud provider.

### Security Considerations

- Keep cloud storage private unless public access is intentionally required.
- Use MFA and appropriate access controls.
- Configure network rules correctly.
- Monitor for exposed resources.

> **Public cloud does not mean that all data is publicly accessible.**

### Private Cloud

A private cloud environment is dedicated to one organization. It may be operated by the organization itself or by a third party.

**Example:** A large company operates a cloud environment dedicated to its internal systems.

### Security Considerations

- Apply strong access controls.
- Update and patch systems.
- Monitor security activity.
- Protect backups and sensitive data.

> **Private cloud does not automatically mean secure. Security depends on how the environment is configured and managed.**

### Hybrid Cloud

A hybrid cloud combines private and public cloud environments that work together or exchange data and applications.

**Example:** A company keeps a sensitive internal system in a private environment while hosting its public website in a public cloud.

### Security Considerations

- Secure connections between environments.
- Apply consistent access policies.
- Monitor data movement.
- Protect interfaces between systems.

> **Hybrid cloud = Private and public environments working together.**

### Community Cloud

A community cloud is designed for multiple organizations that share requirements, such as security, policy, or compliance needs.

**Example:** Several organizations with similar healthcare or government requirements use a shared cloud environment.

### Security Considerations

- Define security responsibilities clearly.
- Separate each organization's data.
- Control administrative access.
- Agree on monitoring and incident response.

> **Community cloud = A cloud environment shared by organizations with common requirements.**

### Comparison of Deployment Models

| Model           | Meaning                                               | Example                                                              |
| --------------- | ----------------------------------------------------- | -------------------------------------------------------------------- |
| Public cloud    | Services offered to many customers                    | Company website hosted by a cloud provider                           |
| Private cloud   | Environment dedicated to one organization             | Internal enterprise systems                                          |
| Hybrid cloud    | Private and public environments working together      | Sensitive systems remain private while web services use public cloud |
| Community cloud | Environment shared by organizations with common needs | Organizations sharing a compliance-focused environment               |

### Important Security Points

- A cloud provider's name does not determine the deployment model.
- Sensitive data does not automatically require a private cloud.
- No deployment model guarantees security by itself.
- Identity management, configuration, monitoring, and data protection remain important.

> **Remember:** Public = many customers; private = one organization; hybrid = connected environments; community = organizations with shared needs.

---

## 4. Benefits of Cloud Computing

Cloud computing offers several benefits, but organizations must manage costs, access, and security carefully.

### Scalability and Elasticity

**Scalability** means increasing or decreasing computing capacity as needed.

**Elasticity** means resources can adjust to changes in demand, often automatically.

**Example:** An online shopping website increases its capacity during a festival sale and reduces it when traffic drops.

### Security Considerations

- Secure newly created resources.
- Review permissions after scaling.
- Monitor unusual resource creation.
- Avoid exposing services unnecessarily.

> **Scalability and elasticity = Adjust computing resources to match demand.**

### Cost Management

Cloud services can reduce the need to purchase physical servers and other hardware upfront.

**Example:** A small company rents cloud servers instead of purchasing its own server equipment.

However, cloud computing is not always cheaper. Unused resources, excessive data transfer, and unsuitable service choices can increase costs.

### Cost and Security Tips

- Set budget and billing alerts.
- Review resource usage regularly.
- Remove unused resources.
- Restrict who can create expensive resources.
- Investigate unexpected usage spikes.

> **Cloud can reduce upfront costs, but usage still needs to be monitored.**

### Access from Different Locations

Authorized employees can access cloud services from different locations using a network connection.

**Example:** Employees work on shared project files from home or the office.

### Security Considerations

- Enable MFA.
- Apply least privilege.
- Use secure devices and connections.
- Avoid sharing accounts.
- Review access permissions regularly.

> **Access from anywhere should mean access for authorized users, not access for everyone.**

### Backup and Disaster Recovery

A **backup** is a saved copy of data or systems.

**Disaster recovery** is the process of restoring systems and services after a serious disruption.

**Example:** A company restores its application from protected backups after a system failure.

### Security Considerations

- Restrict access to backups.
- Keep important backups isolated or immutable where appropriate.
- Test restoration regularly.
- Consider ransomware when designing backup protection.

A backup is useful only if it can be restored successfully.

> **Backup = A saved copy. Disaster recovery = Restoring systems after a disruption.**

### Global Reach

Cloud providers may offer services in multiple geographic regions, helping businesses serve users in different parts of the world.

**Example:** A company deploys its application in different regions to improve access for international customers.

### Security Considerations

- Check data residency requirements.
- Follow applicable privacy laws and contracts.
- Understand where data is stored and processed.
- Configure access controls consistently across regions.

> **Global reach helps serve users worldwide, but d**
>
> **ata-location requirements still matter.**

### Quick Comparison

| Benefit                         | Meaning                                        | Security Consideration             |
| ------------------------------- | ---------------------------------------------- | ---------------------------------- |
| Scalability and elasticity      | Adjust capacity to demand                      | Secure new resources               |
| Cost management                 | Reduce the need for upfront hardware purchases | Monitor usage and billing          |
| Access from different locations | Reach services over a network                  | MFA and least privilege            |
| Backup and recovery             | Restore data and systems                       | Protect and test backups           |
| Global reach                    | Serve users across regions                     | Respect data-location requirements |

> **Remember:** Cloud benefits are strongest when cost, access, configuration, and recovery are managed properly.

---

## 5. Enterprise Cloud Adoption

**Enterprise cloud adoption** is the process of an organization starting to use cloud services to run applications, store data, or manage IT resources.

A company can adopt cloud gradually. It does not have to move every system at once.

**Example:** A hospital moves its appointment-booking system to the cloud while keeping other systems in its existing environment.

### Why Organizations Adopt Cloud Services

- Reduce the need for upfront hardware purchases.
- Increase or decrease resources as business needs change.
- Deploy applications more quickly.
- Improve backup and recovery options.
- Support authorized access from different locations.

Successful adoption requires planning, security reviews, testing, and ongoing management.

### Typical Cloud Adoption Steps

```text
Plan
  ↓
Assess Risks
  ↓
Choose Provider and Services
  ↓
Migrate Applications and Data
  ↓
Test and Secure
  ↓
Monitor and Improve
```

1. **Plan:** Decide what to move and why.
2. **Assess risks:** Identify sensitive data, dependencies, legal requirements, and security risks.
3. **Choose services:** Select the provider, service model, and suitable region.
4. **Migrate:** Move applications and data or adapt them for cloud services.
5. **Test and secure:** Check functionality, permissions, backups, and monitoring.
6. **Monitor and improve:** Review cost, performance, security alerts, and access permissions.

### Cloud Migration Strategies

#### Rehost — Lift and Shift

Move an application to the cloud with few changes.

**Example:** Move an existing virtual machine to a cloud virtual machine.

#### Replatform

Move an application while making selected improvements.

**Example:** Replace a self-managed database with a managed cloud database service.

#### Refactor or Re-architect

Redesign an application to make better use of cloud capabilities.

**Example:** Break a large application into smaller services.

#### Retire

Stop using an application that is no longer needed.

**Example:** Decommission an outdated internal tool.

#### Retain

Keep an application where it is for now.

**Example:** Leave a system in its existing environment until a technical dependency is resolved.

### Migration Strategy Comparison

| Strategy   | Meaning                                  |
| ---------- | ---------------------------------------- |
| Rehost     | Move with few changes                    |
| Replatform | Move with selected improvements          |
| Refactor   | Redesign the application                 |
| Retire     | Stop using an unnecessary application    |
| Retain     | Keep the application where it is for now |

### Common Security Risks

#### 1. Stolen Credentials

#### 2. Storage Misconfiguration

#### 3. Exposed Services or Ports

#### 4. Poor Monitoring

#### 5. Excessive Permissions

#### 6. Data Loss or Ransomware




> **Remember:** Cloud adoption is not just moving an application. It includes planning, risk assessment, migration, testing, security, and continuous monitoring.

---

## Conclusion

Cloud computing allows organizations to use computing resources without managing every part of the physical infrastructure themselves.

The five main ideas in this task are:

1. **Cloud computing:** Using computing resources over a network.
2. **Cloud service models:** Understanding IaaS, PaaS, and SaaS.
3. **Cloud deployment models:** Understanding public, private, hybrid, and community cloud.
4. **Cloud benefits:** Understanding flexibility, cost management, access, recovery, and global reach.
5. **Enterprise cloud adoption:** Planning and migrating to the cloud while managing security risks.
