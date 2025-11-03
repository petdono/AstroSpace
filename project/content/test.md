---
title: Test
author: The astrospace Team
date: 2025-09-29
tags: [html, css, javascript]
description: A test.
check: [<h1>, <p>]
next: advanced-design
prepaste: example.html
---

# Mistune Feature Showcase

This document demonstrates *every* supported Markdown feature.  
It’s intended as a reference to show how every markdown feature shows up on astrospace.

---

## Headings

`<h1 style="color:red; font-family: 'Comic Sans MS'">Custom HTML</h1>`

# H1 Heading
## H2 Heading
### H3 Heading
#### H4 Heading
##### H5 Heading
###### H6 Heading

---

## Emphasis

- *Italic*  
- **Bold**  
- ***Bold Italic***  
- ~~Strikethrough~~ (if `strikethrough` plugin is enabled)

---

## Paragraphs & Line Breaks

This is a paragraph.

This is another paragraph, separated by a blank line.

Line breaks end  
with two spaces.

---

## Blockquotes

> Single line quote  
>
> Multi-line quote
>
> > Nested blockquote

---

## Lists

### Unordered
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3

### Ordered
1. First
2. Second
   1. Sub-second
   2. Sub-second
3. Third

### Task Lists (plugin)
- [x] Completed task
- [ ] Pending task

---

### Code Example

Here’s a Python snippet:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("world"))