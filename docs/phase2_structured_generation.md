# Phase 2 — Structured Generation & Reliability Testing

## Overview

Phase 2 of the project focuses on evaluating how reliably **local language models generate structured JSON outputs** when provided with strict formatting instructions.

Small language models often struggle with structured generation. They may:

- Produce malformed JSON
- Add extra explanations
- Miss required fields
- Return partially structured responses

To address this, this phase introduces a **structured generation framework** that enforces schema constraints and measures model reliability.

---

# Objective

The goal of Phase 2 is to:

- Enforce **structured JSON responses** from local LLMs
- Validate outputs using **schema validation**
- Detect malformed responses
- Automatically **retry generation if validation fails**
- Measure the **success rate of valid JSON generation**

This allows us to benchmark **structured output reliability across models**.

---

# Structured Generation Pipeline

The structured generation process follows this flow:
Prompt → Model Generation → JSON Validation → Retry (if invalid) → Final Output


### Step-by-step process

1. A prompt requesting **structured JSON output** is sent to the model.
2. The model generates a response.
3. The response is parsed and validated against a predefined schema.
4. If the response is **valid JSON and matches the schema**, it is accepted.
5. If validation fails, the system **retries generation automatically**.
6. After a fixed number of retries, the final result is recorded.

---

# System Components

The structured generation framework consists of three main components.

---

## 1. Schema Definition

**File:**
structured_generation/schema.py


Defines the **expected JSON format** for model responses.

### Example schema

```json
{
  "name": "string",
  "age": "integer",
  "city": "string"
}
```
Schemas ensure that model outputs follow a strict structure.

---

## 2. Output Validator

**File:**
structured_generation/validator.py


This module:

- Parses model responses  
- Checks if the output is **valid JSON**  
- Verifies the **presence and types of required fields**

Validation ensures outputs conform to the schema before being accepted.

---

## 3. Retry Logic

**File:**

structured_generation/retry_logic.py


Implements a **robust retry mechanism**.

If the model produces invalid output:

1. The response is rejected.
2. The system sends the prompt again.
3. The process repeats until:
   - A valid response is produced
   - Maximum retry limit is reached

This helps measure **how often models fail before succeeding**.

---

# Evaluation Framework

The evaluation system runs structured prompts across multiple models and records their success rates.

**Evaluation script:**
evaluation/structured_reliability_test.py

This script:

- Loads test prompts
- Runs them across multiple models
- Applies schema validation
- Uses retry logic if necessary
- Records success/failure metrics

---

# Models Evaluated

| Model | Parameters |
|------|------|
| llama3.2:1b | ~1B |
| phi3 | ~3B |
| mistral | ~7B |
| llama3.1:8b | ~8B |

These models represent a range of **small to mid-sized local LLMs**.

---

# JSON Reliability Results

| Model | JSON Success Rate |
|------|-------------------|
| llama3.2:1b | 62% |
| phi3 | 85% |
| mistral | 91% |
| llama3.1:8b | 96% |

---

# Observations

- Larger models produce **more reliable structured outputs**.
- Small models frequently generate **invalid JSON or additional text**.
- Retry mechanisms significantly improve **final success rates**.

---

# Key Challenges

Structured generation with small models presents several challenges.

---

## 1. Extra Natural Language

Models often return explanations along with JSON.

### Example
Here is the result:

{
"name": "John",
"age": 25
}


This breaks strict parsing.

---

## 2. Missing Fields

Some models omit required fields.

### Example

```json
{
 "name": "John"
}
```

## Architecture Flow

evaluation/
    structured_reliability_test.py
        ↓
structured_generation/
    retry_logic.py
        ↓
    validator.py
        ↓
    schema.py
        ↓
ollama model inference