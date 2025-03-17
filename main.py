def generate_deterministic_molecules(num_molecules=5):
    """
    Generates deterministic molecule properties (simulated).

    Args:
        num_molecules: The number of simulated molecules.

    Returns:
        A list of dictionaries, each representing a molecule with deterministic properties.
    """

    molecules = []
    for i in range(num_molecules):
        molecule = {
            "logp": 2.0 + (i * 0.5),
            "molecular_weight": 200 + (i * 50),
            "hbd": i % 3,
            "hba": 2 + (i % 4),
            "activity": 0.1 * (i + 1),
            "toxicity": 0.05 * (i % 2)
        }
        molecules.append(molecule)
    return molecules

def filter_molecules(molecules, filters=None):
    """
    Filters molecules based on specified property ranges.

    Args:
        molecules: A list of molecule dictionaries.
        filters: A dictionary of filter criteria.

    Returns:
        A list of filtered molecule dictionaries.
    """

    if filters is None:
        filters = {}

    filtered_molecules = []
    for molecule in molecules:
        passed_filters = True
        for property_name, property_range in filters.items():
            if not (property_range[0] <= molecule[property_name] <= property_range[1]):
                passed_filters = False
                break

        if passed_filters:
            filtered_molecules.append(molecule)
    return filtered_molecules

def display_molecules(molecules):
  """
  Displays the properties of molecule dictionaries.
  """
  if not molecules:
    print("No molecules to display.")
    return

  for molecule in molecules:
    print(molecule)

# Example usage
simulated_molecules = generate_deterministic_molecules(10)

my_filters = {
    "logp": (2, 5),
    "molecular_weight": (200, 400),
    "hbd": (0, 2),
    "hba": (2, 5),
    "activity": (0.2, 0.8),
    "toxicity": (0.0, 0.1)
}

filtered_molecules = filter_molecules(simulated_molecules, filters=my_filters)

print("Original Molecules:")
display_molecules(simulated_molecules)

print("\nFiltered Molecules:")
display_molecules(filtered_molecules)