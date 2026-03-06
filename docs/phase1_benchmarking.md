# Phase 1 — Local LLM Benchmarking

## Objective

The goal of Phase 1 is to measure the inference performance of multiple
local language models running on consumer hardware.

Understanding these metrics is important when designing systems that rely
on local inference such as offline assistants or privacy-focused AI tools.

---

## Metrics Measured

The benchmark collects the following metrics:

### Time To First Token (TTFT)

Time taken by the model to generate the first token after receiving a prompt.

This reflects the **initial response delay** experienced by users.

---

### Tokens Per Second

The speed at which the model generates tokens during inference.

Higher values indicate faster generation speed.

---

### Total Latency

Total time required for the model to generate the complete response.

---

### Average Tokens Generated

Average number of tokens produced per prompt.

This ensures comparisons remain fair across models.

---

## Benchmark Methodology

1. A standardized dataset of prompts was created.
2. Each model was executed using the same prompt set.
3. Metrics were collected for every inference run.
4. Results were averaged across prompts.

---

## Models Evaluated

| Model | Approx Parameters |
|------|------------------|
| llama3.2:1b | 1B |
| phi3 | ~3B |
| mistral | ~7B |
| llama3.1:8b | 8B |

---

## Hardware Configuration

GPU: NVIDIA RTX 4050 Laptop GPU  
VRAM: 6GB  
CUDA Version: 13.1  

---

## CPU vs GPU Evaluation

Benchmarking was performed on both CPU and GPU to understand
how hardware affects inference performance.

CPU vs GPU Benchmark Results

| Model       | TTFT CPU (s) | TTFT GPU (s) | Tokens/sec CPU | Tokens/sec GPU | Latency CPU (s) | Latency GPU (s) |
| ----------- | ------------ | ------------ | -------------- | -------------- | --------------- | --------------- |
| llama3.2:1b | 0.381        | 0.410        | 124.77         | 124.52         | 3.889           | 3.777           |
| phi3        | 0.250        | 0.252        | 70.89          | 69.97          | 4.166           | 4.531           |
| mistral     | 0.308        | 0.298        | 37.75          | 36.90          | 8.862           | 9.073           |
| llama3.1:8b | 0.561        | 0.549        | 24.90          | 25.16          | 20.549          | 20.313          |

GPU inference was verified using:

nvidia-smi -l 1

While running models, GPU utilization increased and VRAM allocation rose significantly, confirming GPU-accelerated inference.

Example:

![GPU Inference](images/gpu_inference_proof.png)

---

## Key Insights

1. Small models show minimal performance difference between CPU and GPU.
2. Larger models benefit slightly from GPU acceleration.
3. Model size has a larger impact on inference speed than hardware.
4. Models between **1B–3B parameters provide excellent latency for local systems**.

---

## Conclusion

This phase establishes a baseline understanding of local model inference
performance. These insights guide the selection of models for structured
generation tasks in later phases of the project.