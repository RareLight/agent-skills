---
name: frontend-ui-engineering
description: Builds production-quality UIs. Use when building or modifying user-facing interfaces. Use when creating components, implementing layouts, managing state, or when the output needs to look and feel production-quality rather than AI-generated.
---

# Frontend UI Engineering

## Architectural Rules
- **Colocate Assets**: Keep markup, styling, tests, and component logic grouped together in dedicated folders.
- **Separation of Concerns**: Isolate API/data-fetching from presentation components. Keep presentation pure and deterministic.
- **State Selection**: Choose the simplest state scope: local DOM/state first → URL params for shareable state → shared global store/events only when necessary. Avoid tight coupling between sibling elements.

## Design Integrity (Anti-AI Aesthetic)
- **Contrast & Radii**: Follow the design system spacing grid, typographic hierarchy, and color tokens. Never use arbitrary pixels or raw hex values. Ensure strict AA color contrast (≥4.5:1).
- **Copy & Spacing**: Avoid generic layouts, extreme gradients, indigo-everything palettes, and oversized/uneven margins. Always test layouts with realistic content (wrapping, overflow, varying lengths).
- **Responsive-First**: Design mobile-first using responsive grids (Flexbox/Grid with breakpoints). Test at 320px, 768px, 1024px, and 1440px.
- **States**: Build native error boundary handlers, skeleton loading animations (not just spinners), and meaningful empty-state illustrations with actionable buttons.

## Accessibility Standards (WCAG 2.1 AA)
- **Keyboard Access**: Ensure all interactive components are focusable and operable via Keyboard (`Tab`, `Shift+Tab`, `Enter`, `Space`, `ESC`). Trap focus within modals.
- **Aria Attributes**: Include meaningful labels (`aria-label` / `htmlFor` / `aria-labelledby`) on all interactive or image elements lacking visible text.
- **Dynamic Announcements**: Use `aria-live="polite"` or `role="status"` to announce dynamic page modifications.
- **Verification Layers**:
  1. *Automated*: Run Lighthouse Accessibility (target ≥90) and `axe` checks.
  2. *Keyboard Audit*: Test the page entirely with the keyboard.
  3. *Screen Reader*: Verify navigation layout and dynamic changes with a screen reader.

## Verification Checklist
- [ ] Component renders clean with zero browser console errors or accessibility violations.
- [ ] Keyboard navigation is completely functional (no focus traps).
- [ ] View is responsive across all major viewports (320px to 1440px).
- [ ] Loading, error, and empty states are built and polished.
- [ ] Visual styling perfectly matches the design system token guidelines.
