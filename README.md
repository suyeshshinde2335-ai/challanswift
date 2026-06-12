# ChallanSwift: Enterprise Traffic Enforcement Pipeline 🚦🏎️

An automated, text-based digital traffic compliance and fine simulator designed for on-duty traffic officers and RTO authorities. Built purely on core Python control structures for 100% operational transparency and zero-latency receipt processing.

---

## 📊 System Architecture & Logic Flow

Below is the logical data routing pipeline for every vehicle processed under the **v6.0 Production Build**:

```text
   [Vehicle Input Logged]
              │
              ▼
   Is Emergency Vehicle? ───(Yes)───► [Waiver Applied: Rs 0 Fine] ───► [Print Receipt]
              │                                                               ▲
            (No)                                                              │
              ▼                                                               │
     [Select Vehicle Type]                                                    │
              │                                                               │
     ┌────────┴────────┐                                                      │
     ▼                 ▼                                                      │
[Two-Wheeler]    [Four-Wheeler]                                               │
     │                 │                                                      │
  Helmet?           Seatbelt?                                                 │
     │                 │                                                      │
     └────────┬────────┘                                                      │
              ▼                                                               │
     [Speed Check Engine] ───► [License Validation] ───► [Sobriety Check] ────┘
