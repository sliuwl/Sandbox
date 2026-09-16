# Lecture Note Format

A style guide for lecture notes, derived from `02VariationalCalculus.md`.

---

## 1. Document Structure

- **Title**: Level-1 heading at the top, unnumbered, title case.
  ```markdown
  # Variational Calculus
  ```

- **Reading material**: Immediately below the title, bold label with italicized book title.
  ```markdown
  **Reading material:** Chapter 6 of *Classical Mechanics* by John R. Taylor
  ```

- **Table of Contents**: Level-2 heading `## Table of Contents`, containing a numbered list with jump links. Subsections are indented under their parent section as bullet items.
  ```markdown
  ## Table of Contents

  1. [Single-Variable Functions](#1-single-variable-functions)
  2. [Functionals](#2-functionals)
  3. [Some Examples of Functionals](#3-some-examples-of-functionals)
     - [3.1 Length of a Plane Curve](#31-length-of-a-plane-curve)
  ```

- **Horizontal rules**:
  - `---` (three dashes) after the TOC and before the first section.
  - `------` (six dashes) between every section and subsection.

- **Section numbering**:
  - Major sections: `## N. Title` (H2)
  - Subsections: `### N.M Title` (H3)
  - Do not use unnumbered body sections; if a topic needs a heading, give it a number or absorb it into a numbered subsection.

---

## 2. Mathematics

- **Display math**: Use `$$` on its own lines, surrounded by blank lines.
  ```markdown
  $$
  \frac{df(x)}{dx}=0.
  $$
  ```

- **Inline math**: Use `$...$`.
  ```markdown
  ...a local extremum of $f$...
  ```

- **Important results**: Box the final answer or key formula.
  ```markdown
  $$
  \boxed{ \,y(x)=mx+b\, }
  $$
  ```

- **Derivation chains**: intermediate display lines may use `\[` and `\]` if preferred, but keep the style consistent within one document.

---

## 3. Text Formatting

- **Key terms**: The first time a technical term is introduced, make it **bold**.
  ```markdown
  ...a **stationary point** of $f$...
  ...a **functional**, i.e. a quantity...
  ```

- **Blockquotes (`>`)**: Use for:
  - Explanatory notes (e.g., clarifying notation)
  - Worked examples or concrete illustrations
  - Important cautionary remarks
  ```markdown
  > **Note.** There is a subtle notational difference...
  ```

- **Bullet lists**: Use `-` for enumerating variables, properties, or consequences.
  ```markdown
  - $F[y]$ is the functional.
  - $y(x)$ is the input function.
  ```

- **Numbered lists**: Use `1.` for procedural steps or summaries.
  ```markdown
  1. **Write the functional.**
  2. **Identify the integrand.**
  ```

- **Chinese translations**: Provide the Chinese term in parentheses at first mention of a key named concept.
  ```markdown
  The **brachistochrone problem (最速降线问题)** asks...
  the **fundamental lemma (引理)** of the calculus of variations...
  ```

---

## 4. Figures

Place the image on its own line, followed immediately by a bold figure caption.

```markdown
![
](images/hash.jpg)
**Figure 1**: The path $y = y(x)$ between points 1 and 2...
```

---

## 5. Cross-References and Voice

- Use **first-person plural** ("we study", "we impose", "we get").
- Refer to previous sections by name or number when needed.
- Keep the tone formal but pedagogical.
