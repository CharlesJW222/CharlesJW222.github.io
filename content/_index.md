---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '1rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ''
      headings:
        about: 'About Me'
        education: ''
    design:
      # Apply a gradient background
      css_class: "hbx-bg-gradient top-tight"
      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: rounded # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '📚 My Research Interests'
      subtitle: ''
      text: |-
        My current research interests include but not limited to: <br>
          - Generative AI <br>
          - Responsible AI <br>
          - Agentic AI <br>
          - AI4Science <br>
    
        Please reach out to collaborate 😃
    design:
      columns: '1'
---
