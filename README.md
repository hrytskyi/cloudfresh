#  Part 2: **Networking**

## Objective
Assess basic networking knowledge.
## Task
1. Set up a simple virtual network in GCP with at least two subnets.
2. Configure a VM instance in each subnet.
3. Ensure the VM instances can communicate with each other.
4. Demonstrate basic network troubleshooting steps if communication fails.



## Steps

### Step 1: Setting Up the Virtual Network
1. **Create a VPC network**: 
   - Navigate to the VPC Network section in the GCP Console.
   - Click on "Create VPC network".
   - Name the network `internship-test`.
![Screenshot 2024-07-30 103315](https://github.com/user-attachments/assets/5fcd4abb-1129-4989-94ec-6716c4039645)

   - Add four subnets: `public-subnet-1`, `public-subnet-2`, `private-subnet-1`, `private-subnet-2` with appropriate IP ranges (10.0.1.0/24, 10.0.2.0/24, 10.1.1.0/24, 10.1.2.0/24).
![Screenshot 2024-07-30 103509](https://github.com/user-attachments/assets/bfeaa176-3059-4e57-80fe-50b6b973c3d0)


### Step 2: Configuring VM Instances
1. **Create VM instances**:
   - Navigate to the VM instances section in the GCP Console.
   - Click on "Create instance".
   - Create one VM instance in each subnet (`test-vm1`, `test-vm1`, `test-vm1`, `test-vm1`).
![Screenshot 2024-07-30 110827](https://github.com/user-attachments/assets/899e50b8-71b6-446d-b455-22ddfb1bc113)

   - Assign appropriate tags to the instances for easier firewall management (`public-vm` and `private-vm`).
   
```
   gcloud compute instances add-tags test-vm-3 --tags=public-vm
   gcloud compute instances add-tags test-vm-4 --tags=public-vm
   gcloud compute instances add-tags test-vm-1 --tags=private-vm
   gcloud compute instances add-tags test-vm-2 --tags=private-vm
```
![Screenshot 2024-07-30 113613](https://github.com/user-attachments/assets/bfce27a0-4fe6-434e-927f-8acd76ce1fe3)

### Step 3: Configuring Firewall Rules
0. **Configure firewall rules to allow ICMP**:
![Screenshot 2024-07-30 103529](https://github.com/user-attachments/assets/9f0fc97f-d7f8-4c6f-afd8-696e17c8e8e8)

1. **Allow traffic between public subnets**:
```
   gcloud compute firewall-rules create allow-public-traffic \
       --direction=INGRESS \
       --priority=1000 \
       --network=vpc1 \
       --action=ALLOW \
       --rules=icmp \
       --source-ranges=10.0.1.0/24,10.0.2.0/24 \
       --target-tags=public-vm
```
![Screenshot 2024-07-30 112537](https://github.com/user-attachments/assets/c50819a1-b636-4a44-9ab8-8897e1ff93fc)

2. **Block traffic between public and private subnets**:
```
 gcloud compute firewall-rules create deny-public-to-private \
    --direction=INGRESS \
    --priority=1000 \
    --network=vpc1 \
    --action=DENY \
    --rules=icmp \
    --source-ranges=10.0.1.0/24,10.0.2.0/24 \
    --target-tags=private-vm
```
![Screenshot 2024-07-30 113010](https://github.com/user-attachments/assets/cfcb3f1f-853a-4117-b00f-298b21d7ae1e)

3. **Allow traffic between private subnets**:
```
   gcloud compute firewall-rules create allow-private-traffic \
    --direction=INGRESS \
    --priority=1000 \
    --network=vpc1 \
    --action=ALLOW \
    --rules=icmp \
    --source-ranges=10.1.1.0/24,10.1.2.0/24 \
    --target-tags=private-vm
```
![Screenshot 2024-07-30 113218](https://github.com/user-attachments/assets/14bac948-b7c3-4ab8-a499-5869f67f6a99)

4. **Block traffic between private and public subnets**:
```
   gcloud compute firewall-rules create deny-private-to-public \
    --direction=INGRESS \
    --priority=1000 \
    --network=vpc1 \
    --action=DENY \
    --rules=icmp \
    --source-ranges=10.1.1.0/24,10.1.2.0/24 \
    --target-tags=public-vm
```
![Screenshot 2024-07-30 113323](https://github.com/user-attachments/assets/45a33548-2255-4710-a29b-65b124e1503e)

### Step 4: Network Troubleshooting

1.  **Verify connectivity**:
    
    -   We can verify that public VMs can communicate with each other, but can't reach private VMs. The same is with private VMs: they can communicate, but cant access public VMs.

test-vm-1:

![Screenshot 2024-07-30 113736](https://github.com/user-attachments/assets/3e6b65b3-2579-4ee6-ab48-53bda16da568)

test-vm-2:

![Screenshot 2024-07-30 113834](https://github.com/user-attachments/assets/8e2b7877-921b-4e5e-8385-053c4f24b736)

## Conclusion

By following the above steps, a virtual network with the specified subnets and VM instances is successfully set up. Proper communication between the public and private subnets is ensured, and basic network troubleshooting steps are demonstrated.
![Screenshot 2024-07-30 105803](https://github.com/user-attachments/assets/0ce4db70-b3b0-4746-bf73-a38af05e1321)

