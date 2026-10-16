# CodeInspect: Incident Autopsies

Forensic post-mortems, root cause analyses, and executable simulations of history's costliest software crashes, architectural oversights, and system engineering failures.

---

## 📂 Incident Registry

| Ep | Incident | Date | Failure Mechanism | Impact | Technical Post-Mortem |
|:--:|:---|:--:|:---|:---|:--:|
| **#02** | **The Left-Pad Collapse** | Mar 2016 | Fragile transitive dependency & unpublishing | Global npm CI/CD pipeline breakage | [View Autopsy](./02-left-pad) |
| **#04** | **Knight Capital Group** | Aug 2012 | Dead code execution & feature flag collision | $440M insolvency in 45 minutes | [View Autopsy](./04-knight-capital) |
| **#05** | **Ariane 5 Flight 501** | Jun 1996 | 64-bit float to 16-bit signed integer overflow | $370M rocket destruction at T+37s | [View Autopsy](./05-ariane-5-overflow) |

---

## 🛠️ Repository Architecture

Each directory functions as an isolated incident case study containing:
* **`README.md`**: Complete architectural breakdown, sequence of failure events, root causes, and systemic prevention rules.
* **Source / Simulation Scripts**: Minimal, runnable reproductions (`simulation.py`, `index.js`) isolating the exact logic trap or defect.

```text
codeinspect-autopsies/
├── 02-left-pad/
│   ├── index.js                  # The 11-line string utility
│   └── README.md                 # Transitive dependency post-mortem
├── 04-knight-capital/
│   ├── simulation.py             # Runaway Power Peg loop simulation
│   └── README.md                 # Deployment desync & dead code audit
├── 05-ariane-5-overflow/
│   ├── simulation.py             # Float64 to Int16 numeric overflow simulation
│   └── README.md                 # SRI inertial guidance failure audit
└── README.md                     # Incident index & community hub

 ## 🌐 Community & Official Links

* 📺 **YouTube:** [https://www.youtube.com/@CodeInspect]
* 📸 **Instagram:** [https://www.instagram.com/codeinspect_tech]
* 💬 **Discord:** [https://discord.gg/wR373CCyGf]
