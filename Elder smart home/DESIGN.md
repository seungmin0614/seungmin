---
name: Lumina Ambient
colors:
  surface: '#17130c'
  surface-dim: '#17130c'
  surface-bright: '#3e3830'
  surface-container-lowest: '#120e07'
  surface-container-low: '#201b13'
  surface-container: '#241f17'
  surface-container-high: '#2f2921'
  surface-container-highest: '#3a342c'
  on-surface: '#ece1d5'
  on-surface-variant: '#d3c5b0'
  inverse-surface: '#ece1d5'
  inverse-on-surface: '#353027'
  outline: '#9b8f7d'
  outline-variant: '#4f4536'
  surface-tint: '#f3be55'
  primary: '#ffd076'
  on-primary: '#412d00'
  primary-container: '#e6b34b'
  on-primary-container: '#624600'
  inverse-primary: '#7b5800'
  secondary: '#cdc5bf'
  on-secondary: '#34302b'
  secondary-container: '#4b4641'
  on-secondary-container: '#bbb4ae'
  tertiary: '#dbd5d2'
  on-tertiary: '#32302e'
  tertiary-container: '#bfbab6'
  on-tertiary-container: '#4d4a47'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdea5'
  primary-fixed-dim: '#f3be55'
  on-primary-fixed: '#261900'
  on-primary-fixed-variant: '#5d4200'
  secondary-fixed: '#eae1db'
  secondary-fixed-dim: '#cdc5bf'
  on-secondary-fixed: '#1f1b17'
  on-secondary-fixed-variant: '#4b4641'
  tertiary-fixed: '#e7e1de'
  tertiary-fixed-dim: '#cbc5c2'
  on-tertiary-fixed: '#1d1b19'
  on-tertiary-fixed-variant: '#494644'
  background: '#17130c'
  on-background: '#ece1d5'
  surface-variant: '#3a342c'
typography:
  headline-xl:
    fontFamily: Geist
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.2'
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-padding-mobile: 24px
  container-padding-desktop: 48px
  gutter: 16px
  card-gap: 12px
---

## Brand & Style

This design system is built for the modern smart home experience, focusing on an atmosphere of calm, control, and premium comfort. The brand personality is sophisticated and "hushed"—it values the space between elements as much as the elements themselves.

The visual direction follows a **refined Glassmorphism** approach. It utilizes deep, atmospheric layering where UI components appear as frosted glass panes floating over a moody, tonal background. The emotional response is one of "luxury utility"—the interface should feel like a high-end physical remote made of light and glass. 

Key stylistic pillars include:
- **Depth through Translucency:** Using backdrop blurs and subtle white inner-glows to define surface edges.
- **Warmth through Light:** High-contrast amber and gold glows represent active energy and human presence.
- **Minimalist Friction:** Reducing visual noise by using thin-line iconography and avoiding heavy borders in favor of tonal separation.

## Colors

The palette is rooted in a dark, warm-neutral foundation to minimize light pollution in a home environment at night. 

- **Primary (Amber Glow):** Used exclusively for active states, toggles, and highlights. It mimics the warmth of a filament bulb.
- **Secondary (Charcoal Brown):** The base for high-level surfaces and glass containers.
- **Tertiary (Obsidian):** The deep background color, providing the "dark room" canvas.
- **Neutral (Warm Grey):** Used for secondary text and inactive icons, ensuring they recede into the background without disappearing.

**Gradients & Overlays:**
Backgrounds should use a radial gradient moving from `#2C2824` at the center-top to `#0F0E0D` at the edges to create a sense of environmental lighting.

## Typography

This design system uses **Geist** for its technical precision and clean, architectural lines. The type scale is designed to be highly legible against translucent backgrounds.

- **Headlines:** Use tight letter-spacing and low line-heights to create a "display" feel that looks impactful even at medium weights.
- **Body Text:** Maintains a generous line-height to ensure readability when placed over blurred photographic backgrounds.
- **Labels:** Small, all-caps labels are used for metadata like device status or room names to create a clear information hierarchy without requiring large font sizes.

## Layout & Spacing

The layout follows a **fluid grid** model with a mobile-first focus. 

- **Mobile (Default):** A single-column layout for main navigation, switching to a 2-column masonry or grid view for device tiles. Use 24px side margins to provide breathing room for the glass edges.
- **Desktop:** A 12-column grid. Sidebars and control panels are treated as persistent glass panes anchored to the edges, with a central fluid area for room visualization or data.
- **Rhythm:** Spacing follows an 8px incremental scale. Use 12px for internal card padding and 24px for section spacing to maintain a relaxed, premium density.

## Elevation & Depth

Depth is established through **Backdrop Blur** rather than traditional drop shadows.

1.  **Level 0 (Base):** The dark obsidian background.
2.  **Level 1 (Cards/Tiles):** 15% opacity white fill with a `20px` backdrop blur. A `1px` inner-stroke at 20% white opacity creates a crisp "glass edge" highlight.
3.  **Level 2 (Modals/Overlays):** 25% opacity secondary color fill with a `40px` backdrop blur. These should cast an ambient, low-opacity shadow (`rgba(0,0,0,0.4)`) to separate them from Level 1.
4.  **Active States:** These elements do not "lift" higher; instead, they emit a soft outer glow in the primary amber color (`box-shadow: 0 0 20px rgba(230, 179, 75, 0.3)`).

## Shapes

The design system uses a generous roundedness scale to evoke comfort and friendliness.

- **Standard Containers:** Use `1rem` (16px) for device tiles and smaller cards.
- **Main Action Cards:** Use `1.5rem` (24px) for high-level dashboard containers to create a distinct visual hierarchy.
- **Interactive Elements:** Buttons and pill-toggles use a fully rounded (pill) style to distinguish them from structural containers.

## Components

### Buttons
- **Primary:** Full amber fill with dark charcoal text. No border. High-impact.
- **Ghost:** Transparent background with a `1px` white (20% opacity) border. White text.
- **Icon Buttons:** Circular glass panes with centered minimalist line icons.

### Device Tiles (Cards)
- Rectangular glass containers with a 1:1 or 4:3 aspect ratio.
- Top-left: Icon and Name.
- Bottom-left: Status (e.g., "72°" or "On").
- Active State: Background opacity increases to 30%, and icons transition to the primary amber color.

### Control Sliders
- Track: A thin, dark semi-transparent line.
- Thumb: A large, circular glass handle with a `2px` amber border.
- Progress: The "filled" part of the track should glow in the primary amber color.

### Chips (Room Selectors)
- Inactive: No background, neutral text.
- Active: White pill-shaped background with dark text, or a glass pill with a subtle inner glow.

### Input Fields
- Underlined style or subtle glass containers. Focus state is indicated by the underline or border transitioning to the primary amber color.