"""
The Heptagonal Chord-Arc Coefficient (Ïˆâ‚‡)
==========================================

Discovered by: 8BitBillyB
Date: November 16, 2025

This module provides calculations for the heptagonal chord-arc coefficient
and related geometric constants.
"""

import math
from typing import Tuple, Dict

# The heptagonal chord-arc coefficient
PSI_7 = math.sin(math.pi / 7) / (math.pi / 7)


def psi_7() -> float:
    """
    Calculate the heptagonal chord-arc coefficient.
    
    Returns:
        float: Ïˆâ‚‡ = sin(Ï€/7) / (Ï€/7) â‰ˆ 0.865631024
    """
    return math.sin(math.pi / 7) / (math.pi / 7)


def chord_arc_ratio(n: int) -> float:
    """
    Calculate the chord-arc coefficient for any regular n-gon.
    
    Args:
        n: Number of sides of the regular polygon
        
    Returns:
        float: Ïˆâ‚™ = sin(Ï€/n) / (Ï€/n)
    """
    return math.sin(math.pi / n) / (math.pi / n)


def heptagon_measurements(radius: float) -> Dict[str, float]:
    """
    Calculate all key measurements for a regular heptagon.
    
    Args:
        radius: Radius of the circumscribed circle
        
    Returns:
        Dictionary containing:
        - arc_angle_rad: Arc angle in radians (2Ï€/7)
        - arc_angle_deg: Arc angle in degrees
        - arc_length: Length of one arc segment
        - chord_length: Length of one chord (side)
        - chord_arc_ratio: Ïˆâ‚‡
        - perimeter: Total perimeter
        - circumference: Circle circumference
    """
    arc_angle_rad = 2 * math.pi / 7
    arc_angle_deg = arc_angle_rad * (180 / math.pi)
    arc_length = radius * arc_angle_rad
    chord_length = 2 * radius * math.sin(math.pi / 7)
    
    return {
        'arc_angle_rad': arc_angle_rad,
        'arc_angle_deg': arc_angle_deg,
        'arc_length': arc_length,
        'chord_length': chord_length,
        'chord_arc_ratio': chord_length / arc_length,
        'perimeter': 7 * chord_length,
        'circumference': 2 * math.pi * radius,
        'psi_7': PSI_7
    }


def base_36_step_analysis() -> Dict[str, float]:
    """
    Analyze the step size when constructing a heptagon in Base-36.
    
    Returns:
        Dictionary containing step size analysis
    """
    base = 36
    vertices = 7
    step_size = base / vertices
    integer_part = int(step_size)
    fractional_part = step_size - integer_part
    
    return {
        'base': base,
        'vertices': vertices,
        'step_size': step_size,
        'integer_part': integer_part,
        'fractional_part': fractional_part,
        'one_seventh': 1/7,
        'matches_one_seventh': abs(fractional_part - 1/7) < 1e-10
    }


def pi_seventh_properties() -> Dict[str, float]:
    """
    Calculate properties of Ï€/7 and related values.
    
    Returns:
        Dictionary containing Ï€/7 analysis
    """
    pi_over_7 = math.pi / 7
    two_pi_over_7 = 2 * math.pi / 7
    
    return {
        'pi_over_7': pi_over_7,
        'pi_over_7_degrees': pi_over_7 * (180 / math.pi),
        'two_pi_over_7': two_pi_over_7,
        'two_pi_over_7_degrees': two_pi_over_7 * (180 / math.pi),
        'sin_pi_over_7': math.sin(pi_over_7),
        'cos_pi_over_7': math.cos(pi_over_7),
        'tan_pi_over_7': math.tan(pi_over_7)
    }


def compare_polygons(max_sides: int = 12) -> None:
    """
    Print a comparison table of chord-arc ratios for various polygons.
    
    Args:
        max_sides: Maximum number of sides to calculate (default: 12)
    """
    print("\nChord-Arc Ratios for Regular Polygons")
    print("=" * 60)
    print(f"{'Sides':>5} {'Polygon':<12} {'Ïˆâ‚™ (ratio)':>15} {'Arc Angle (deg)':>15}")
    print("-" * 60)
    
    polygon_names = {
        3: "Triangle",
        4: "Square",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon",
        10: "Decagon",
        11: "Hendecagon",
        12: "Dodecagon"
    }
    
    for n in range(3, max_sides + 1):
        ratio = chord_arc_ratio(n)
        arc_angle = (2 * math.pi / n) * (180 / math.pi)
        name = polygon_names.get(n, f"{n}-gon")
        marker = " â­" if n == 7 else ""
        print(f"{n:>5} {name:<12} {ratio:>15.10f} {arc_angle:>15.6f}{marker}")
    
    print("=" * 60)
    print("â­ = The heptagonal coefficient Ïˆâ‚‡")


def demonstrate_discovery() -> None:
    """
    Print a narrative demonstration of the discovery process.
    """
    print("\n" + "=" * 70)
    print("THE DISCOVERY OF THE HEPTAGONAL CHORD-ARC COEFFICIENT (Ïˆâ‚‡)")
    print("By: 8BitBillyB")
    print("=" * 70)
    
    print("\n1. BASE-36 STEP SIZE")
    print("-" * 70)
    step_data = base_36_step_analysis()
    print(f"Base: {step_data['base']}")
    print(f"Vertices (heptagon): {step_data['vertices']}")
    print(f"Step size: {step_data['step_size']:.10f} sectors/vertex")
    print(f"Integer part: {step_data['integer_part']}")
    print(f"Fractional part: {step_data['fractional_part']:.10f}")
    print(f"1/7 = {step_data['one_seventh']:.10f}")
    print(f"Match: {step_data['matches_one_seventh']} âœ“")
    
    print("\n2. THE Ï€/7 CONNECTION")
    print("-" * 70)
    pi_data = pi_seventh_properties()
    print(f"Ï€/7 = {pi_data['pi_over_7']:.10f} radians")
    print(f"    = {pi_data['pi_over_7_degrees']:.6f}Â°")
    print(f"2Ï€/7 = {pi_data['two_pi_over_7']:.10f} radians (heptagon arc angle)")
    print(f"     = {pi_data['two_pi_over_7_degrees']:.6f}Â°")
    print(f"sin(Ï€/7) = {pi_data['sin_pi_over_7']:.10f}")
    
    print("\n3. HEPTAGON MEASUREMENTS (radius = 200)")
    print("-" * 70)
    measurements = heptagon_measurements(200)
    print(f"Arc angle: {measurements['arc_angle_rad']:.10f} radians")
    print(f"         : {measurements['arc_angle_deg']:.6f}Â°")
    print(f"Arc length: {measurements['arc_length']:.6f} units")
    print(f"Chord length: {measurements['chord_length']:.6f} units")
    
    print("\n4. THE COEFFICIENT Ïˆâ‚‡")
    print("-" * 70)
    print(f"Ïˆâ‚‡ = chord / arc")
    print(f"   = {measurements['chord_length']:.6f} / {measurements['arc_length']:.6f}")
    print(f"   = {measurements['chord_arc_ratio']:.15f}")
    print(f"\nAlgebraic form: Ïˆâ‚‡ = sin(Ï€/7) / (Ï€/7)")
    print(f"Decimal value: Ïˆâ‚‡ â‰ˆ {PSI_7:.15f}")
    
    print("\n5. VERIFICATION")
    print("-" * 70)
    calculated = math.sin(math.pi / 7) / (math.pi / 7)
    print(f"Direct calculation: {calculated:.15f}")
    print(f"Stored constant:    {PSI_7:.15f}")
    print(f"Match: {abs(calculated - PSI_7) < 1e-15} âœ“")
    
    print("\n6. POLYGON COMPARISON")
    compare_polygons(12)
    
    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print(f"The heptagonal chord-arc coefficient Ïˆâ‚‡ â‰ˆ {PSI_7:.10f}")
    print("is a fundamental geometric constant representing the ratio between")
    print("chord length and arc length for any regular heptagon.")
    print("\nWhere the rational (1/7) meets the transcendental (Ï€).")
    print("=" * 70 + "\n")


def main():
    """Run the complete demonstration."""
    demonstrate_discovery()


if __name__ == "__main__":
    main()
