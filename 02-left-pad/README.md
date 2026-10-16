# codeinspect-autopsies
Production post-mortems, architectural analysis, and incident autopsies from the CodeInspect documentary series.

# Incident Autopsy #02: The Left-Pad Collapse (March 2016)

> **Watch the 50-Second Visual Breakdown:** [CodeInspect Episode 02 on YouTube](https://youtube.com/shorts/kewqZmvzGhY)

---

## Incident Overview
On March 22, 2016, a single command—`npm unpublish left-pad`—knocked down CI/CD pipelines, Docker builds, and deployment workflows globally. Thousands of enterprise applications (including builds at Meta, PayPal, and Netflix) ground to a halt within minutes.

## The Trigger
The incident was rooted in a trademark dispute between developer Azer Koçulu and messaging platform Kik. When npm leadership manually transferred ownership of Koçulu's `kik` package to the corporation, Koçulu unpublished all 273 of his modules from the registry in protest.

Among those unpublished packages was `left-pad@0.0.3`, an 11-line string utility function.

## Why the Internet Broke (Transitive Dependency Cascades)
Virtually no major company imported `left-pad` directly. Instead:
1. Industry tooling like `babel-core` depended on intermediate utilities (such as `line-numbers`).
2. Those libraries pinned an exact version constraint: `"left-pad": "0.0.3"`.
3. When automated CI/CD runners executed `npm install`, the registry returned `HTTP 404: Not Found`.

Because lockfile enforcement (`package-lock.json`) did not exist natively in npm at the time, automated build scripts re-resolved upstream trees dynamically, collapsing the entire dependency graph.

## Architectural Lessons & Permanent Fixes
1. **Registry Immutability:** npm removed unrestricted package unpublishing. Today, packages depended on by other projects cannot be yanked abruptly.
2. **Deterministic Lockfiles:** Standardized lockfiles (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`) ensure build pipelines do not dynamically pull unpinned upstream assets.
3. **Artifact Caching & Private Proxies:** Enterprise stacks now mirror dependencies through private registries (Nexus, Artifactory, Cloudsmith) rather than resolving raw public registries in production CI/CD.

---
*Created by [CodeInspect](https://youtube.com/@CodeInspect). New incident autopsies every Monday & Wednesday.*
