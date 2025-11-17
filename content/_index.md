---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ''
      headings:
        about: 'About Me'
        education: ''
        interests: 'Research Interests'
    design:
      # Apply a gradient background
      heading_style: big
      css_class: "hbx-bg-gradient top-tight"
      css_style: |
      .biography .section-subheading {
        font-size: 1.6rem !important;
        font-weight: 700;
      }
      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: rounded # Options: circle (default), square, rounded

---
