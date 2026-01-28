# Financial Transactions Analyzer

A clean, beginner-friendly yet professional Python project that ingests raw transaction data, cleans it safely, validates it against financial rules, and produces meaningful analytical outputs.

This project is designed to demonstrate **real-world data engineering practices**: correctness over cleverness, auditability, and clean Git workflow.

---

##  What This Project Does

The pipeline processes raw transaction data and produces:

* *Valid transactions* (clean, rule-compliant)
* *Rejected transactions* (with clear rejection reasons)
* *User-level spend analysis*

It explicitly avoids silent data corruption and makes every decision traceable.

---

## 🧠 Why This Project Exists

Many beginner projects:

* silently drop bad data
* mix cleaning and validation
* rely on brittle row-by-row logic
* look correct but fail in edge cases

This project intentionally avoids those traps and follows practices used in real analytics / data teams.

---

##  Project Structure

```
financial-transactions-analyzer/
│
├── analyzer/
│   ├── __init__.py
│   ├── loader.py        # Reads raw CSV data
│   ├── cleaner.py       # Safe data normalization (no corruption)
│   ├── validator.py     # Business rule enforcement & auditability
│   ├── analysis.py      # Aggregations and analytics
│   └── anomalies.py     # (reserved for future anomaly detection)
│
├── data/
│   └── raw/
│       └── transactions.csv   # Sample input data
│
├── tests/
│   └── test_cleaner_*.py       # Unit tests for cleaning logic
│
├── main.py                     # Pipeline orchestrator
├── requirements.txt
├── .gitignore
└── README.md
```

---

##  Data Flow (End-to-End)

```
Raw CSV
   ↓
Loader (read file)
   ↓
Cleaner (normalize safely)
   ↓
Validator (business rules)
   ↓
Valid CSV  +  Rejected CSV (with reasons)
   ↓
Analysis outputs
```

Each step has **one responsibility** and does it deterministically.

---

##  Validation Rules Implemented

Transactions are **rejected** if they violate any of the following:

* Missing required fields
* Invalid or zero/negative amount
* Amount exceeds a sanity upper bound
* Unsupported currency
* Future timestamp
* Duplicate transaction IDs

Rejected rows are **not dropped** — they are saved with explicit reasons.

---

##  How to Run the Project

###  Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

###  Run the pipeline

```bash
python main.py
```

###  Outputs

Generated files (ignored by Git):

* `data/processed/valid_transactions.csv`
* `data/processed/rejected_transactions.csv`
* `data/processed/user_spend_summary.csv`

---

##  Tests

Unit tests validate that:

* text fields are normalized correctly
* empty and malformed values are handled safely

Run tests:

```bash
pytest
```

---

## 🛠 Design Principles Followed

* **No silent data loss**
* **Vectorized pandas operations** (no iterrows)
* **Timezone-safe timestamps**
* **Auditability over convenience**
* **Beginner-readable, reviewer-friendly code**

---

## 🔮 Future Improvements

* Add anomaly detection (outliers, fraud signals)
* Add logging instead of print statements
* Add CLI arguments (input/output paths)
* Add integration tests
* Add visualization layer

---


##  Final Note

This is a small project, but it’s built with the same habits used in real data teams: be explicit, avoid surprises, and keep the pipeline easy to understand.
