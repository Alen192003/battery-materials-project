
from analysis import load_battery_data


def test_dataset_has_expected_technologies():
    data = load_battery_data()

    expected = {"LFP", "NMC", "Sodium-ion", "Solid-state"}

    assert set(data["technology"]) == expected


def test_dataset_has_required_columns():
    data = load_battery_data()

    required = {
        "technology",
        "chemistry",
        "energy_density_wh_kg",
        "cycle_life_cycles",
        "cost_gbp_kwh",
        "data_level",
        "source",
        "notes",
    }

    assert required.issubset(set(data.columns))
