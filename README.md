<div align="center">

# Danil Silantyev

<p align="center">
  <img src="https://img.shields.io/badge/Co--Founder_&_CEO-NDDev-1a1a2e?style=for-the-badge" alt="Co-Founder & CEO @ NDDev"/>
  <img src="https://img.shields.io/badge/Co--Founder_&_CTO/CAIO-Curestry-0f3460?style=for-the-badge" alt="Co-Founder & CTO @ Curestry"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AI_Architect-16213e?style=flat-square" alt="AI Architect"/>
  <img src="https://img.shields.io/badge/Data_Scientist-16213e?style=flat-square" alt="Data Scientist"/>
  <img src="https://img.shields.io/badge/Technical_Visionary-16213e?style=flat-square" alt="Technical Visionary"/>
</p>

<p align="center">
  Kazakhstan / Worldwide &nbsp;&bull;&nbsp;
  <a href="mailto:danil@nddev.it.com">danil@nddev.it.com</a> &nbsp;&bull;&nbsp;
  <a href="https://t.me/Danil_Silantyev">Telegram</a> &nbsp;&bull;&nbsp;
  <a href="https://www.linkedin.com/in/danil-silantyev-ai/">LinkedIn</a>
</p>

</div>

---

## About

I architect and ship production-grade AI systems at scale. 4+ years of hands-on ML/AI engineering, system design, and technical leadership across two companies and a team of ~10 engineers.

I build at the intersection of **AI research and production reality**: LLM observability platforms, multi-agent orchestration (50+ node LangGraph pipelines with conditional routing and human-in-the-loop), dual-database architectures (OLTP + OLAP), and ML pipelines that handle multi-TB workloads in the real world.

**Track record:** 20+ delivered business projects. 30+ system architectures designed from scratch. Manufacturing, civic tech, e-commerce, industrial sectors.

---

## Curestry - LLM Observability & Root Cause Analysis Platform

> Co-Founder & CTO/CAIO | Building the debugging layer for the AI era

**Curestry** is an AI operations platform providing intelligent diagnostics for LLM-powered applications. It combines automated root cause analysis, systematic prompt optimization, and high-throughput trace analytics into a unified observability layer.

**Key differentiators:**
- **15 specialized analyzers** across a 4-tier analysis pipeline (42 metrics total)
- **Multi-agent RCA** - LangGraph 12-node orchestration for automated failure diagnostics
- **Prompt Optimization** - A/B testing, scoring, and auto-tuning with multi-vendor LLM support
- **Client ecosystem** - VSCode extension + Chrome extension (MV3) for in-workflow integration
- **Dual-database architecture** - PostgreSQL (OLTP) + ClickHouse (OLAP) for traces at scale

```
Curestry Platform (11 services)
├── Web Dashboard          Next.js 16, React 19, TypeScript, tRPC
├── Worker Service         BullMQ job processing, background analytics
├── RCA Core               FastAPI, LangGraph, LiteLLM (Vertical Slice Architecture)
│   ├── 8 feature slices   (findings, analysis, code_scanner, comparator, chat, connectors, optimizer, systems)
│   ├── Multi-agent RCA    Root cause analysis with corrective recommendations
│   └── Findings engine    51 types across 10 categories, SHA256 deduplication
├── Prompt Optimization    15 analyzers, 4-tier pipeline (quick→standard→thorough)
├── Client SDK             Python SDK + JavaScript SDK (@curestry/client, @curestry/core, @curestry/langchain)
├── Extensions             VSCode extension + Chrome extension (Bridge pattern + FSD)
├── Data Layer
│   ├── PostgreSQL 18+     OLTP - Prisma + Alembic migrations (strict ownership)
│   ├── ClickHouse 25.8    OLAP - golang-migrate, ReplacingMergeTree, time-series optimized
│   ├── Redis (x2)         Queue (:6379, BullMQ, noeviction) + Cache (:6380, allkeys-lru)
│   └── MinIO              S3-compatible blob storage
├── Observability          Prometheus + Grafana + Loki
└── Infrastructure         Docker (11 services), Caddy reverse proxy, Turborepo + pnpm
```

---

## NDDev - AI/IT Engineering Studio

> Co-Founder & CEO | <a href="https://nddev.it.com">nddev.it.com</a>

Full-cycle AI/IT outsourcing and outstaffing studio (~10 engineers). We design and deliver production solutions for manufacturing, civic tech, and enterprise clients.

**Six divisions:** NDDev Dev, NDDev AI, NDDev Design, NDDev Platform, NDDev RnD, NDDev OpenNetwork.

**Delivery focus:** ML systems, computer vision, full-stack platforms, multi-agent services, mobile applications.

---

## Engineering at Scale - Selected Projects

> Client projects delivered by NDDev. Details anonymized.

| Domain | Scope | Architecture Highlights | Scale |
|--------|-------|------------------------|-------|
| **City-wide digital library ecosystem** | Mobile + Admin + Backend | Flutter (Riverpod), React, FastAPI. Two-service backend, Meilisearch, Firebase, biometric auth, barcode integration | 123 endpoints, 25 models, 1436 tests, 29 screens, 38 admin pages |
| **B2B industrial equipment platform (UAE)** | Full-stack bilingual catalog (EN/AR) | Next.js ISR/SSG, async FastAPI, Feature-Sliced Design, GitHub Actions CI/CD | 10+ domain modules, zero-downtime deploys |
| **Industrial equipment sales platform** | Corporate site + Admin + API | Layered architecture, React Admin, Redis rate limiting, 2FA, SEO with JSON-LD | 541+ products, 13 service modules |
| **Computer vision for road infrastructure** | ML pipeline + CV | Real-time object detection, edge deployment | Production safety system |
| **ML systems for mining operations** | Data pipeline + ML | Multi-TB data processing, optimization models | Industrial-scale analytics |
| **CV for collaborative whiteboards** | Real-time CV pipeline | Object recognition on canvas, Miro-like platform integration | Real-time processing |
| **ML system for agricultural machinery** | Embedded ML | Smart harvester control systems | On-device inference |
| **Subscription marketplace (CIS)** | Frontend platform | Next.js, ISR, i18n, Server Components | Region-wide marketplace |

---

## Open Source & Hackathon Projects

**[hackathon-ai-auditor-agent](https://github.com/rldyourmnd/hackathon-ai-auditor-agent)** - AI-powered code auditing platform with multi-agent analysis. FastAPI + LangGraph + Next.js + VSCode extension + Chrome extension + Admin panel. Monorepo (pnpm workspaces), Docker Compose, PostgreSQL, Redis. *NFNG Hackathon.*

**[local-llm-prompt-optimizer](https://github.com/rldyourmnd/local-llm-prompt-optimizer)** - Offline prompt A/B testing and auto-tuning for local LLMs. Privacy-first architecture with multi-vendor adapter (OpenAI, Claude, Grok, Gemini, Qwen, DeepSeek). FastAPI + React + Telegram bot.

**[telegram_to_pdfVectorDB](https://github.com/rldyourmnd/telegram_to_pdfVectorDB)** - Telegram chat export to AI-ready PDF converter. Smart chunking, dynamic sizing, optimized for vector databases and n8n workflows.

---

## Research

### Uncertainty-Aware Web Agents

Investigating uncertainty quantification for autonomous web-browsing AI agents. Developed **GUAWA** - a framework implementing 5 uncertainty estimation methods based on 6 research papers.

**Implemented methods:**

| Method | Type | Based on |
|--------|------|----------|
| Normalized Entropy | Single-step | H(Y)/log(N) normalization |
| Predictive Entropy | Single-step | Information-theoretic H(Y) |
| Semantic Entropy | Single-step | NLI-based clustering |
| Averaging (RMS/mean/geometric) | Multi-step | SAUP paper |
| UProp (IU+EU decomposition) | Multi-step | UProp paper |

**Core question:** How can agents reliably self-assess confidence before executing real-world actions?

Integrated with REAL benchmark (AGISDK), browser-agent, and tree-search agent implementations. Hyperparameter calibration via Optuna.

---

## Leadership & Soft Skills

Beyond technical execution, I invest in the human side of engineering and leadership:

- **Public Speaking** - Presenting technical solutions and product vision to stakeholders and at events
- **Strategic Decision-Making** - Cognitive frameworks for complex technical and business decisions
- **Team Building & Communication** - Growing a team from scratch, mentoring engineers in AI/ML and system design
- **Business Modeling** - Translating technical capabilities into viable business models and product roadmaps
- **Emotional Intelligence** - Managing cross-functional teams, client relationships, and high-pressure delivery cycles
- **Research Methodology** - Bridging academic research and production engineering, paper-to-product pipeline

*Developed through ITMO University programs: public speaking, cognitive decision-making methods, business modeling, communications and team building, life in science.*

---

## Technical Expertise

<table>
<tr>
<td valign="top" width="50%">

### AI & ML Engineering
<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" />
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV" />
<img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="HuggingFace" />
<img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white" alt="ONNX" />
<img src="https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/W%26B-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black" alt="W&B" />
<img src="https://img.shields.io/badge/Optuna-2A0134?style=flat-square" alt="Optuna" />
</p>

<b>Deep Learning</b> &mdash; CNNs, Transformers, autoencoders, diffusion models<br>
<b>Computer Vision</b> &mdash; detection, segmentation, tracking, OCR<br>
<b>NLP</b> &mdash; embeddings, NER, classification, sentiment analysis<br>
<b>Boosting & Ensembles</b> &mdash; XGBoost, CatBoost, LightGBM, Optuna tuning<br>
<b>Metrics & Evaluation</b> &mdash; custom losses, precision-recall, A/B testing<br>
<b>MLOps</b> &mdash; MLflow, W&B, model registry, feature stores, DVC<br>
<b>Optimization</b> &mdash; quantization (INT8/FP16), pruning, distillation, ONNX, Triton<br>
<b>Research</b> &mdash; uncertainty quantification, Bayesian inference, conformal prediction

### LLM & Agent Systems
<p>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square" alt="LangChain" />
<img src="https://img.shields.io/badge/LangGraph-FF6B35?style=flat-square" alt="LangGraph" />
<img src="https://img.shields.io/badge/LiteLLM-000000?style=flat-square" alt="LiteLLM" />
<img src="https://img.shields.io/badge/CrewAI-FF4B4B?style=flat-square" alt="CrewAI" />
<img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square" alt="LangSmith" />
<img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Anthropic-191919?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic" />
</p>

<b>Orchestration</b> &mdash; 50+ node LangGraph pipelines, conditional routing, fan-out/fan-in, HITL<br>
<b>RAG</b> &mdash; hybrid search, cross-encoder reranking, Graph RAG, multi-modal RAG<br>
<b>Prompting</b> &mdash; chain-of-thought, tree-of-thought, few-shot, structured outputs<br>
<b>Observability</b> &mdash; distributed tracing, eval frameworks, cost analytics, drift detection<br>
<b>Models</b> &mdash; GPT-4o / Claude Opus / Llama / Gemini / Qwen / DeepSeek / Mistral<br>
<b>Fine-tuning</b> &mdash; LoRA, QLoRA, PEFT adapters, DPO alignment<br>
<b>Tooling</b> &mdash; MCP protocol, function calling, agentic orchestration, SSE streaming

### Architecture & Design Patterns

<b>Domain-Driven</b> &mdash; bounded contexts, aggregates, domain events, anti-corruption layers<br>
<b>Architecture</b> &mdash; VSA, FSD, Clean Architecture, Hexagonal (Ports & Adapters)<br>
<b>Data Patterns</b> &mdash; CQRS + Event Sourcing, OLTP/OLAP split, CDC<br>
<b>Distributed</b> &mdash; Saga, Transactional Outbox, choreography vs orchestration<br>
<b>GoF in Production</b> &mdash; Strategy, Observer, Mediator, Factory, Builder, Decorator, Bridge<br>
<b>Migration</b> &mdash; Strangler Fig, Branch by Abstraction<br>
<b>Monorepo</b> &mdash; Turborepo, workspace isolation, shared packages, dependency graphs

</td>
<td valign="top" width="50%">

### Platform Engineering
<p>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js" />
<img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
<img src="https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/ClickHouse-FFCC01?style=flat-square&logo=clickhouse&logoColor=white" alt="ClickHouse" />
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/GraphQL-E10098?style=flat-square&logo=graphql&logoColor=white" alt="GraphQL" />
<img src="https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white" alt="Prisma" />
</p>

<b>Backend</b> &mdash; FastAPI (async, DI, middleware), SQLAlchemy, asyncpg, Alembic, Celery<br>
<b>Frontend</b> &mdash; Next.js (App Router, RSC, ISR/SSG/PPR), React, tRPC, Zustand, TanStack Query<br>
<b>Systems</b> &mdash; Rust for performance-critical services, CLI tools, and data processing pipelines<br>
<b>API Design</b> &mdash; REST, GraphQL, gRPC, tRPC, WebSocket, SSE<br>
<b>Messaging</b> &mdash; Kafka, RabbitMQ, BullMQ, Celery<br>
<b>Search</b> &mdash; Meilisearch, Elasticsearch<br>
<b>Databases</b> &mdash; PostgreSQL, ClickHouse, Redis, MongoDB, MinIO<br>
<b>ORM</b> &mdash; Prisma, SQLAlchemy, Alembic, Drizzle<br>
<b>Extensions</b> &mdash; VSCode (LSP), Chrome (MV3, Service Workers, Bridge pattern)

### Infrastructure & DevOps
<p>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes" />
<img src="https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazonaws&logoColor=white" alt="AWS" />
<img src="https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="GCP" />
<img src="https://img.shields.io/badge/Yandex_Cloud-5282FF?style=flat-square" alt="Yandex Cloud" />
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
<img src="https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white" alt="Jenkins" />
<img src="https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white" alt="Terraform" />
</p>

<b>Containers</b> &mdash; 25+ service Docker Compose, multi-stage builds, health checks<br>
<b>Kubernetes</b> &mdash; Helm charts, HPA, Ingress controllers, service mesh (Istio)<br>
<b>CI/CD</b> &mdash; GitHub Actions, Jenkins, GitLab CI, multi-env pipelines<br>
<b>Cloud</b> &mdash; AWS (ECS, Lambda, S3, SQS), GCP (GKE, Cloud Run), Yandex Cloud<br>
<b>IaC</b> &mdash; Terraform, Ansible<br>
<b>Observability</b> &mdash; Prometheus, Grafana, Loki, Tempo, OpenTelemetry, Jaeger<br>
<b>Proxy</b> &mdash; Nginx, Caddy, Traefik<br>
<b>Deploy</b> &mdash; blue-green, canary, zero-downtime strategies

### Mobile Development
<p>
<img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter" />
<img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white" alt="Dart" />
<img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black" alt="Firebase" />
<img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white" alt="Swift" />
<img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />
</p>

<b>Framework</b> &mdash; Flutter (Riverpod, BLoC, GoRouter, Freezed, build_runner)<br>
<b>State</b> &mdash; Riverpod with codegen, BLoC/Cubit for complex reactive flows<br>
<b>Native</b> &mdash; biometric auth, push (FCM/APNs), NFC, barcode, camera, geolocation<br>
<b>Firebase</b> &mdash; Auth, Firestore, Cloud Functions, Analytics, Crashlytics<br>
<b>Offline-first</b> &mdash; Hive, Drift, SQLite with background sync<br>
<b>Platform</b> &mdash; Swift (iOS) and Kotlin (Android) via platform channels<br>
<b>CI/CD</b> &mdash; Fastlane, Codemagic<br>
<b>UI</b> &mdash; Material 3, Cupertino widgets, responsive adaptive layouts

</td>
</tr>
</table>

---

## Competition Track Record

| Year | Event | Result |
|------|-------|--------|
| 2025 | AI Talent Hub ITMO | **1st place** |
| 2025 | Leaders of Digital Transformation | **3rd place** |
| 2024 | Digital Almaty Product Hackathon | **2nd place** |
| 2024 | AI Talent Hub ITMO | **4th place** |
| 2023 | Kaspersky Hackathon | **1st place** |
| 2022 | NASA Space Apps Challenge | **3rd place** |

---

## Education

**ITMO University** - Faculty of Programming and Computer Technologies

**Technical focus:** LLM engineering, AI agent architectures, MLOps, distributed systems.

**Leadership programs:** Public speaking, cognitive decision-making methods, business modeling, communications & team building, scientific methodology.

Mentoring team engineers in AI/ML technologies and system design practices.

---

## Beyond Engineering

Mountain hiking, strategic board games, chess, world history and historical landmarks, travel. I read scientific papers for fun and play Civilization for the decision trees.

---

<div align="center">

<a href="https://t.me/Danil_Silantyev">
<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram" />
</a>
&nbsp;
<a href="mailto:danil@nddev.it.com">
<img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
</a>
&nbsp;
<a href="https://www.linkedin.com/in/danil-silantyev-ai/">
<img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
&nbsp;
<a href="https://nddev.it.com">
<img src="https://img.shields.io/badge/NDDev-1a1a2e?style=for-the-badge" alt="NDDev" />
</a>

*Open to technical advisory, architecture consulting, and strategic partnerships worldwide.*

</div>
