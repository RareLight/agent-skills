# Testing Patterns Reference

Quick reference for common testing patterns across the stack. Use alongside the `test-driven-development` skill.

## Table of Contents

- [Test Structure (Arrange-Act-Assert)](#test-structure-arrange-act-assert)
- [Test Naming Conventions](#test-naming-conventions)
- [Common Assertions](#common-assertions)
- [Mocking Patterns](#mocking-patterns)
- [React/Component Testing](#reactcomponent-testing)
- [API / Integration Testing](#api--integration-testing)
- [E2E Testing (Playwright)](#e2e-testing-playwright)
- [Test Anti-Patterns](#test-anti-patterns)

## Test Structure (Arrange-Act-Assert)

```typescript
it('describes expected behavior', () => {
  // Arrange: Set up test data and preconditions
  const input = { title: 'Test Task', priority: 'high' };

  // Act: Perform the action being tested
  const result = createTask(input);

  // Assert: Verify the outcome
  expect(result.title).toBe('Test Task');
  expect(result.priority).toBe('high');
  expect(result.status).toBe('pending');
});
```

## Test Naming Conventions

```typescript
// Pattern: [unit] [expected behavior] [condition]
describe('TaskService.createTask', () => {
  it('creates a task with default pending status', () => {});
  it('throws ValidationError when title is empty', () => {});
  it('trims whitespace from title', () => {});
  it('generates a unique ID for each task', () => {});
});
```

## Common Assertions

```typescript
// Equality
expect(result).toBe(expected);           // Strict equality (===)
expect(result).toEqual(expected);        // Deep equality (objects/arrays)
expect(result).toStrictEqual(expected);  // Deep equality + type matching

// Truthiness
expect(result).toBeTruthy();
expect(result).toBeFalsy();
expect(result).toBeNull();
expect(result).toBeDefined();
expect(result).toBeUndefined();

// Numbers
expect(result).toBeGreaterThan(5);
expect(result).toBeLessThanOrEqual(10);
expect(result).toBeCloseTo(0.3, 5);      // Floating point

// Strings
expect(result).toMatch(/pattern/);
expect(result).toContain('substring');

// Arrays / Objects
expect(array).toContain(item);
expect(array).toHaveLength(3);
expect(object).toHaveProperty('key', 'value');

// Errors
expect(() => fn()).toThrow();
expect(() => fn()).toThrow(ValidationError);
expect(() => fn()).toThrow('specific message');

// Async
await expect(asyncFn()).resolves.toBe(value);
await expect(asyncFn()).rejects.toThrow(Error);
```

## Mocking Patterns

### Mock Functions

```typescript
const mockFn = jest.fn();
mockFn.mockReturnValue(42);
mockFn.mockResolvedValue({ data: 'test' });
mockFn.mockImplementation((x) => x * 2);

expect(mockFn).toHaveBeenCalled();
expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2');
expect(mockFn).toHaveBeenCalledTimes(3);
```

### Mock Modules

```typescript
// Mock an entire module
jest.mock('./database', () => ({
  query: jest.fn().mockResolvedValue([{ id: 1, title: 'Test' }]),
}));

// Mock specific exports
jest.mock('./utils', () => ({
  ...jest.requireActual('./utils'),
  generateId: jest.fn().mockReturnValue('test-id'),
}));
```

### Mock at Boundaries Only

```
Mock these:                    Don't mock these:
├── Database calls             ├── Internal utility functions
├── HTTP requests              ├── Business logic
├── File system operations     ├── Data transformations
├── External API calls         ├── Validation functions
└── Time/Date (when needed)    └── Pure functions
```

## React/Component Testing

```tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';

describe('TaskForm', () => {
  it('submits the form with entered data', async () => {
    const onSubmit = jest.fn();
    render(<TaskForm onSubmit={onSubmit} />);

    // Find elements by accessible role/label (not test IDs)
    await screen.findByRole('textbox', { name: /title/i });
    fireEvent.change(screen.getByRole('textbox', { name: /title/i }), {
      target: { value: 'New Task' },
    });
    fireEvent.click(screen.getByRole('button', { name: /create/i }));

    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith({ title: 'New Task' });
    });
  });

  it('shows validation error for empty title', async () => {
    render(<TaskForm onSubmit={jest.fn()} />);

    fireEvent.click(screen.getByRole('button', { name: /create/i }));

    expect(await screen.findByText(/title is required/i)).toBeInTheDocument();
  });
});
```

## API / Integration Testing

```typescript
import request from 'supertest';
import { app } from '../src/app';

describe('POST /api/tasks', () => {
  it('creates a task and returns 201', async () => {
    const response = await request(app)
      .post('/api/tasks')
      .send({ title: 'Test Task' })
      .set('Authorization', `Bearer ${testToken}`)
      .expect(201);

    expect(response.body).toMatchObject({
      id: expect.any(String),
      title: 'Test Task',
      status: 'pending',
    });
  });

  it('returns 422 for invalid input', async () => {
    const response = await request(app)
      .post('/api/tasks')
      .send({ title: '' })
      .set('Authorization', `Bearer ${testToken}`)
      .expect(422);

    expect(response.body.error.code).toBe('VALIDATION_ERROR');
  });

  it('returns 401 without authentication', async () => {
    await request(app)
      .post('/api/tasks')
      .send({ title: 'Test' })
      .expect(401);
  });
});
```

## E2E Testing (Playwright)

```typescript
import { test, expect } from '@playwright/test';

test('user can create and complete a task', async ({ page }) => {
  // Navigate and authenticate
  await page.goto('/');
  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="password"]', 'testpass123');
  await page.click('button:has-text("Log in")');

  // Create a task
  await page.click('button:has-text("New Task")');
  await page.fill('[name="title"]', 'Buy groceries');
  await page.click('button:has-text("Create")');

  // Verify task appears
  await expect(page.locator('text=Buy groceries')).toBeVisible();

  // Complete the task
  await page.click('[aria-label="Complete Buy groceries"]');
  await expect(page.locator('text=Buy groceries')).toHaveCSS(
    'text-decoration-line', 'line-through'
  );
});
```

## Test Anti-Patterns

| Anti-Pattern | Problem | Better Approach |
|---|---|---|
| Testing implementation details | Breaks on refactor | Test inputs/outputs |
| Snapshot everything | No one reviews snapshot diffs | Assert specific values |
| Shared mutable state | Tests pollute each other | Setup/teardown per test |
| Testing third-party code | Wastes time, not your bug | Mock the boundary |
| Skipping tests to pass CI | Hides real bugs | Fix or delete the test |
| Using `test.skip` permanently | Dead code | Remove or fix it |
| Overly broad assertions | Doesn't catch regressions | Be specific |
| No async error handling | Swallowed errors, false passes | Always `await` async tests |

## Python Testing Patterns

> See also `~/.config/agent-skills/references/python-patterns.md` for comprehensive Python testing examples (fixtures, parameterization, async mocking, monkeypatch).

### Test Structure (Python)

```python
import pytest

def test_describes_expected_behavior():
    # Arrange
    input_data = {"title": "Test Task", "priority": "high"}

    # Act
    result = create_task(input_data)

    # Assert
    assert result.title == "Test Task"
    assert result.priority == "high"
    assert result.status == "pending"
```

### Common Assertions (Python)

```python
# Equality
assert result == expected_value           # Deep equality (==)
assert result is None                     # Identity (is)

# Truthiness
assert result                             # Truthy
assert not result                         # Falsy

# Numbers
assert result == 42
assert result > 5
assert result <= 10
assert result == pytest.approx(0.3)       # Floating point

# Strings
assert "substring" in result
assert result.startswith("prefix")
assert result.endswith("suffix")

# Collections
assert item in collection
assert item not in collection
assert len(collection) == 3

# Exceptions
with pytest.raises(ValueError):
    create_task(title="")

with pytest.raises(ValueError, match="title must not"):
    create_task(title="")

# Async
async def test_async_result():
    result = await async_function()
    assert result == expected
```

### Mocking (Python)

```python
from unittest.mock import patch, MagicMock, AsyncMock

# At boundaries only (same principle as JS):
# Mock these:                  Don't mock these:
# ├── Database calls           ├── Internal utility functions
# ├── HTTP requests            ├── Business logic
# ├── File system operations   ├── Data transformations
# ├── External API calls       ├── Validation functions
# └── Time/Date (when needed)  └── Pure functions

# Context-manager patching (preferred)
def test_fetch_user():
    with patch("myapp.api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"name": "Alice"}
        result = fetch_user(user_id=1)
        mock_get.assert_called_once_with("https://api.example.com/users/1")
        assert result.name == "Alice"

# mocker fixture (pytest-mock plugin)
def test_with_mocker(mocker):
    mock_query = mocker.patch("myapp.db.session.query")
    mock_query.return_value.all.return_value = [user1, user2]
    results = list_active_users()
    assert len(results) == 2
    mock_query.assert_called_once()
```

### Parametrized Tests (Python)

```python
@pytest.mark.parametrize("title,priority,expected_status", [
    ("Task 1", "high", "pending"),
    ("Task 2", "low", "pending"),
    ("", "high", None),           # Empty title raises ValueError
    ("x" * 201, "low", None),    # Too long raises ValueError
])
def test_create_task(title, priority, expected_status):
    if expected_status is None:
        with pytest.raises(ValueError):
            create_task(title=title, priority=priority)
    else:
        result = create_task(title=title, priority=priority)
        assert result.status == expected_status
```

### Integration Testing (Python)

```python
# FastAPI / Starlette
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_task_returns_201():
    response = client.post(
        "/api/tasks",
        json={"title": "Test Task"},
        headers={"Authorization": f"Bearer {test_token}"},
    )
    assert response.status_code == 201
    assert response.json()["status"] == "pending"

def test_missing_title_returns_422():
    response = client.post("/api/tasks", json={"title": ""})
    assert response.status_code == 422

# Django
from django.test import TestCase

class TaskAPITests(TestCase):
    def test_create_task(self):
        response = self.client.post(
            "/api/tasks/",
            {"title": "Test Task"},
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.token}",
        )
        self.assertEqual(response.status_code, 201)
```

### E2E Testing (Python)

```python
# Playwright works identically with Python bindings
from playwright.sync_api import sync_playwright, expect

def test_user_can_create_task():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")
        page.fill('[name="title"]', "Buy groceries")
        page.click('button:has-text("Create")')
        expect(page.locator("text=Buy groceries")).to_be_visible()
        browser.close()
```
