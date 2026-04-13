# Sand Hourglass

A meditative hourglass simulation that responds to device orientation. Tilt your phone to watch the sand flow with realistic particle physics.

## Live Demo

[https://gcicc.github.io/sand-hourglass/](https://gcicc.github.io/sand-hourglass/)

## Features

- **Device Orientation**: Tilt your phone to control gravity. Sand flows naturally in response to device motion (uses deviceorientation API)
- **~2000 Sand Particles**: Realistic physics with gravity, collision detection, and particle stacking
- **Multiple Sand Colors**: Classic Tan, Ocean Blue, Desert Red, Arctic White, Galaxy (purple/blue mix), Rainbow (random hues)
- **Timer Modes**: 1, 3, 5, 10, 15 minutes — sand flow calibrated to timer duration, soft chime when complete
- **Free Mode**: Just watch the sand flow without a timer
- **Flip Button**: Instantly flip the hourglass to reverse gravity (also resets timer in timer mode)
- **Clear Button**: Reset all sand
- **Offline Support**: Full PWA with service worker — works without internet
- **No Gyroscope?** Desktop fallback: Click flip button to reverse gravity direction

## Installation

### On Your Phone

1. Open [https://gcicc.github.io/sand-hourglass/](https://gcicc.github.io/sand-hourglass/) on your phone
2. **iOS**: Tap Share → Add to Home Screen → Add
3. **Android**: Tap Menu (⋮) → Install App (or Add to Home Screen)

### For Development

```bash
cd sand-hourglass
python generate-icons.py      # Regenerate icons if needed
python -m http.server 8000    # Serve locally at http://localhost:8000
```

## How to Play

1. **Tilt your phone** to move the sand in response to gravity
2. **Select a color** from the top bar
3. **Set a timer** (1, 3, 5, 10, or 15 minutes) or leave in Free mode
4. **Flip the button** to reverse — sand flows to the other chamber
5. **Listen for the chime** when the timer completes (if timer mode)

## Technical Details

- **Particles**: ~2000–3000 grains of sand, each with position, velocity, and color
- **Physics**: Simple gravity + velocity damping + elastic collisions + spatial hashing for efficient collision detection
- **Hourglass Shape**: Two triangular chambers connected by a narrow circular neck opening
- **Device Orientation API**: Extracts beta/gamma angles from device tilt, converts to gravity vector
- **Web Audio**: Soft chime tone (528 Hz decay) when timer completes
- **Service Worker**: Cache-first strategy for instant offline replay

## Files

- `index.html` — Complete single-file app (HTML + CSS + Canvas + JS)
- `manifest.json` — PWA metadata, icons, theme colors
- `sw.js` — Service worker for offline support
- `generate-icons.py` — Icon generator (192x192, 512x512 PNG)

## Browser Compatibility

- iOS Safari 15.1+ (requires permission for deviceorientation)
- Android Chrome, Firefox, Edge
- Desktop: Works with fallback (tilt unavailable, use flip button)

## Design System

- **Colors**: Dark theme (#0d1117 bg, #161b22 panels, #c4a882 accent)
- **Fonts**: Cormorant Garamond (display), Inter (body) from Google Fonts
- **UI**: Minimal, touch-friendly buttons with active states
- **Accessibility**: Full keyboard support, high contrast, clear onboarding

## Privacy

- No tracking, no analytics, no data collection
- All processing happens in your browser
- Service worker caches only static assets

## License

MIT — feel free to fork, modify, and deploy.

---

Part of the **MobileTapper** portfolio: PWA prototypes for mobile apps across wellness, physics/games, and eye-candy simulations.
