# Python Patterns Reference

Quick reference for Python-specific patterns across the stack. Use alongside language-agnostic skill workflows to apply correct idioms, tooling, and safety practices when working in Python codebases.

## Table of Contents

- [Project Discovery](#project-discovery)
- [Testing](#testing)
- [Type Checking & Schema Validation](#type-checking--schema-validation)
- [Concurrency & Performance](#concurrency--performance)
- [Package & Dependency Management](#package--dependency-management)
- [Security & Language Hazards](#security--language-hazards)
- [Pythonic Idioms](#pythonic-idioms)

## Project Discovery

Before issuing any Python tooling command, discover the project's setup:

```bash
# Which package manager is in use?
ls pyproject.toml poetry.lock Pipfile requirements.txt setup.py setup.cfg 2>/dev/null

# Check project metadata
cat pyproject.toml 2>/dev/null || cat setup.cfg 2>/dev/null || cat setup.py 2>/dev/null

# Discover installed tools
which pytest mypy ruff black uv poetry tox 2>/dev/null
```

**High-level variant selection** — detect one of these layouts and follow its conventions:

```
Python project layouts (in order of preference):
├── pyproject.toml + poetry.lock     → Poetry-managed project
├── pyproject.toml + uv.lock         → uv-managed project
├── pyproject.toml (PEP 621)         → Standards-based, use pip/uv
├── Pipfile + Pipfile.lock           → Pipenv-managed project
├── requirements.txt                 → vanilla pip + venv
├── requirements/*.txt               → split requirements (base, dev, prod)
├── setup.py / setup.cfg              → setuptools (legacy)
└── tox.ini / noxfile.py              → multi-env test runner detected
```

## Testing

### Pytest Basics

```python
# test_module.py
import pytest
from myapp import create_task

def test_create_task_assigns_default_status():
    result = create_task(title="Write docs")
    assert result.title == "Write docs"
    assert result.status == "pending"

def test_create_task_rejects_empty_title():
    with pytest.raises(ValueError, match="title must not be empty"):
        create_task(title="")
```

### Fixtures

```python
import pytest
from myapp import create_user, db

@pytest.fixture
def test_user():
    user = create_user(email="test@example.com")
    yield user
    db.cleanup(user.id)

@pytest.fixture(scope="module")
def db_session():
    session = db.connect()
    yield session
    session.close()

def test_password_hashing(test_user):
    assert test_user.password_hash != "plaintext"
```

### Parameterized Tests

```python
@pytest.mark.parametrize("title,expected_status", [
    ("Normal task", "pending"),
    ("", None),                    # Expects ValueError
    ("x" * 201, None),             # Expects ValueError
])
def test_create_task_variants(title, expected_status):
    if expected_status is None:
        with pytest.raises(ValueError):
            create_task(title=title)
    else:
        result = create_task(title=title)
        assert result.status == expected_status
```

### Mocking with unittest.mock

```python
from unittest.mock import patch, MagicMock, AsyncMock, ANY

# Context-manager patching (preferred)
def test_send_notification():
    with patch("myapp.tasks.EmailService.send") as mock_send:
        mock_send.return_value = {"status": "sent"}
        result = notify_user(user_id=42)
        mock_send.assert_called_once_with(to="user@example.com", body=ANY)

# Decorator-based patching
@patch("myapp.tasks.fetch_weather")
@patch("myapp.tasks.fetch_traffic")
def test_route_planner(mock_traffic, mock_weather):
    # Mocks are injected bottom-up (closest to function first)
    mock_weather.return_value = {"temp": 22}
    mock_traffic.return_value = {"delay_min": 5}
    result = plan_route(home="A", work="B")
    assert result.eta_minutes == 30

# Async mocking
@pytest.mark.asyncio
async def test_async_operation():
    mock_client = AsyncMock()
    mock_client.fetch.return_value = {"data": "result"}
    result = await process_async(mock_client)
    assert result == "result"
    mock_client.fetch.assert_awaited_once()
```

### Pytest-mock (mocker fixture)

```python
def test_with_mocker_fixture(mocker):
    # mocker.patch auto-unpatches after test
    mock_db = mocker.patch("myapp.storage.Database.query")
    mock_db.return_value = [{"id": 1, "name": "Alice"}]
    result = list_users()
    assert len(result) == 1
```

### Monkeypatch (built-in fixture)

```python
def test_with_monkeypatch(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    monkeypatch.setattr("myapp.config.DEBUG", False)
    assert load_config().debug is False
```

## Type Checking & Schema Validation

### Standard Typing

```python
from typing import Optional, Union, Literal, Protocol, TypeGuard, Final
from collections.abc import Callable, Sequence, Mapping

# Discriminated union
from typing import TypedDict

class PendingTask(TypedDict):
    kind: Literal["pending"]
    title: str

class CompletedTask(TypedDict):
    kind: Literal["completed"]
    title: str
    completed_at: str

Task = PendingTask | CompletedTask

def describe(task: Task) -> str:
    if task["kind"] == "pending":
        return f"TODO: {task['title']}"
    else:
        return f"DONE: {task['title']} at {task['completed_at']}"

# TypeGuard (user-defined narrowing)
def is_completed(task: Task) -> TypeGuard[CompletedTask]:
    return task["kind"] == "completed"

# Protocol (structural subtyping)
class HasName(Protocol):
    name: str

def greet(entity: HasName) -> str:
    return f"Hello, {entity.name}"
```

### Static Analysis

```bash
# mypy — static type checker
mypy src/ tests/

# pyright — faster alternative
pyright src/

# ruff — fast linter + formatter
ruff check src/ tests/
ruff format src/ tests/
```

### Pydantic for Runtime Validation

```python
from pydantic import BaseModel, Field, field_validator
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class CreateTaskRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    priority: Priority = Field(default=Priority.MEDIUM)
    due_date: str | None = None

    @field_validator("title")
    @classmethod
    def title_must_not_be_whitespace(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("title must not be empty or whitespace")
        return v.strip()

# Usage in FastAPI/Flask
@app.post("/tasks")
async def create_task(body: CreateTaskRequest):
    task = await task_service.create(body.model_dump())
    return task
```

### Dataclasses

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)
class Task:
    title: str
    priority: Priority = Priority.MEDIUM
    created_at: datetime = field(default_factory=datetime.now)
    status: str = "pending"
```

## Concurrency & Performance

### Selecting a Concurrency Model

```
What kind of work?
├── I/O-bound (network, disk, db queries)
│   ├── Async-capable libraries available? → asyncio
│   └── Synchronous libraries only? → threading (ThreadPoolExecutor)
├── CPU-bound (computation, image processing, ML)
│   ├── Needs shared memory? → threading (limited by GIL) or C extension
│   └── Independent work? → multiprocessing (ProcessPoolExecutor)
└── Mixed
    └── asyncio + loop.run_in_executor() for CPU chunks
```

### Async/Await and Event Loop Safety

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

# DANGER: Sync blocking call inside async handler — blocks the entire event loop
@app.get("/report")
async def generate_report():
    data = slow_sync_db_query()            # BLOCKS ALL OTHER REQUESTS
    return process(data)

# SAFE: Offload blocking calls to a thread pool
executor = ThreadPoolExecutor(max_workers=4)

@app.get("/report")
async def generate_report():
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(executor, slow_sync_db_query)
    return process(data)

# OR use async-compatible libraries
@app.get("/tasks")
async def list_tasks():
    async with async_session() as session:    # Async SQLAlchemy / asyncpg
        result = await session.execute(select(Task))
        return result.scalars().all()
```

### GIL Awareness

- The Global Interpreter Lock (GIL) serializes Python bytecode execution — only one thread runs at a time.
- **I/O-bound code:** Threading works fine — threads release the GIL when waiting on I/O.
- **CPU-bound code:** Threading provides no parallelism — use `multiprocessing` or `ProcessPoolExecutor`.
- **C extensions** (NumPy, Cython) can release the GIL during heavy computation.

```python
# CPU-bound: use ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def cpu_intensive(n: int) -> int:
    return sum(i * i for i in range(n))

with ProcessPoolExecutor() as executor:
    results = list(executor.map(cpu_intensive, [10**6, 10**7, 10**8]))
```

### Profiling

```bash
# cProfile — function-level CPU profiling
python -m cProfile -s cumulative myapp/main.py

# In code
import cProfile
cProfile.run("expensive_function()", sort="cumulative")

# line_profiler — line-by-line timing
pip install line_profiler
@profile
def hot_function():
    ...  # Each line gets individual timing

kernprof -l -v myapp/main.py

# memory_profiler — memory usage over time
pip install memory_profiler
python -m memory_profiler myapp/main.py

# py-spy — sampling profiler for running processes (no instrumentation needed)
py-spy top --pid <PID>
py-spy record -o profile.svg --pid <PID>
```

## Package & Dependency Management

### Tool Selection by Project Layout

| Tool | Lock file | Install command | Audit command | Best for |
|------|-----------|----------------|---------------|----------|
| Poetry | `poetry.lock` | `poetry install` | `poetry check` | Full project management |
| uv | `uv.lock` | `uv sync` | `uv pip compile` | Speed, modern tooling |
| Pipenv | `Pipfile.lock` | `pipenv install` | `pipenv check` | Flask/Django tutorials |
| pip-tools | `requirements/*.txt` | `pip-sync` | — | Minimal, composable |
| pip + venv | `requirements.txt` | `pip install -r requirements.txt` | `pip-audit` | Simple projects |

### Lockfile Management

```bash
# Poetry
poetry lock          # Resolve and lock dependencies
poetry install       # Install from lockfile
poetry add requests  # Add dependency + update lock

# uv
uv lock              # Resolve and lock
uv sync              # Install from lockfile
uv add requests      # Add dependency + update lock

# pip-tools
pip-compile requirements.in -o requirements.txt
pip-sync requirements.txt
```

### Running with Correct Interpreter

```bash
# Always discover before executing
which python python3
python --version

# If Poetry-managed
poetry run pytest
poetry run mypy src/

# If uv-managed
uv run pytest
uv run mypy src/

# If virtualenv
source .venv/bin/activate  # (or .venv/Scripts/activate on Windows)
pytest
```

## Security & Language Hazards

### Unsafe Deserialization

```python
# DANGER: pickle — arbitrary code execution on deserialization
data = pickle.loads(untrusted_input)          # NEVER do this

# DANGER: PyYAML's default loader
data = yaml.load(untrusted_input)             # Executes arbitrary Python

# SAFE: yaml.safe_load
data = yaml.safe_load(untrusted_input)        # Only basic types, no code execution

# SAFE: JSON (but still validate after parsing)
data = json.loads(untrusted_input)
task = CreateTaskRequest.model_validate(data)  # Pydantic validation after parsing
```

### Dynamic Execution Hazards

```python
# DANGER: eval/exec on user input
eval(user_input)          # Arbitrary code execution
exec(user_input)          # Arbitrary code execution
__import__(user_input)    # Arbitrary import

# DANGER: compile() with user input
compile(user_input, "<string>", "exec")

# No safe equivalent exists — never pass untrusted input to these functions.
```

### Subprocess Safety

```python
import subprocess

# DANGER: shell=True with user input — shell injection
subprocess.run(f"git log {user_branch}", shell=True)

# SAFE: List form with no shell
subprocess.run(["git", "log", user_branch])  # user_branch passed as single argument

# DANGER: Untrusted input in command name
subprocess.run([user_provided_command, "--flag"])

# SAFE: Validate against allowlist
ALLOWED_COMMANDS = {"git", "docker", "npm"}
if user_cmd not in ALLOWED_COMMANDS:
    raise ValueError(f"Command not allowed: {user_cmd}")
subprocess.run([user_cmd, "--flag"])
```

### Static Security Analysis

```bash
# bandit — finds common security issues
bandit -r src/

# Safety / pip-audit — check dependencies for known CVEs
pip-audit
# or
safety check

# detect-secrets — prevent credential leaks
detect-secrets scan --all-files
```

### Dependency Auditing

```bash
# pip-audit (preferred — uses PyPA advisory DB)
pip-audit

# safety (commercial alternative)
safety check

# Check in CI: same command
pip-audit || exit 1
```

**Python equivalents for npm audit:**

| npm command | Python equivalent |
|-------------|-------------------|
| `npm audit` | `pip-audit` or `safety check` |
| `npm audit fix` | `pip install --upgrade <package>` (manual, no auto-fix) |
| `npm audit --audit-level=critical` | `pip-audit --strict` (exit 1 on any vuln) |
| `npx npm-check-updates` | `pip list --outdated` or `pur` (pip-upgrade-requirements) |

## Pythonic Idioms

### Decorators

```python
import functools
import time

def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_remote_data(url: str) -> dict:
    ...
```

### Context Managers

```python
from contextlib import contextmanager

@contextmanager
def temporary_env(**overrides):
    import os
    original = {k: os.environ.get(k) for k in overrides}
    os.environ.update(overrides)
    try:
        yield
    finally:
        for k, v in original.items():
            if v is None:
                del os.environ[k]
            else:
                os.environ[k] = v

# Usage
with temporary_env(DATABASE_URL="sqlite:///:memory:", DEBUG="true"):
    app = create_app()
    result = app.test_client().get("/")

# Class-based (for stateful resources)
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False  # Don't suppress exceptions

    async def __aenter__(self):
        self.conn = await async_connect()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
        return False

with DatabaseConnection() as conn:
    conn.query("SELECT 1")
```

### Generators

```python
# Lazy iteration for memory efficiency
def read_large_file(path: str):
    with open(path) as f:
        for line in f:
            if not line.startswith("#"):
                yield line.strip()

# Generator expressions (preferred for simple cases)
squares = (x * x for x in range(10**6))  # Lazy — no memory allocation

# Delegating to sub-generators
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

### Enum Usage

```python
from enum import Enum, StrEnum, auto

class TaskStatus(StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

# StrEnum allows direct string comparison and JSON serialization
assert TaskStatus.PENDING == "pending"
json.dumps({"status": TaskStatus.COMPLETED})  # '{"status": "completed"}'
```

### Dataclass vs Pydantic Decision

```
Need Deserialization / IO Boundary Validation?
├── Yes → Pydantic BaseModel (automatic parsing, validation errors)
└── No  → Is the object a value with behavior?
         ├── Yes → Regular class
         └── No  → Dataclass (especially frozen=True for immutability)
```
