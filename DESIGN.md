---
name: Clear Vision Dashboard
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#434653'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#747685'
  outline-variant: '#c4c5d6'
  surface-tint: '#2a55c9'
  primary: '#002a81'
  on-primary: '#ffffff'
  primary-container: '#003eb3'
  on-primary-container: '#a2b6ff'
  inverse-primary: '#b5c4ff'
  secondary: '#0057c0'
  on-secondary: '#ffffff'
  secondary-container: '#006ff0'
  on-secondary-container: '#fefcff'
  tertiary: '#512800'
  on-tertiary: '#ffffff'
  tertiary-container: '#723b00'
  on-tertiary-container: '#ffa454'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b5c4ff'
  on-primary-fixed: '#00164e'
  on-primary-fixed-variant: '#003cad'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#aec6ff'
  on-secondary-fixed: '#001a43'
  on-secondary-fixed-variant: '#004397'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
  status-success: '#166534'
  status-error: '#991B1B'
  status-warning: '#854D0E'
  border-high-contrast: '#0F172A'
  card-bg: '#FFFFFF'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.5'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.04em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  touch-target-min: 4rem
  gutter: 1.5rem
  margin-mobile: 1rem
  margin-desktop: 2.5rem
  stack-gap: 2rem
---

## Brand & Style

The design system is engineered for the "Clear Vision" narrative—a high-accessibility smart home environment tailored for elderly users. The brand personality is **protective, ultra-legible, and dependable**, prioritizing cognitive ease over decorative complexity. 

The aesthetic deviates from the original neomorphic requirements to adopt a **High-Contrast Bento Box** style. This approach uses large, distinct card containers with thick strokes and generous inner padding. Every element is sized for declining motor skills and visual acuity, ensuring "fat-finger" friendly touch targets and maximum color separation. The emotional response should be one of confidence and safety, removing the anxiety often associated with modern technology.

**Key Principles:**
- **Information Primacy:** Only the most essential data is shown at a large scale.
- **Visual Affirmation:** Every interaction provides a significant visual state change.
- **Physicality:** Large cards feel like physical switches or panels.

## Colors

The palette is anchored by **Deep Blue (#003EB3)** to ensure AAA accessibility ratings against white backgrounds. This primary blue provides a calm, "institutional" sense of reliability. 

- **Primary:** Used for main actions and active states.
- **Secondary:** Used for secondary interactive elements like toggle switches or navigation.
- **Tertiary:** Reserved for "Attention" items like the doorbell melody or emergency indicators.
- **Neutral:** A very light grey background (#F8FAFC) to reduce screen glare while maintaining high contrast with the white cards and dark text.
- **High Contrast:** All text and borders utilize a near-black Navy (#0F172A) to ensure edges are sharp and legible even for users with cataracts or low vision.

## Typography

Typography centers on **Plus Jakarta Sans** for its open apertures and modern, friendly geometric shapes that remain legible at large scales.

- **Scale:** Sizes are significantly larger than standard web patterns. The base body size starts at 20px.
- **Numbers:** Sensor data (Temperature, Humidity, Light) uses **JetBrains Mono** to ensure numerical clarity and distinct digit shapes, preventing confusion between '0' and 'O' or '1' and 'l'.
- **Weights:** Medium and Bold weights are preferred over light weights to maintain stroke thickness for better visibility.
- **Mobile:** Headlines scale down slightly but remain the dominant visual element to maintain the hierarchy.

## Layout & Spacing

The layout follows a **Fixed Bento Grid** model. On mobile, it collapses into a single column of full-width cards. On larger screens, it uses a 4-column layout where primary sensors span 2 columns and small controls span 1.

- **Rhythm:** A strict 8px-based spacing system is used. 
- **Touch Safety:** Every interactive element has a minimum touch target of 64px (4rem) to accommodate reduced manual dexterity.
- **Bento Logic:** Cards are used to group related functions (e.g., "Environment Card" contains Temp + Humidity). Margins between cards are kept wide (24px) to prevent visual crowding.

## Elevation & Depth

This design system avoids complex shadows to prevent visual "muddiness." Instead, it uses **Tonal Layers and High-Contrast Outlines**:

- **Borders:** All cards and buttons use a 2px solid border (#0F172A). This creates a "comic" or "blueprint" clarity that defines where one control ends and another begins.
- **Active State:** When a button is pressed, it shifts from a 4px bottom-offset "lifted" look to a flat look, simulating a physical mechanical click.
- **Layering:** The background is #F8FAFC, and cards are pure #FFFFFF. The contrast between the two is reinforced by the heavy border rather than a shadow.

## Shapes

The shape language uses **Rounded (0.5rem)** corners. This provides a soft, approachable feel while remaining structured enough for the high-contrast grid. 

Large-scale containers (cards) use `rounded-xl` (1.5rem) to emphasize the "Bento" container metaphor. Buttons within those containers use the standard 0.5rem to create a clear nested hierarchy. Icons should be contained within circular or rounded-square enclosures to serve as large, identifiable touch zones.

## Components

### Buttons
Buttons are oversized with 2px borders. Primary buttons use the Primary Blue with white text. "Off" states use a white background with a heavy grey border to indicate inactivity.

### Sensor Cards
Cards display data in the `data-display` type style. They include a large icon (48px+) in the top left and the sensor name in `label-caps`. A "Refresh" icon must be at least 48x48px in the top right.

### Control Chips
For toggles like "Light On/Off," use a split-segment control. The active segment is filled with Primary Blue, and the inactive is white. This "physical switch" metaphor is easier to understand than a small sliding toggle.

### Status Indicators
Located in the header. Use a large (16px) colored dot accompanied by a text label ("CONNECTED" / "DISCONNECTED"). Do not rely on color alone; always provide text for accessibility.

### Input Fields / Terminal
The communication log uses a high-contrast dark background (#0F172A) with neon-green or white monospaced text to differentiate "system data" from "user interface."

### Navigation
The bottom tab bar uses large, labeled icons. Each tab is a dedicated block that fills 25% of the screen width, ensuring easy thumb access.