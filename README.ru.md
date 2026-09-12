# Данил Силантьев

**AI Staff Engineer · Архитектор систем и AI**  
OSS-разработчик и контрибьютор. CEO [NDDev](https://nddev.it.com).

Создаю AI-системы, агентные процессы и инструменты разработки, от архитектуры до реализации.

[Email](mailto:danil@nddev.it.com) · [Telegram](https://t.me/Danil_Silantyev) · [LinkedIn](https://www.linkedin.com/in/danil-silantyev-ai/) · [English](README.md)

## С чем работаю

### Языки

**Rust · Python · Go · C / C++ · TypeScript · Dart (Flutter)**  
Также JavaScript, SQL и shell-скрипты.

### Семь кодинг-харнессов

**Claude Code · Codex · Grok Build · Pi · OpenCode · Cursor · Antigravity**

Работаю с окружением модели: инструкциями, skills, MCP-серверами,
LSP-интеграцией, hooks, commands, subagents и plugins. Для каждого харнесса
использую его нативную конфигурацию, а не копию настроек другого инструмента.

### Инструменты агентов

| Область | Чем пользуюсь |
| --- | --- |
| Маршрутизация API | [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI), LiteLLM, OpenRouter |
| Дизайн и ревью кода | [Impeccable](https://github.com/pbakaus/impeccable), [Ponytail](https://github.com/DietrichGebert/ponytail), собственные skills и rules |
| Контекст и работа с кодом | `ctx`, Serena, Context7, DeepWiki, grep.app, LSP |
| MCP-интеграции | GitHub, Figma, shadcn, Dart/Flutter, Chrome DevTools, sequential-thinking, OpenAI Docs |
| Работа с браузером | Playwright CLI, Chrome DevTools MCP |

### Прикладной стек

| Область | Основные технологии |
| --- | --- |
| AI и ML | LangGraph, LangChain, PyTorch, scikit-learn, Hugging Face, OpenCV |
| Инференс и RAG | vLLM, ONNX, Qdrant, гибридный поиск, reranking |
| Бэкенд и интерфейсы | FastAPI, React, Next.js, Node.js, Flutter |
| Данные и хранение | PostgreSQL, ClickHouse, Redis, Meilisearch, RustFS |
| Разработка и наблюдаемость | Linux, macOS, Docker, GitHub Actions, OpenTelemetry, Prometheus, Grafana |
| Эксперименты и оценка | MLflow, Weights & Biases, Optuna, Langfuse, LangSmith |

Занимаюсь мультиагентной оркестрацией, RAG, компьютерным зрением и MLOps.
Применяю явные границы сервисов, разделение OLTP/OLAP и transactional outbox
там, где это нужно задаче.

## Избранные open-source проекты

<a href="https://github.com/NDDev-OpenNetwork/github-device-sync">
<picture>
  <source media="(max-width: 640px) and (prefers-color-scheme: dark)" srcset="assets/profile/gds-dark-mobile.svg">
  <source media="(max-width: 640px)" srcset="assets/profile/gds-light-mobile.svg">
  <source media="(prefers-reduced-motion: no-preference) and (prefers-color-scheme: dark)" srcset="assets/profile/gds-dark-motion.svg">
  <source media="(prefers-reduced-motion: no-preference)" srcset="assets/profile/gds-light-motion.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile/gds-dark.svg">
  <img src="assets/profile/gds-light.svg" width="960" alt="GDS: исходные данные, компилятор политик и контекста, неизменяемый пакет, локальные проекции репозиториев. Идентичность отделена от расположения рабочей копии.">
</picture>
</a>

**[GDS](https://github.com/NDDev-OpenNetwork/github-device-sync)** · Управление репозиториями  
Создаю инструменты, которые сохраняют согласованность идентичности репозиториев, политик и контекста агентов на разных устройствах. Путь к рабочей копии обозначает её расположение, а не идентичность.

<a href="https://github.com/ai-engineers-guild/ai-stp">
<picture>
  <source media="(max-width: 640px) and (prefers-color-scheme: dark)" srcset="assets/profile/ai-stp-dark-mobile.svg">
  <source media="(max-width: 640px)" srcset="assets/profile/ai-stp-light-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile/ai-stp-dark.svg">
  <img src="assets/profile/ai-stp-light.svg" width="960" alt="ai-stp: CLI собирает пакет, провайдер записывает нативную конфигурацию инструмента. Проект AI Engineers Guild.">
</picture>
</a>

**[ai-stp](https://github.com/ai-engineers-guild/ai-stp)** · AI Engineers Guild  
Занимаюсь архитектурой, CLI и интеграциями. CLI собирает версионированные сетапы, а провайдеры записывают конфигурацию инструментов.

<a href="https://github.com/NDDev-OpenNetwork/codex-setup-system">
<picture>
  <source media="(max-width: 640px) and (prefers-color-scheme: dark)" srcset="assets/profile/setup-dark-mobile.svg">
  <source media="(max-width: 640px)" srcset="assets/profile/setup-light-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile/setup-dark.svg">
  <img src="assets/profile/setup-light.svg" width="960" alt="Setup systems: резервная копия до изменения, применение и проверка. Восстановление возвращает сохранённое состояние в целевую директорию.">
</picture>
</a>

**[Setup systems](https://github.com/NDDev-OpenNetwork/codex-setup-system)** · NDDev OpenNetwork  
Инструменты настройки семи перечисленных харнессов: явные целевые директории, резервные копии и восстановление. Начать можно с реализации для Codex.

## В NDDev

Руковожу NDDev и сам работаю над архитектурой и кодом.

<a href="https://nddev.it.com">
<picture>
  <source media="(max-width: 640px) and (prefers-color-scheme: dark)" srcset="assets/profile/nddev-dark-mobile.svg">
  <source media="(max-width: 640px)" srcset="assets/profile/nddev-light-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile/nddev-dark.svg">
  <img src="assets/profile/nddev-light.svg" width="960" alt="Шесть направлений NDDev: Dev, AI, Design, R&amp;D, Platform и OpenNetwork.">
</picture>
</a>

Dev · AI · Design · R&D · Platform · OpenNetwork

## Клиентские проекты

Таможня Алматы · Библиотеки Алматы

## Связаться

Есть проект или инженерная роль для обсуждения? [Напишите на почту](mailto:danil@nddev.it.com) или [в Telegram](https://t.me/Danil_Silantyev).

Пользуетесь одним из инструментов? Поставьте звезду его репозиторию или расскажите в issue, чего вам не хватает.
