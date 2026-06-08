---
name: Invoice Intelligence
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#4b41e1'
  on-secondary: '#ffffff'
  secondary-container: '#645efb'
  on-secondary-container: '#fffbff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#00201d'
  on-tertiary-container: '#0c9488'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#e2dfff'
  secondary-fixed-dim: '#c3c0ff'
  on-secondary-fixed: '#0f0069'
  on-secondary-fixed-variant: '#3323cc'
  tertiary-fixed: '#89f5e7'
  tertiary-fixed-dim: '#6bd8cb'
  on-tertiary-fixed: '#00201d'
  on-tertiary-fixed-variant: '#005049'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 24px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

The brand personality is **Trustworthy, Intelligent, and Cutting-Edge**. As a financial SaaS platform, the design system must convey the stability of a traditional bank while projecting the efficiency of modern AI. The UI facilitates "Invoice Intelligence" by making complex data feel manageable and insights feel intuitive.

The chosen style is **Modern Corporate Minimalism**. It prioritizes high-density data visualization through a clean, systematic interface. We employ subtle glassmorphism for overlays and tonal layering to separate "system" actions from "intelligence" insights. The aesthetic is professional and grounded, using whitespace not just for breathing room, but as a functional separator between distinct financial data sets.

## Colors

This design system utilizes a sophisticated, high-contrast palette designed for long-term legibility and trust.

*   **Primary (Deep Navy/Slate):** Used for core navigation, headings, and high-level structural elements to establish authority.
*   **Secondary (Vibrant Indigo):** Represents the "Intelligence" layer. Used for AI-driven insights, primary actions, and active states.
*   **Tertiary (Teal):** Used for financial health indicators, positive growth, and "success" states related to processing.
*   **Neutrals:** A scale of cool grays (Slate) to provide soft contrast for borders, secondary text, and background surfaces.
*   **Semantic Colors:**
    *   **Success:** Teal-600
    *   **Warning:** Amber-500 (for pending approvals or late invoices)
    *   **Error:** Rose-600 (for failed payments or data errors)

## Typography

The typography system is built on **Inter** for its exceptional legibility in data-heavy environments and its neutral, professional character. We introduce **JetBrains Mono** for specific labels, monetary values, and ID numbers to evoke a sense of precision and technical accuracy.

**Scaling & Hierarchy:**
- Large display styles are reserved for dashboard summaries and empty state headers.
- Body-sm is the workhorse for data table cells and form labels to maximize information density.
- All monetary figures and invoice IDs should utilize the `label` styles to ensure characters like '0' and 'O' or '1' and 'I' are easily distinguishable.

## Layout & Spacing

The design system uses a **Fixed Grid** approach for the main content area to ensure financial reports remain readable and structured, while the sidebar navigation remains fluid.

*   **Desktop:** 12-column grid, 24px gutters, 32px side margins. Max container width of 1440px.
*   **Tablet:** 8-column grid, 16px gutters, 24px side margins.
*   **Mobile:** 4-column grid, 16px gutters, 16px side margins.

We utilize a **4px base unit** for all spacing. Component internal padding should strictly follow the `sm` (8px) or `md` (16px) tokens to maintain a tight, professional density. Section headers should be separated from content by `lg` (24px) spacing.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Ambient Shadows**.

1.  **Background (Level 0):** Slate-50 (#F8FAFC). The lowest layer.
2.  **Surface (Level 1):** White (#FFFFFF). Used for cards, table containers, and the main content area. Includes a subtle 1px border (Slate-200) for definition.
3.  **Raised (Level 2):** Applied to active cards or hovered elements. Uses an ambient shadow: `0px 4px 12px rgba(15, 23, 42, 0.08)`.
4.  **Overlay (Level 3):** Modals and dropdowns. Uses a more pronounced shadow: `0px 12px 32px rgba(15, 23, 42, 0.12)`.

We use a "Glass" effect for floating AI notifications or "Processing" banners, utilizing a backdrop blur of 8px and a 70% opacity white fill to differentiate intelligence-layer communications from standard system data.

## Shapes

The shape language is **Rounded**, utilizing an 8px base radius for primary components. This softens the "industrial" feel of financial data without appearing too casual or consumer-oriented.

*   **Default (rounded-md):** 8px (0.5rem). Used for buttons, input fields, and standard cards.
*   **Large (rounded-lg):** 16px (1rem). Used for main dashboard containers or promotional "Intelligence" banners.
*   **Full (rounded-full):** Used exclusively for status badges (chips) and avatars.

## Components

**Buttons**
- **Primary:** Indigo background, white text. Bold, 8px corners.
- **Secondary:** Slate-100 background, Slate-900 text.
- **Ghost:** No background, Slate-600 text. Used for less frequent actions like "Cancel" or "Export."

**Data Tables**
- Header rows use `label-sm` in Slate-500 with a subtle bottom border.
- Row heights are fixed at 56px to ensure consistency.
- Hover states use a Slate-50 background tint.

**Metrics Cards**
- Large `label-md` for the title, `headline-md` for the value.
- Include a small sparkline or percentage change indicator in the bottom right corner using Teal (up) or Rose (down).

**Progress Indicators (AI Processing)**
- Use a shimmering gradient animation (Indigo to Teal) for progress bars to indicate "Intelligence" at work.
- Accompany with `label-sm` status text (e.g., "Analyzing tax compliance...").

**Input Fields**
- 1px border (Slate-300).
- Focused state: 2px border (Indigo-500) with a 4px Indigo-50 soft outer glow.
- Labels use `body-sm` (Medium weight).

**Chips/Badges**
- Used for invoice status: "Paid" (Teal), "Pending" (Amber), "Overdue" (Rose). 
- Use a "Soft" style: 10% opacity background of the color with 100% opacity text.