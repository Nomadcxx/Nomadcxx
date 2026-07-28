<p align="center">
  <picture>
    <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Nomadcxx/Nomadcxx/main/assets/banner-mobile.svg">
    <img src="https://raw.githubusercontent.com/Nomadcxx/Nomadcxx/main/assets/banner.svg" width="960" alt="RAMA — terminal-native tooling for the linux desktop">
  </picture>
</p>

Building for the Linux desktop: a greeter worth looking at, terminal animation engines, wallpaper and media tooling, and a bridge that puts Cursor's agent inside OpenCode.

<br>

### opencode-cursor · 630★

**No prompt limits. No broken streams. Full thinking + tool support in OpenCode. Your Cursor subscription, properly integrated.**

cursor-agent is a closed binary that speaks its own stream protocol and owns its own tool loop. This plugin puts it behind a local OpenAI-compatible proxy and translates in both directions, so OpenCode sees an ordinary provider and you get every model your subscription exposes — Composer, Auto, and the frontier models — without a second API bill.

**What it handles**

- **Streaming** — cursor-agent emits raw token deltas followed by full snapshots; the parser reconciles both so answers don't duplicate or truncate mid-thought
- **Tools** — streaming tool-call interception, schema-compatible mapping between the two tool vocabularies, and session resume that survives across turns
- **MCP** — your existing servers work through the built-in `mcptool` bridge, reading the same `opencode.json` OpenCode already uses. No second config to maintain
- **Thinking** — reasoning blocks pass through intact rather than being flattened into the answer

**Install** — Linux, macOS, Windows

```sh
npm install -g @rama_nigg/open-cursor
open-cursor install
cursor-agent login
```

Verify with `opencode models | grep cursor-acp`.

[repo →](https://github.com/Nomadcxx/opencode-cursor) · [issues](https://github.com/Nomadcxx/opencode-cursor/issues) · `@rama_nigg/open-cursor` on npm

---

### sysc-greet · 375★

A graphical console greeter for [greetd](https://git.sr.ht/~kennylevinsen/greetd), written in Go with Bubble Tea. Animated backgrounds, theming that matches the rest of my tooling — Eldritch, RAMA, Dracula — and a session picker that doesn't look like it was drawn in 1998.

Runs on niri by default, with cagebreak and sway variants. Installs with one line on Arch, Debian/Ubuntu, Fedora and openSUSE; four AUR packages and a NixOS flake are maintained alongside.

```sh
curl -fsSL https://raw.githubusercontent.com/Nomadcxx/sysc-greet/master/install.sh | sudo bash
```

[repo →](https://github.com/Nomadcxx/sysc-greet) · [docs](https://nomadcxx.github.io/sysc-greet/)

<br>

<img src="https://raw.githubusercontent.com/Nomadcxx/sysc-greet/master/assets/showcase.gif" width="100%" alt="sysc-greet showcase">

---

<br>

### sysc-Go · 139★

The terminal animation library that drives sysc-greet's backgrounds — pure Go, drop-in for any Bubble Tea application, and a standalone CLI when you just want the terminal to do something interesting.

**Standalone effects** — fire, matrix rain, ASCII rain, fireworks, beams, aquarium.
**Text effects** — fire text, matrix art, rain art, pour, print, beam text, ring text, blackhole.

Text effects render through `.bit` bitmap fonts, with a converter for figlet fonts and a TUI editor for drawing your own.

```sh
syscgo -effect matrix -theme eldritch -duration 10
```

[repo →](https://github.com/Nomadcxx/sysc-Go)

<br>

<img src="https://raw.githubusercontent.com/Nomadcxx/sysc-Go/master/assets/matrix.gif" width="100%" alt="matrix rain effect">

---

<br>

### more

| repo | what it is | |
|---|---|---|
| [gSlapper](https://github.com/Nomadcxx/gSlapper) | wallpaper utility — static images + video via gstreamer | 71★ |
| [moonbit](https://github.com/Nomadcxx/moonbit) | system cleaner with a TUI and CLI | 65★ |
| [sysc-walls](https://github.com/Nomadcxx/sysc-walls) | terminal screensaver with idle detection | 39★ |
| [plex2jellyfin](https://github.com/Nomadcxx/plex2jellyfin) | migrate Plex → Jellyfin and keep the library clean | |
| [searxng-RAMA](https://github.com/Nomadcxx/searxng-RAMA) | SearXNG with custom themes and privacy defaults | |
| [noctalia-hermes-agent](https://github.com/Nomadcxx/noctalia-hermes-agent) | Noctalia bar plugin for Hermes Agent | |

### recently

<!-- ACTIVITY:START — refreshed nightly by .github/workflows/readme.yml -->
- 2026-07-27 — plex2jellyfin v0.1.6
- 2026-07-24 — sysc-walls: new commits
- 2026-07-24 — sysc-Go: new commits
<!-- ACTIVITY:END -->

### support

If any of this saves you time: [GitHub Sponsors ♥](https://github.com/sponsors/Nomadcxx) · or grab a [help-wanted issue](https://github.com/search?q=user%3ANomadcxx+label%3A%22help+wanted%22+state%3Aopen&type=issues).
