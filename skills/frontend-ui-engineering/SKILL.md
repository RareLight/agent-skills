---
name: frontend-ui-engineering
description: Builds accessible, maintainable user interfaces that follow the active product and codebase conventions. Use when modifying user-facing browser or native UI.
applies_when: The request changes layout, interaction, presentation state, or accessibility.
skip_when: No user-facing interface changes.
risk: medium
requires: [ui-runtime-optional]
fallback: Use component tests, static review, and documented visual/runtime gaps.
outputs: [ui-change, accessibility-evidence]
related_skills: []
---

# Frontend UI Engineering

1. Follow the existing design system and component conventions; establish a minimal local convention only when none exists.
2. Keep presentation, data access, and state ownership appropriately separated; choose the smallest state scope that supports the behavior.
3. Cover loading, error, and empty states when the changed flow can encounter them; do not invent decorative requirements.
4. Use semantic controls, keyboard behavior, accessible names, focus management, and contrast appropriate to the interface. Modals must contain focus; views must not create unintended focus traps.
5. Verify relevant viewport and assistive-technology behavior with available tools.

## Verification checklist

- [ ] The UI follows existing visual and interaction conventions.
- [ ] Changed controls are operable and named appropriately.
- [ ] Relevant states and responsive behavior have evidence or a reported gap.
