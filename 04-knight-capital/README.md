# Episode 04: The Knight Capital $440M Disaster

Forensic technical autopsy of the August 1, 2012 automated trading meltdown.

- **Financial Impact:** $440,000,000 USD (Insolvency in 45 minutes)
- **Trade Volume:** 397 million shares across 4 million executions
- **Root Cause:** A manual deployment missed Server #8, causing a repurposed feature flag to execute dormant 2003 test code without fill-tracking logic.

---

### Technical Breakdown

Between July 27 and July 31, 2012, Knight engineers manually deployed an updated SMARS build to 8 production servers, but omitted Server #8.

When the NYSE opened at 9:30 AM:
1. An existing configuration flag was toggled on. On servers 1–7, it routed orders through the new Retail Liquidity Program.
2. On server 8, that same flag triggered **"Power Peg"**—an obsolete test routine from 2003 that was never deleted.
3. Power Peg sent rapid child orders without verifying parent order completion.
4. Server 8 bought at the ask and sold at the bid continuously, burning ~$10 million per minute until halted.

---

### Engineering Takeaways

1. **Purge Retired Code:** Deprecated features must be deleted from the codebase, not masked behind configuration toggles.
2. **Eliminate Manual Deployments:** Node-by-node updates invite drift. Use atomic, automated deployment pipelines with cryptographic checksum verification.
3. **Network Circuit Breakers:** Distributed high-velocity systems must maintain hard financial kill switches at the network perimeter.

---

### How to Run Simulation

```bash
python simulation.py
