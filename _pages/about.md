---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hello! I’m Jinwei Hu (胡津玮), currently pursuing my Ph.D. in Computer Science at the University of Liverpool under the supervision of Prof. Xiaowei Huang and Dr. Yi Dong. My research focuses on understanding and improving the robustness, interpretability, and reliability of modern AI systems, particularly in safety-critical settings. I am especially interested in LLM-driven agents operating in dynamic or adversarial environments, the emergence of collusive behaviours among autonomous agents, and fine-grained knowledge manipulation techniques such as LLM unlearning. I also work on simulation-driven cyber defence, multi-agent coordination, and the integration of symbolic structure with generative intelligence.

Before starting my Ph.D., I completed an MSc in Applied Computational Science and Engineering with Distinction at Imperial College London, where I conducted research on AI4Science and explainable AI under the supervision of Dr. Sibo Cheng and Dr. Rossella Arcucci from the Data Science Institute.I also hold a First Class BSc (Hons) in Computer Science (Artificial Intelligence) from the University of Liverpool and BSc in Information and Computing Science from Xi’an Jiaotong-Liverpool University.

📚 My current research interests include but not limited to:

- Generative AI
- Responsible AI
- Agentic AI
- AI Safety and Security
- AI4Science
  
Please reach out to collaborate 😃


# 🔥 News
- *2026.04*: &nbsp; 📝 Invited as the **Reviewer** for **NeurIPS 2026**.
- *2026.04*: &nbsp; 🎉 Our paper on multi-agent collusive attack of LLM-based agents in open channel has been accepted at **ACL 2026**.
- *2026.04*: &nbsp; 📝 Invited as the **Journal Referee** for **IEEE Transactions on Neural Networks and Learning Systems (TNNLS)**.  
- *2026.03*: &nbsp; 📝 Invited as the **Journal Referee** for **ACM Transactions on Software Engineering and Methodology (TOSEM)**.  
- *2026.01*: &nbsp; 🎤 Gave an **Oral Presentation** at **AAAI 2026** at **Singapore EXPO**.  
- *2026.01*: &nbsp; 🎉 Our paper on adversarial robustness testing has been accepted at **IEEE ICASSP 2026** which will be hosted at Barcelona, Spain.  

- *2025.12*: &nbsp; 🎤 Invited to present a talk on **AI in Programmatic Agents** at the **Trustworthy AI+ Workshop**, co-hosted by King’s College London and the University of Exeter.  
- *2025.11*: &nbsp; 🎉 Our paper on Agentic AI has been accepted at **AAAI 2026** and selected for an **Oral** Presentation.  
- *2025.09*: &nbsp; 🎉 Our paper on LLM unlearning has been accepted at **NeurIPS 2025**.  
- *2025.09*: &nbsp; 🎉 Our emerging research work on LLM-powered agent's responsibility has been accepted as a poster by **UKAIRS 2025**.  
- *2025.08*: &nbsp; 📝 Served as a **Reviewer** for **NeurIPS 2025**, reviewing submissions in the area of AI safety.  
- *2025.08*: &nbsp; 📝 Served as a **Programme Committee Member** for **AAAI 2026**, contributing to the review process for papers in main technical track.  
- *2025.08*: &nbsp; 🎉 Our paper on randomized smoothing for LLM-driven multi-agent systems was accepted as a Fast Track publication in the top-tier journal **CJoA**.  
- *2025.07*: &nbsp; 🎉 Our paper on adversarial testing for industrial cyber-physical systems, was published in **IEEE Transactions on ICPS**.
- *2025.06*: &nbsp; 🎉 Our paper on safe prunning LoRA has been accepted at **TACL**.   
- *2025.06*: &nbsp; 📝 Served as a **Programme Committee Member** for **UKAIRS 2025**.  
- *2025.02*: &nbsp; 🎉 Our paper on social media deepfake detection which is accepted by **CVPR 2025**.  

- *2024.09*: &nbsp; 🔬 Act as a **Research Associate** and mainly work on the project “CRoCS: Certified Robust and Scalable Autonomous Operation in Cyber Space,” funded by the Alan Turing Institute (AICD Research Centre).  
- *2024.06*: &nbsp; 🏆 Won the **ELLIS Manchester Scholarship** and thanks for supporting me to attended the ELLIS Summer Session hosted at the University of Manchester.  
- *2024.05*: &nbsp; 🎤 Gave a tutorial session about **"How to Control LLMs’ behaviors and Design Strategy to safeguard LLMs"** at TACPS & Trust-AI Reading Group.  
- *2024.05*: &nbsp; 📝 Served as a **Reviewer** for **ECAI 2024**.  
- *2024.01*: &nbsp; 🎉 My Master’s thesis research on **Explainable AI and Chemistry (AI4Science)** was accepted for publication in the top journal **CEJ**.  

- *2023.12*: &nbsp; 🏆 Awarded a **full scholarship** to pursue my PhD at the **University of Liverpool** and joined the Trustworthy Autonomous Cyber Physical Systems (ACPS) Lab, under the supervision of Prof. Xiaowei Huang and Dr. Yi Dong.  
- *2023.10*: &nbsp; 🎓 Graduated from **Imperial College London** and is honored to receive the highest academic award of **Master of Science with Distinction** in UK.  

# 📝 Publications
## Selected Publications in Conference

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/ACL26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage](https://arxiv.org/abs/2601.01685)

**Jinwei Hu**, Xinmiao Huang, Youcheng Sun, Yi Dong, Xiaowei Huang

* We identify and formalize cognitive collusion in LLM agents, and propose a multi-agent generative montage framework that manipulates beliefs using only truthful evidence, revealing a new class of reasoning-driven vulnerabilities in public channel.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026 Oral</div><img src='images/AAAI26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Tapas Are Free! Training-Free Adaptation of Programmatic Agents via LLM-Guided Program Synthesis in Dynamic Environments](https://ojs.aaai.org/index.php/AAAI/article/view/40189)

**Jinwei Hu**, Yi Dong, Youcheng Sun, Xiaowei Huang

* We propose TAPA, a training-free framework that uses LLMs to synthesize agent actions for adaptive decision-making, shifting from policy retraining to action-level adaptation and demonstrating strong performance in cyber defense and swarm control.

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/Nips25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FALCON: Fine-grained Activation Manipulation by Contrastive Orthogonal Unalignment for Large Language Model](https://arxiv.org/abs/2502.01472)

**Jinwei Hu**, Zhenglin Huang, Xiangyu Yin, Wenjie Ruan, Guangliang Cheng, Yi Dong, Xiaowei Huang

* A representation-guided unlearning framework that combines contrastive learning, gradient projection, and information-theoretic metrics to enable more precise knowledge removal in LLMs.
</div>
</div>

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2026</div><img src='images/ICASSP26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DDSA: Dual-Domain Strategic Attack for Spatial-Temporal Efficiency in Adversarial Robustness Testing](https://arxiv.org/abs/2601.14302)

**Jinwei Hu**, Shiyuan Meng, Yi Dong, Xiaowei Huang

* We propose a dual-domain adversarial testing framework that improves efficiency by selectively attacking critical regions and frames, enabling resource-efficient robustness evaluation in real-time image systems.

</div>
</div> -->

## Selected Publications in Journal

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Chinese Journal of Aeronautics</div><img src='images/CJOA.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing](https://www.sciencedirect.com/science/article/pii/S1000936125003851)

**Jinwei Hu**, Yi Dong, Zhengtao Ding, Xiaowei Huang

* We propose a defense framework for LLM-driven multi-agent systems that leverages randomized smoothing to provide probabilistic safety guarantees, mitigating malicious behaviors and hallucination propagation while preserving system performance.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE Transactions on Industrial Cyber-Physical Systems</div><img src='images/TICPS.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Hierarchical Testing With Rabbit Optimization for Industrial Cyber-Physical Systems](https://ieeexplore.ieee.org/abstract/document/11077439)

**Jinwei Hu**, Zezhi Tang, Xin Jin, Benyuan Zhang, Yi Dong, Xiaowei Huang

* We propose HERO, a black-box adversarial testing framework that combines hierarchical analysis and optimization to efficiently generate high-quality time-series adversarial examples, enabling robust evaluation of ICPS applications.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Chemical Engineering Journal</div><img src='images/CEJ.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Explainable AI models for predicting drop coalescence in microfluidics device](https://www.sciencedirect.com/science/article/pii/S1385894723071978)

**Jinwei Hu**, Kewei Zhu, Sibo Cheng, Nina M Kovalchuk, Alfred Soulsby, Mark JH Simmons, Omar K Matar, Rossella Arcucci

* We investigate droplet coalescence prediction in microfluidic systems using machine learning and explainable AI, revealing key physical factors that govern coalescence while ensuring interpretability in AI predictions.

</div>
</div>


**Other publication details are shown in [Google Scholar](https://scholar.google.com/citations?user=lpql_8kAAAAJ).**
<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

# 💻 Involved Projects
- **Robustifying Generative AI through Human-Centric Integration of Neural and Symbolic Methods**  
  - Role: Research Associate  
  - Funding: EU Horizon   
- **CRoCS: Certified Robust and Scalable Autonomous Operation in Cyber Space**  
  - Role: Research Associate  
  - Funding: Alan Turing Institute (AI for Cyber Defence (AICD) Research Centre)
<!--- **Development of AI-Based Digital Platform and Service to Enhance Efficiency and Safety for Ships and PORTs (AI-PASSPORT)**  - Role: Research Associate  - Funding: Innovate UK -->   


# 🎖 Honors and Awards
- *2024.06*: **ELLIS Manchester Scholarship**, the University of Manchester.  
- *2023.12*: **PhD Full Scholarship**, University of Liverpool.  
- *2023.10*: **MSc with Distinction**, Imperial College London.  
- *2022.07*: **BSc with First Class Honours** in Computer Science (Artificial Intelligence), University of Liverpool.  
- *2022.07*: **BSc with First Class Honours** in Information and Computing Science, Xi’an Jiaotong-Liverpool University.  

# 📖 Educations
- *2023.12 – Present*: **PhD in Computer Science**, University of Liverpool, UK  
- *2022.10 – 2023.10*: **MSc in Applied Computational Science and Engineering**, Imperial College London, UK  
- *2020.09 – 2022.07*: **BSc in Computer Science (Artificial Intelligence)**, University of Liverpool, UK  
- *2018.09 – 2020.06*: **BSc in Information and Computing Science**, Xi’an Jiaotong-Liverpool University, China  

# 💬 Invited Talks
- *2026.01*: **Oral Presentation** at **AAAI 2026**, Singapore EXPO. 
- *2025.12*: Invited talk on **AI in Programmatic Agents** at the **Trustworthy AI+ Workshop**, co-hosted by King’s College London and the University of Exeter.  
- *2024.05*: Tutorial on **["How to Control LLMs’ behaviors and Design Strategy to safeguard LLMs"](https://cgi.csc.liv.ac.uk/~acps/tutorial04/)** at TACPS &amp; Trust-AI Reading Group. 

# 🤝 Services
## Journal Reviewing
- **IEEE Transactions on Neural Networks and Learning Systems (TNNLS)**  
- **ACM Transactions on Software Engineering and Methodology (TOSEM)**  
- **IEEE Internet of Things Journal (IoTJ)**  

## Conference Program Committee / Reviewer
- **AAAI 2026**  
- **AAMAS 2026**  
- **NeurIPS 2025/2026**  
- **ICML 2025**  
- **UKAIRS 2025**
- **ECAI 2024**
<!--# 💻 Internships - *2019.05 - 2020.02*, [Lorem](https://github.com/), China.-->
