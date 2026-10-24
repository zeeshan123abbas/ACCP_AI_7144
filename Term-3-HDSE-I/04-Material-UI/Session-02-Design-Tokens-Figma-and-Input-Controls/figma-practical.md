# Figma Practical: Design a Login Screen with Material 3

Time: about 60 minutes. You need a free Figma account (https://www.figma.com).

## Part A: Setup (10 min)
1. Create a new **Design file** and name it `Login - Material 3`.
2. Open the **Assets** panel → **UI kits** and choose **Material 3 Design Kit** (built into Figma). If it is missing, open the kit from the Figma Community page and click **Open in Figma**.
3. Press **F** (Frame tool) and choose **Android Compact** (or 360 × 800).

## Part B: Layout with Auto Layout (15 min)
1. Draw a frame inside the screen for the form; press **Shift + A** to add **Auto layout**.
2. Set direction **vertical**, gap **16**, padding **24** (8 dp grid).
3. Add a **Headline Small** text: "Welcome back".

## Part C: Use components (20 min)
1. From the kit's Assets panel, drag in two **Outlined text fields**: Email and Password.
2. Drag a **Filled button**: "Sign in"; set it to **Fill container** width.
3. Add a **Text button**: "Forgot password?".
4. Select a component and use the right panel to switch **variants** (e.g. state = Focused, Error).

## Part D: Apply tokens / styles (10 min)
1. Open **Material Theme Builder** (https://material-foundation.github.io/material-theme-builder/).
2. Pick a source colour (e.g. your college colour) and export, or use the Figma plugin to apply the theme.
3. Check that the button now uses your **primary** colour and the background uses **surface**.

## Part E: Prototype (5 min)
1. Duplicate the frame and create a "Home" screen.
2. Select the Sign in button → **Prototype** tab → drag a connection to the Home frame (On tap → Navigate to, Smart animate).
3. Press **Present** (▶) to test.

## Checklist before submitting
- [ ] All spacing is a multiple of 8
- [ ] Only kit components and styles used (no random colours)
- [ ] Error state of the email field designed
- [ ] Share link set to "Anyone with the link can view"
