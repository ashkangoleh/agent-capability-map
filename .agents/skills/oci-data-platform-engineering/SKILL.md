---
name: oci-data-platform-engineering
description: "Design Oracle Cloud data platforms across Object Storage, Data Flow, GoldenGate, Streaming and Autonomous Database."
license: Proprietary
metadata:
  version: "1.1.0"
---

# oci-data-platform-engineering

## Activation boundary
Use for OCI data platform design and operations, not general OCI network/compute administration.

## Required inputs
Region/tenancy; compartments; IAM; sources; Data Flow/Spark version; GoldenGate; Streaming retention; Object Storage; database workload.

## Production workflow
1. Define compartment boundaries, dynamic groups and least-privilege IAM.
2. Use Object Storage for durable landing with encryption and lifecycle.
3. Select Data Flow for managed Spark where runtime/connectors fit.
4. Use GoldenGate for supported CDC; define capture position, trail retention and apply checkpoint.
5. Use OCI Streaming where partitioning and retention fit.
6. Monitor service limits, lag, job duration, lifecycle and spend.

## Failure modes and recovery
- IAM denial: inspect principal and compartment scope.
- GoldenGate lag: separate extract, transport and apply.
- Data Flow failure: preserve logs and immutable inputs.
- Streaming retention expiry: define checkpoint and replay SLA.
- Region mismatch: validate availability and residency.

## Validation and evidence
- Test GoldenGate catch-up, Data Flow retry, consumer recovery and object restore.
- Verify production identity permissions.
- Measure lag, duration, throughput, cost and quota headroom.

## Output contract
Return service topology, IAM design, data flow, recovery and rollout gates.

## Official references
- https://docs.oracle.com/en-us/iaas/data-flow/using/home.htm
- https://docs.oracle.com/en-us/iaas/goldengate/
