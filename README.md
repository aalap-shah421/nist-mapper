# NIST-Mapper

Map paragraphs of a security policy to NIST 800-53 controls. Embedding-based crosswalk, useful for GRC workflows where someone hands you a 30-page policy doc and asks "what's our coverage?"

> Status: very early scaffold. The CLI skeleton and control catalog loader exist. Embedding similarity is next.

## Quickstart (planned)

```bash
git clone https://github.com/aalap-shah421/nist-mapper.git
cd nist-mapper
pip install -r requirements.txt
python -m nist_mapper map --input policy.pdf --output crosswalk.csv
```

## Why

You have NIST 800-53 controls on your resume. A working tool that maps prose to controls is a much stronger artifact than "familiar with NIST 800-53." Built because half the GRC interviews I do start with "how would you crosswalk a policy?" - so I built the crosswalk.

## Roadmap

- [x] CLI skeleton + control catalog loader
- [ ] PDF/DOCX paragraph extraction (`pypdf`, `python-docx`)
- [ ] Embedding similarity (`sentence-transformers/all-MiniLM-L6-v2`)
- [ ] HTML report grouped by control family
- [ ] Coverage scorecard ("you cover 47 of 1006 controls")
- [ ] Word "compliance crosswalk" doc export

## About

Built by [Aalap Shah](https://aalap-shah421.github.io) - cybersecurity engineering student at GMU. Built on the back of my Mindboard work supporting NIST 800-53 and ISO 27001 control implementation.
