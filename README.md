# Episode 05: The Ariane 5 Flight 501 Disaster

Forensic technical autopsy of the Ariane 5 self-destruction on June 4, 1996.

- **Cost of Disaster:** ~$370,000,000 USD
- **Liftoff to Destruction:** 37 seconds
- **Root Cause:** Software exception (`Ada Numerical_Error`) during a 64-bit floating-point to 16-bit signed integer conversion.

---

### Technical Autopsy

The Inertial Reference System (SRI) software was reused directly from the older **Ariane 4** rocket. Ariane 5 had a significantly steeper flight profile, resulting in horizontal bias values ($BH$) far exceeding $32,767$ (the maximum boundary of a signed 16-bit integer: $2^{15} - 1$).

Because the Ada conversion code lacked an explicit exception handler:
1. Primary computer (SRI 1) halted execution due to arithmetic overflow.
2. Secondary backup computer (SRI 2) was running identical code and halted milliseconds later.
3. Diagnostic telemetry was misinterpreted by the autopilot computer as active flight commands.
4. Engine nozzles swiveled to physical limits, ripping the rocket apart under aerodynamic shear.

---

### How to Run Simulation

```bash
python simulation.py
