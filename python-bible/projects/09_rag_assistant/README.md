# AI/RAG Knowledge Assistant

Production blueprint: document ingestion → text extraction → chunking → embeddings → vector index → retrieval → LLM answer → source citations.

Required implementation gates: provider abstraction, environment-based secrets, document metadata, retrieval tests, prompt-injection defenses, evaluation set, request logging without sensitive document leakage, and API boundary.

This project is intentionally provider-neutral. Add the selected embedding/vector/LLM SDKs as dependencies rather than hard-coding credentials or a vendor.
