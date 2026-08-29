// Shared slugify used both to build the on-page table of contents and to
// stamp matching ids onto rendered markdown headings, so TOC links land
// exactly on the heading they describe.
export function slugify(text) {
  return String(text)
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
}

// Extract h2/h3 headings from a lesson's raw markdown source, in order,
// de-duplicating slugs the same way GitHub/rehype-slug would (heading,
// heading-1, heading-2, ...).
export function extractHeadings(markdown) {
  if (!markdown) return []
  const lines = markdown.split('\n')
  const seen = new Map()
  const headings = []
  for (const line of lines) {
    const match = /^(#{2,3})\s+(.*)$/.exec(line.trim())
    if (!match) continue
    const depth = match[1].length
    const text = match[2].replace(/[*_`]/g, '').trim()
    let slug = slugify(text)
    const count = seen.get(slug) || 0
    seen.set(slug, count + 1)
    if (count > 0) slug = `${slug}-${count}`
    headings.push({ depth, text, slug })
  }
  return headings
}
