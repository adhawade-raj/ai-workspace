# Matplotlib format strings (`fmt`) — quick reference

A Matplotlib format string is a short way to specify **marker + line style + color** in a single argument to `plot()`.

General pattern:

```python
plt.plot(x, y, "[marker][line][color]")
```

The parts are optional. For example, `"o-r"` means **circle markers + solid line + red color**.  
`"o--r"` means **circle markers + dashed line + red color**.

> **Important:** `fmt` is mainly used by `plt.plot()`. You can also set `marker=`, `linestyle=`, and `color=` separately. If a component is omitted, Matplotlib uses its default behavior / color cycle.

## 1. Marker symbols

| Format snippet | Marker | Mini pictorial preview | Meaning |
|---|---|---|---|
| `o` | Circle | `—●—` | Circle at each data point |
| `s` | Square | `—■—` | Square at each data point |
| `^` | Triangle up | `—▲—` | Upward triangle |
| `v` | Triangle down | `—▼—` | Downward triangle |
| `<` | Triangle left | `—◀—` | Left-facing triangle |
| `>` | Triangle right | `—▶—` | Right-facing triangle |
| `D` | Diamond | `—◆—` | Diamond |
| `d` | Thin diamond | `—◇—` | Narrow diamond |
| `p` | Pentagon | `—⬟—` | Five-sided marker |
| `h` | Hexagon 1 | `—⬢—` | Hexagon marker |
| `H` | Hexagon 2 | `—⬡—` | Alternate hexagon marker |
| `*` | Star | `—★—` | Star marker |
| `+` | Plus | `—+—` | Plus sign |
| `x` | Cross | `—×—` | X-shaped cross |
| `X` | Filled cross | `—✖—` | Filled X marker |
| `\|` | Vertical line | `—│—` | Vertical tick marker |
| `_` | Horizontal line | `———` | Horizontal tick marker |
| `.` | Point | `—·—` | Very small point marker |
| `,` | Pixel | `—▪—` | Pixel-sized marker |

## 2. Line styles

| Format snippet | Line style | Mini pictorial preview | Meaning |
|---|---|---|---|
| `-` | Solid | `━━━━━━━━━━━━` | Continuous line |
| `--` | Dashed | `━━ ━━ ━━ ━━` | Repeating dashes |
| `-.` | Dash-dot | `━━ · ━━ · ━━` | Dash followed by dot |
| `:` | Dotted | `············` | Dots |
| `None` / `''` | No line | `●     ●     ●` | Show markers only, no connecting line |

## 3. Short color codes

| Format snippet | Color name | Mini pictorial preview |
|---|---|---|
| `b` | Blue | `🔵 ━━━━━` |
| `g` | Green | `🟢 ━━━━━` |
| `r` | Red | `🔴 ━━━━━` |
| `c` | Cyan | `🩵 ━━━━━` |
| `m` | Magenta | `🟣 ━━━━━` |
| `y` | Yellow | `🟡 ━━━━━` |
| `k` | Black | `⚫ ━━━━━` |
| `w` | White | `⚪ ━━━━━`* |

*White can be hard to see on a white background. Use a contrasting axes background or marker edge when needed.*

## 4. Combining marker + line + color

| Format string | Pictorial preview | Breakdown |
|---|---|---|
| `"o-r"` | 🔴—●—🔴 | `o` circle + `-` solid line + `r` red |
| `"o--r"` | 🔴 - - ● - - 🔴 | `o` circle + `--` dashed line + `r` red |
| `"s:g"` | 🟢··■··🟢 | `s` square + `:` dotted line + `g` green |
| `"^-.b"` | 🔵—·—▲—·—🔵 | `^` triangle + `-.` dash-dot line + `b` blue |
| `"x--k"` | ⚫ - - × - - ⚫ | `x` cross + `--` dashed line + `k` black |

**Reading order:** Matplotlib generally accepts the marker, line-style, and color components in a compact format string. The examples above use the common marker → line → color order.

## 6. Your example — Oscar vs Non-Oscar movies

```python
# Non-Oscar Winner Movies
non_oscar_movies = ["Slumdog Millionaire", "Avatar", "Inception", "Hugo", "Lincoln"]
non_oscar_revenue = [378, 2788, 829, 185, 275]  # in $M

plt.plot(years, oscar_revenue, "o-r", label="Oscar Movies")
plt.plot(years, non_oscar_revenue, label="Non Oscar Movies")

plt.title("Oscar VS Non Oscar Movies")
plt.xlabel("Years")
plt.ylabel("Revenue (in $M)")
plt.legend()
```

- `"o-r"`: red solid line with circle markers for each Oscar-movie data point.
- No format string on the second `plot()`: Matplotlib chooses the default line style and the next color from its color cycle.

## 7. Same plot, with the arguments written separately

These two styles are equivalent in intent:

```python
# Compact format string
plt.plot(years, oscar_revenue, "o-r", label="Oscar Movies")

# Explicit keyword arguments
plt.plot(
    years,
    oscar_revenue,
    marker="o",
    linestyle="-",
    color="red",
    label="Oscar Movies"
)
```

## 5. All-in-one mini examples

Each row below shows the complete `fmt` string and its visual idea directly in the Markdown table—no separate image is needed.

| `fmt` string | Mini pictorial preview | What it means |
|---|---|---|
| `"o-r"` | `🔴—●—🔴` | Red solid line with circle markers |
| `"o--r"` | `🔴 ━━ ● ━━ 🔴` | Red dashed line with circle markers |
| `"s:g"` | `🟢··■··🟢` | Green dotted line with square markers |
| `"^-.b"` | `🔵—·—▲—·—🔵` | Blue dash-dot line with triangle markers |
| `"x--k"` | `⚫ ━━ × ━━ ⚫` | Black dashed line with cross markers |
| `"D-y"` | `🟡—◆—🟡` | Yellow solid line with diamond markers |

## Quick memory trick

- **Marker** = shape at each data point (`o`, `s`, `^`)
- **Line style** = how points are connected (`-`, `--`, `:`, `-.`)
- **Color** = line/marker color (`r`, `b`, `g`, etc.)
- **Format string** = combination of these (`"o-r"`, `"s--g"`)
