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
    design:
      # Apply a gradient background
      css_class: "home-custom-bg hbx-bg-gradient top-tight"
      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: rounded # Options: circle (default), square, rounded
    advanced:
      css_style: |
        /* 自定义首页背景图 */
        .home-custom-bg {
          background-image: url('/media/home-bg.jpg') !important;
          background-size: cover !important;
          background-position: center !important;
          background-repeat: no-repeat !important;
          background-attachment: fixed !important; /* 可选：固定视差效果 */
        }
---
