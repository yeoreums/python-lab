# Python Lab

Structured daily practice to build practical Python skills for **data processing and backend logic**.

## Purpose

This repository follows a progressive learning approach:

* Small daily exercises (30–60 minutes)
* Focus on real-world logic instead of isolated syntax
* Emphasis on data transformation, aggregation, and reporting
* Building foundations for:

  * Data analysis
  * Data engineering
  * Backend processing

---

## Learning Progression

### Core Programming (Day 5–20)

* Functions and modular design
* Problem decomposition
* CLI applications
* File I/O and persistence
* Project structure (`app / logic / storage`)

### Data Processing (Day 21–26)

Working with tabular data using pure Python:

* Read CSV files
* Parse structured rows
* Aggregation using dictionaries (**GROUP BY**)
* Nested aggregation (multi-level grouping)
* Sorting aggregated results (**ORDER BY**)

Workflow pattern:

```
CSV → Parse → Aggregate → Sort → Report
```

This mirrors real data pipeline logic and prepares for future use of:

* Pandas
* SQL
* ETL workflows

---

## Structure

Each folder represents one day of focused practice.

Examples:

```
day21_read_csv_lines
day22_parse_csv_rows
day23_group_by_date
day24_group_by_category
day25_group_by_date_and_category
day26_top_categories
```

An `interview_prep` folder contains small problem-style exercises based on common data-processing patterns.

---

## Approach

* Progressive difficulty (slightly harder each day)
* Minimal external libraries
* Focus on understanding execution and data flow
* Emphasis on clean, readable logic

---

## Next Direction

* Top-N analysis
* Filtering and reporting
* Pandas-based workflows
* Small end-to-end data projects
