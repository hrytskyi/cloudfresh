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
   - Add four subnets: `public-subnet-1`, `public-subnet-2`, `private-subnet-1`, `private-subnet-2` with appropriate IP ranges (10.0.1.0/24, 10.0.2.0/24, 10.1.1.0/24, 10.1.2.0/24).

### Step 2: Configuring VM Instances
1. **Create VM instances**:
   - Navigate to the VM instances section in the GCP Console.
   - Click on "Create instance".
   - Create one VM instance in each subnet (`test-vm1`, `test-vm1`, `test-vm1`, `test-vm1`).
   - Assign appropriate tags to the instances for easier firewall management (`public-vm` and `private-vm`).

### Step 3: Configuring Firewall Rules
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
3. **Allow traffic between private subnets**:
```
   gcloud compute firewall-rules create allow-private-traffic \
    --direction=INGRESS \
    --priority=1000 \
    --network=vpc1 \
    --action=ALLOW \
    --rules=icmp \
    --source-ranges=10.0.3.0/24,10.0.4.0/24 \
    --target-tags=private-vm
```
4. **Block traffic between private and public subnets**:
```
   gcloud compute firewall-rules create deny-private-to-public \
    --direction=INGRESS \
    --priority=1000 \
    --network=vpc1 \
    --action=DENY \
    --rules=icmp \
    --source-ranges=10.0.3.0/24,10.0.4.0/24 \
    --target-tags=public-vm
```
5. **Add tags to VM instances**:
```
   gcloud compute instances add-tags test-vm-3 --tags=public-vm
   gcloud compute instances add-tags test-vm-4 --tags=public-vm
   gcloud compute instances add-tags test-vm-1 --tags=private-vm
   gcloud compute instances add-tags test-vm-2 --tags=private-vm
```
### Step 4: Network Troubleshooting

1.  **Verify connectivity**:
    
    -   We can verify that public VMs can communicate with each other, but can't reach private VMs. The same is with private VMs: they can communicate, but cant access public VMs.

## Conclusion

By following the above steps, a virtual network with the specified subnets and VM instances is successfully set up. Proper communication between the public and private subnets is ensured, and basic network troubleshooting steps are demonstrated.
