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
        interests:
          text: 'Research Interests'
          class: 'big-interests'
    design:
      # Apply a gradient background
      css_class: "hbx-bg-gradient top-tight"
      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: rounded # Options: circle (default), square, rounded
    advanced:
      css_style: |
        /* 单独放大 Research Interests */
        .big-interests {
          font-size: 2.2rem !important;
          line-height: 2.4rem !important;
          font-weight: 700 !important;
        }
    
---
