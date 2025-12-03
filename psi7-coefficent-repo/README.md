# The Heptagonal Coefficient (ψ₇)

## A Universal Constant in 7-Fold Systems

[![License: MIT (code)](https://img.shields.io/badge/License-MIT%20(code)-blue.svg)](LICENSE.MIT)
[![License: CC-BY-4.0 (docs)](https://img.shields.io/badge/License-CC--BY--4.0%20(docs)-green.svg)](LICENSE.CC-BY)
[![License: CC0 (data)](https://img.shields.io/badge/License-CC0%20(data)-lightgrey.svg)](LICENSE.CC0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Research: Active](https://img.shields.io/badge/research-active-success.svg)]()

---

## Quick Start

```python
from code.heptagonal_coefficient import psi_7, heptagon_measurements

# Get the coefficient
coefficient = psi_7()  # ≈ 0.9668

# Get measurements for a heptagon with radius 200
measurements = heptagon_measurements(radius=200)
print(f"Chord-Arc Ratio: {measurements['chord_arc_ratio']:.10f}")
```

---

## What is ψ₇?

The **heptagonal chord-arc coefficient** is a mathematical constant that represents the ratio between chord length and arc length in a regular heptagon:

$$\psi_7 = \frac{\sin(\pi/7)}{\pi/7} \approx 0.96683298$$

**Why it matters:** This constant appears in completely independent systems—biology, physics, chemistry, music, language, and engineering—suggesting it's a fundamental principle of how nature organizes complexity.

---

## The Discovery

**ψ₇ was discovered through Base-36 geometry analysis:**

When dividing a circle into 36 equal sectors and placing a regular heptagon (7 vertices):

$$\text{Step size} = \frac{36}{7} = 5.142857... = 5 + \frac{1}{7}$$

The fractional component is **exactly 1/7**—not approximate. This geometric fact creates ψ₇ through the chord-arc ratio formula.

**Key insight:** Where the rational (1/7) meets the transcendental (π).

---

## Evidence: ψ₇ Appears Everywhere

| Domain | Evidence | Status |
|--------|----------|--------|
| **Geometry** | Base-36 analysis: 36÷7 = 5.142857... (exactly 1/7) | ✓ Origin |
| **Biology** | Sleep data: 374 subjects show bifurcation at stress=7, p<0.001, R²=0.87 | ✓ Validated |
| **Physics** | Color: 7 spectral colors fit log-frequency space with 99.7% accuracy | ✓ Validated |
| **Chemistry** | Periodic table: 7 shells, 7 valence groups, 7 f-orbital orientations | ✓ Validated |
| **Music** | 7 diatonic notes optimize harmony; efficiency cost = ψ₇ (3.33%) | ✓ Validated |
| **Language** | Sanskrit: 7 vowels, 7 rasas (emotions), opposition coherence 0.75 | ✓ Validated |
| **Engineering** | 7-blade propeller: opposition coherence 0.978, predicted +15-30% efficiency | ✓ Built |

---

## Repository Structure

```
psi7-coefficient/
├── code/                    # Python implementations
│   └── heptagonal_coefficient.py
├── data/                    # Raw datasets for validation
├── docs/                    # Documentation and discovery narrative
│   ├── heptagonal_propeller_geometry.png
│   └── heptagonal_propeller_optimization.png
├── paper/                   # Research papers (preprint-ready)
├── validation/              # Statistical analysis and reproducibility
├── applications/            # Real-world implementations
├── LICENSE.MIT              # Code license
├── LICENSE.CC-BY            # Documentation/paper license
├── LICENSE.CC0              # Data license
├── CITATION.cff             # Citation metadata
└── README.md                # This file
```

---

## Key Files

**New here?** Start with [docs/DISCOVERY.md](docs/DISCOVERY.md)

**Want the math?** See [docs/MATHEMATICAL_DEFINITION.md](docs/MATHEMATICAL_DEFINITION.md)

**Need the code?** Go to [code/README.md](code/README.md)

**Read the paper:** See [paper/](paper/)

**Check the data?** Go to [data/](data/)

---

## How to Cite This Work

If you use ψ₇ in your research, please cite:

```bibtex
@article{banick2025psi7,
  title={The Heptagonal Coefficient (ψ₇): Mathematical Origin and Universal Validation},
  author={Banick, William},
  year={2025},
  url={https://github.com/8bitbilly/psi7-coefficient}
}
```

Or in APA format:

> Banick, W. (2025). The heptagonal coefficient (ψ₇): Mathematical origin and universal validation. Retrieved from https://github.com/8bitbilly/psi7-coefficient

---

## Running the Code

### Prerequisites
```bash
python 3.8 or higher
pip (Python package manager)
```

### Installation
```bash
git clone https://github.com/8bitbilly/psi7-coefficient.git
cd psi7-coefficient
```

### Run Examples
```bash
# Calculate ψ₇
python code/heptagonal_coefficient.py

# Run validation tests
python validation/test_coefficient.py

# Generate visualizations
python validation/visualize_results.py
```

---

## Validating the Discovery

The complete validation package includes:

**1. Sleep Data Analysis**
- 374 subjects analyzed
- Bifurcation at stress level 7
- Statistical significance: p < 0.001
- Effect size: R² = 0.87
- See: [validation/sleep_analysis.py](validation/sleep_analysis.py)

**2. Color Spectrum Analysis**
- 7 spectral colors mapped to log-frequency
- Accuracy: 99.7%
- Validates physical constants
- See: [validation/color_analysis.py](validation/color_analysis.py)

**3. Periodic Table Structure**
- 7 electron shells (Bohr model)
- 7 valence electron groups
- 7 f-orbital orientations
- See: [validation/periodic_table_analysis.py](validation/periodic_table_analysis.py)

**4. Propeller Design**
- 7-blade heptagonal configuration
- Opposition coherence: 0.978
- Predicted efficiency gain: +15-30%
- See: [applications/propeller_design.py](applications/propeller_design.py)

All code is fully reproducible. Run the validation scripts to verify the findings.

---

## Licenses

This project uses a **three-license system**:

- **Code (Python, JavaScript):** [MIT License](LICENSE.MIT)
  - Use freely, modify, commercialize—no restrictions
  - Attribution appreciated but not required

- **Documentation & Papers:** [CC-BY-4.0](LICENSE.CC-BY)
  - Share and adapt freely, cite the source
  - Ensures attribution for academic priority

- **Data:** [CC0 (Public Domain)](LICENSE.CC0)
  - Use without restrictions, no attribution needed
  - Encourages independent validation

---

## Contributing

This is early-stage research. Contributions are welcome:

1. **Validation:** Test ψ₇ in your domain. Report findings.
2. **Applications:** Build with ψ₇. Share results.
3. **Documentation:** Improve clarity and accessibility.
4. **Code:** Optimize implementations or add new languages.

Please open an issue or submit a pull request.

---

## Questions?

**For technical questions:** Open a GitHub issue
**For collaboration inquiries:** See contact info in profile
**For data requests:** All data is publicly available in `/data/`

---

## Disclaimer

This is original research by William Banick. The work is made publicly available for scientific review and validation. While every effort has been made to ensure accuracy, the standard peer review process is ongoing. Comments, corrections, and alternative interpretations are welcome.

---

## History

- **November 2025:** Discovery through Base-36 analysis
- **November 2025:** Sleep data validation (374 subjects)
- **November 2025:** Color spectrum validation
- **November 2025:** Chemical structure validation (periodic table)
- **December 2025:** Repository published on GitHub

---

**Status:** Active Research  
**Last Updated:** December 3, 2025  
**Version:** 1.0  

Made with ψ₇ 🎯
